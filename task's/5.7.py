class Counter:

    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1

    def get_value(self):
        return self.counter


class WeightedCounter(Counter):

    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def increment(self):
        self.counter += self.weight

    def decrement(self):
        self.counter -= self.weight

    def get_value(self):
        return self.counter


counter = Counter()
counter.increment()
print(counter.get_value())

weighted_counter = WeightedCounter(weight=2)
weighted_counter.increment()
print(weighted_counter.get_value())
