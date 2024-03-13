class Target:
    page_id = 0
    table_id = 0
    indexes = [0]

    def get_index(self, id):
        return self.indexes[id]

    def __init__(self, page_id, table_id, indexes):
        self.page_id = page_id
        self.table_id = table_id
        self.indexes = indexes