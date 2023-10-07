from abc import ABC, abstractmethod

class PC:
    def __init__(self):
        self._cpu = None
        self._ram = None

    def __str__(self):
        return f"CPU : {self._cpu}, RAM: {self._ram}"

class Builder(ABC):
    @abstractmethod
    def builderCPU(self):
        ...

    @abstractmethod
    def builderRAM(self):
        ...

    @abstractmethod
    def get_result(self):
        ...

class ConcreteBuilder(Builder):
    def __init__(self):
        self._pc = PC()

    def builderCPU(self):
        self._pc._cpu = "Intel core i9"

    def builderRAM(self):
        self._pc._ram = "DDR4 16Gb"

    def get_result(self):
        return self._pc

class Director:
    def construct(self, builder):
        builder.builderCPU()
        builder.builderRAM()

def main():
    print("main!")
    builder = ConcreteBuilder()
    director = Director()

    director.construct(builder)
    product = builder.get_result()

    print(product)

if __name__ == "__main__":
    main()
