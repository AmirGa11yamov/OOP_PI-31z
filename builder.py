from abc import ABC, abstractmethod



class Engine():
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.type

class Transmission():
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.type

class Body():
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.type

class CarBuilder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def transmission(self):
        pass

    @abstractmethod
    def body(self):
        pass



class SedanBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = {}

    @property
    def product(self) -> dict:
        product = self._product
        self.reset()
        return product
    
    def engine(self):
        self._product['engine'] = Engine("Бензиновый")

    def transmission(self):
        self._product['transmission'] = Transmission("Механическая")

    def body(self):
        self._product['body'] = Body("Лада Веста")


class SUVBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = {}

    @property
    def product(self) -> dict:
        product = self._product
        self.reset()
        return product
    
    def engine(self):
        self._product['engine'] = Engine("Дизельный")

    def transmission(self):
        self._product['transmission'] = Transmission("Автоматическая")

    def body(self):
        self._product['body'] = Body("BMW X5")


class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = {}

    @property
    def product(self) -> dict:
        product = self._product
        self.reset()
        return product
    
    def engine(self):
        self._product['engine'] = Engine("Бензиновый")

    def transmission(self):
        self._product['transmission'] = Transmission("Автоматическая")

    def body(self):
        self._product['body'] = Body("McLaren GT")



class CarDirector:
    def __init__(self, builder: CarBuilder) -> None:
        self._builder = builder

    def construct_car(self) -> dict:
        self._builder.reset()
        self._builder.engine()
        self._builder.transmission()
        self._builder.body()
        return self._builder.product



if __name__ == "__main__":
    sedan_builder = SedanBuilder()
    director = CarDirector(sedan_builder)
    sedan = director.construct_car()
    print("Создан седан:", f"Двигатель: {sedan['engine']}, Коробка: {sedan['transmission']}, Модель: {sedan['body']}")

    suv_builder = SUVBuilder()
    director = CarDirector(suv_builder)
    suv = director.construct_car()
    print("Создан внедорожник:", f"Двигатель: {suv['engine']}, Коробка: {suv['transmission']}, Модель: {suv['body']}")

    sports_car_builder = SportsCarBuilder()
    director = CarDirector(sports_car_builder)
    sports_car = director.construct_car()
    print("Создан спорткар:", f"Двигатель: {sports_car['engine']}, Коробка: {sports_car['transmission']}, Модель: {sports_car['body']}")
