class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added [item] to the list.")

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [x] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [item] from the list.")

    def pop(self, item):
        super().pop(item)
        print(f"Popped [item] from the list.")
