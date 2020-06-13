class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
        self.index = 0

    def append(self, item):
        # store item in next available spot
        self.storage[self.index] = item

        # update pointer to next spot
        self.index = (self.index + 1) % self.capacity

    def get(self):
        # return values that are not None
        return [value for value in self.storage if value]