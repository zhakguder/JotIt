class TagGroup:
    def __init__(self, tags):
        self._tags = []
        self.getTags().extend(tags)

    def contains(self, tag):
        return tag in self.getTags()

    def getTags(self):
        # TODO: this exposes the list and lets client manipulate the list
        return self._tags

    def sorted(self):
        """Returns a new sorted tags list"""
        return sorted(self.getTags())

    def contains(self, tag):
        return tag in self._tags

    def add_tags(self, tags):
        self._tags.extend(tags)

    def __iter__(self):
        return self.getTags().__iter__()

    def __str__(self):
        str_ = ""
        for tag in self:
            str_ += tag
        return str_
