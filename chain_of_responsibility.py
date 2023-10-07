from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def __init__(self, demoand, name, successor = None):
        ...
    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class Buyer(Handler):
    def __init__(self, demoand, name, successor=None):
        self.name = name
        self.successor = successor
        self.demoand = demoand

    def handle_request(self, request):
        if request == self.demoand:
            print(f"Accespted by {self.name} -> ({self.demoand})")
        else:
            super().handle_request(request)

if __name__ == "__main__":
    handler_a = Buyer("A", "name_1")
    handler_b = Buyer("B", "name_2", handler_a)
    handler_c = Buyer("C", "name_3", handler_b)

    dict_buyers = { "name_1" : "A", "name_2" : "B", "name_3" : "C"}

    for item in dict_buyers.keys():
        print(f"Отправка запроса: {item}")
        handler_c.handle_request(dict_buyers[item])
