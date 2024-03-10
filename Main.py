from Calc import clac_table

file_path = "Test.pdf"
file_path_result = "Test_result.pdf"
#remove_all_checkboxes(file_path, file_path_result,'/Yes')

class Target:
    page_id = 0
    table_id = 0
    indexes = [0]

    def get_index(self, id):
        return self.indexes[id]

    def __init__(self, page_id, table_id):
        self.page_id = page_id
        self.table_id = table_id


target = Target(4, 0)
target.indexes = [81, 82, 83, 84, 85, 86]
calc_result = clac_table(file_path, target)
print(calc_result)