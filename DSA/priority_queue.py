class PriorityQueue():
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        self.values.append({'value': value, 'priority': priority})
        self.sort()

    def dequeue(self):
        return self.values.pop(0)

    def sort(self):
        self.values.sort(key=lambda item: item['priority'])
