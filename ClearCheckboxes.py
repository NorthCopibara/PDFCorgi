from PyPDF2 import PdfFileReader, PdfReader, PdfWriter
from PyPDF2.generic import NameObject


def remove_all_checkboxes(path, target):
    reader = PdfReader(path)
    writer = PdfWriter()

    for pageIdx in range(reader.numPages):
        page = reader.pages[pageIdx]
        writer.add_page(page)

        if '/Annots' not in page:
            continue

        for i in range(len(page["/Annots"])):  # in order to access the "Annots" key
            print((page["/Annots"][i].get_object()))

            if '/FT' not in page["/Annots"][i].get_object():
                continue

            if (page["/Annots"][i].get_object())['/FT'] == "/Btn":
                writer_annot = page["/Annots"][i].get_object()
                writer_annot.update(
                    {
                        #NameObject("/V"): NameObject(target),
                        #NameObject("/AS"): NameObject(target)
                    }
                )

                with open(path, "wb") as output_stream:
                    writer.write(output_stream)
