from abc import ABC, abstractmethod

class Strategy:
    @abstractmethod
    def execute(self, arr):
        ...

class Bubble(Strategy):
    def execute(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if (arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class Quick(Strategy):
    def execute(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) - 1]
        left = self.execute([x for x in arr if x < pivot])
        right = self.execute([x for x in arr if x > pivot])
        middle = self.execute([x for x in arr if x == pivot])
        return left + middle + right

class Context:
    def __init__(self, strategy, arr):
        self._strategy = strategy
        self._arr = arr[:]

    def execute_strategy(self):
        result = self._strategy.execute(self._arr)
        return result

def main():
    print("main!")
    arr = [1, 4, 2, 7, 5]
    bubble = Bubble()
    quick = Quick()
    context_bubble = Context(bubble, arr)
    context_quick = Context(quick, arr)
    result_1 = context_bubble.execute_strategy()
    result_2 = context_quick.execute_strategy()
    print("result bubble sort:", result_1)
    print("result quick sort:", result_2)

if __name__ == "__main__":
    main()
