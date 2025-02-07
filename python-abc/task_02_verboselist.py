class VerboseList(list):

    def append(self):
        super().append(item)
        print(f"Added [item] to the list.")

    def extend(self):
        super().extend(item)
        print(f"Extended the list with [x] items.")

    def remove(self):
        super().remove(item)
        print(f"Removed [item] from the list.")

    def pop(self):
        super().pop(item)
        print(f"Popped [item] from the list.")
