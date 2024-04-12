class Target:
    page_id = 0
    table_id = 0
    indexes = [0]

    def get_index(self, id):
        if id >= len(self.indexes):
            print('Not valid target index {}'.format(id))
            return -1

        return self.indexes[id]

    def __init__(self, page_id, table_id, indexes):
        self.page_id = page_id
        self.table_id = table_id
        self.indexes = indexes