from schemas.schemas import Car
from repository.car_repository import CarRepository
from typing import List
from starlite import HTTPException
from starlite import status_codes

from events_storage.car_events import car_events
class CarQueryService:
    def __init__(self):
        self.repository = CarRepository()



    def get_car(self, car_id: int) -> Car:
        car = self.repository.get(car_id)
        if not car:
            raise HTTPException(status_code=status_codes.HTTP_404_NOT_FOUND)
        return car

    def get_cars(self) -> List[Car]:
        cars = self.repository.get_all()
        return cars
