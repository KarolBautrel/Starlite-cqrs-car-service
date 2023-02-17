from events.car_events import Car
from starlite import status_codes
from starlite import HTTPException
from repository.car_repository import CarRepository


class CarService:
    def __init__(self):
        self.repository = CarRepository()


    def update_car_price(self, car_id:int, data:dict[str,int]):
        car = self.repository.get(car_id)
        change = data.get("change",0)
        car.change_car_price(change=change)
    def get_car(self, car_id: int):
        car = Car()
        repository = CarRepository()
        car = repository.get(car_id)
        return car


