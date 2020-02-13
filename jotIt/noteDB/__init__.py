class Repository(object):
    def __init__(self, adapter=None):
        if not adapter:
            raise ValueError("Invalid repository implementation")
        self.client = adapter()

    def find_all(self, selector):
        return self.client.find_all(selector)

    def find(self, selector):
        return self.client.find(selector)

    def create(self, note):
        return self.client.create(note)

    def update(self, selector, note):
        return self.client.update(selector, note)

    def delete(self, selector):
        return self.client.delete(selector)
