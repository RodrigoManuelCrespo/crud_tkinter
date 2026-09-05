class Repository:
    def __init__(self):
        self._items = []
        self._next_id = 1

    def create(self, data):
        item = {"id": self._next_id, **data}
        self._items.append(item)
        self._next_id += 1
        return item

    def read_all(self):
        return list(self._items)

    def update(self, item_id, data):
        for item in self._items:
            if item["id"] == item_id:
                item.update(data)
                return item
        return None

    def delete(self, item_id):
        for indice, item in enumerate(self._items):
            if item["id"] == item_id:
                del self._items[indice]
                return True
        return False
