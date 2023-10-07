class WeaderData:
    def __init__(self):
        self._dict = [] #observers

    def add(self, observer):
        self._dict.append(observer)

    def update(self, new_weaderData):
        for i in self._dict:
            i.display(new_weaderData)

class Observer:
    def __init__(self, name_observer):
        self._name = name_observer

    def display(self, new_weaderData):
        print(f"new weader data: {new_weaderData}")

def main():
    print("main!")
    subject = WeaderData()
    observer_1 = Observer("observer_1")
    observer_2 = Observer("observer_2")
    observer_3 = Observer("observer_3")
    subject.add(observer_1)
    subject.add(observer_2)
    subject.add(observer_3)

    subject.update("Hello world")

if __name__ == "__main__":
    main()
