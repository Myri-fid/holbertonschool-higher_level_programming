class CountedIterator:
    def __init__(self):
        pass

    def get_count(self):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        return self 

    def get_count(self):
        return self