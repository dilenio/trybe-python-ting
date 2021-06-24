class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(0)
        return None

    def search(self, index):
        if index not in range(self.__len__()):
            raise IndexError('list index out of range')
        if self._data:
            return self._data[index]

    def find_file(self, path):
        return path in self._data

    def return_data(self):
        return self._data
