import ctypes


class DynamicArray:
    def __init__(self):
        self._count = 0
        self._capacity = 1
        self._arrayA = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self._count

    def __getitem__(self, i):
        if not (0 <= i < self._count):
            raise IndexError('invalid index')
        return self._arrayA[i]

    def append(self, obj):
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
        self._arrayA[self._count] = obj
        self._count += 1

    def _resize(self, capacity):
        arrayB = self._make_array(capacity)
        for i in range(self._count):
            arrayB[i] = self._arrayA[i]
        self._arrayA = arrayB
        self._capacity = capacity

    def __str__(self):
        strg = ""
        for i in range(self._count):
            strg += str(self._arrayA[i]) + " "
        return strg


arr = DynamicArray()
arr.append(1)
arr.append(3)
arr.append('Hello World')
arr.append(5)
arr.append(12)

print(arr)
print(arr._count)
print(arr._capacity)
