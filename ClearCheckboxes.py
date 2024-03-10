from PyPDF2 import PdfFileReader, PdfReader, PdfWriter, PdfFileWriter
from PyPDF2.generic import NameObject, ContentStream


def remove_all_checkboxes(path, path_result, target):

    writer = PdfWriter()
    reader = PdfReader(path)

    for pageIdx in range(reader.numPages):
        page = reader.pages[pageIdx]

        writer.add_page(page)

        if '/Annots' not in page:
            continue

        for i in range(len(page["/Annots"])):  # in order to access the "Annots" key
            ant = page["/Annots"][i].get_object()

            if '/FT' not in ant:
                continue

            if ant['/FT'] == "/Btn":
                ant.update(
                    {
                        NameObject("/V"): NameObject(target),
                        NameObject("/AS"): NameObject(target)
                    }
                )

    with open(path_result, "wb") as output_stream:
        writer.write(output_stream)
