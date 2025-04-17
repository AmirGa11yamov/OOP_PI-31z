from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def produce_car(self):
        pass

    @abstractmethod
    def produce_power_engine(self):
        pass

class ElectricCarFactory(CarFactory):
    def produce_car(self):
        return ElectricCar()

    def produce_power_engine(self):
        return ElectricCar()

class PetrolCarFactory(CarFactory):
    def produce_car(self):
        return PetrolCar()

    def produce_power_engine(self):
        return PetrolCar()

class HybridCarFactory(CarFactory):
    def produce_car(self):
        return HybridCar()

    def produce_power_engine(self):
        return HybridCar()


class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def engine_info(self):
        pass

class ElectricCar(Car):
    def drive(self):
        print("Driving an electric car")

    def engine_info(self):
        print("Electric motor")

class PetrolCar(Car):
    def drive(self):
        print("Driving an petrol car")

    def engine_info(self):
        print("Gasoline engine")

class HybridCar(Car):
    def drive(self):
        print("Driving an hybrid car")

    def engine_info(self):
        print("Hybrid engine")


if __name__ == "__main__":
    electric_factory = ElectricCarFactory()
    petrol_factory = PetrolCarFactory()
    hybrid_factory = HybridCarFactory()

    electric_car = electric_factory.produce_car()
    petrol_car = petrol_factory.produce_car()
    hybrid_car = hybrid_factory.produce_car()

    electric_car.drive()
    electric_car.engine_info()

    petrol_car.drive()
    petrol_car.engine_info()

    hybrid_car.drive()
    hybrid_car.engine_info()