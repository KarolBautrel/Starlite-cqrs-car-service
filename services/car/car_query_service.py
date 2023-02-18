from schemas.schemas import Car
from repository.car_repository import CarRepository
from typing import List


class CarQueryService:
    def __init__(self):
        self.repository = CarRepository()

    def get_car(self, car_id: int) -> Car:
        car = self.repository.get(car_id)
        car = Car(model=car.model, name=car.name, year=car.year, price=car.price)
        return car

    def get_cars(self) -> List[Car]:
        cars = self.repository.get_all()

        return [
            Car(model=car.model, name=car.name, year=car.year, price=car.price)
            for car in cars
        ]
