class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) != 0:
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        if index < 0 or index > len(self._data):
            raise IndexError("Invalid index")
        return self._data[index]
