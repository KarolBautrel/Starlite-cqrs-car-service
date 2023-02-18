
from repository.car_repository import CarRepository

class CarCommandService:

    def __init__(self):
        self.repository = CarRepository()

    def update_car_price(self, car_id: int, data: dict[str, int]):
        car = self.repository.get(car_id)
        change = data.get("change", 0)
        car.change_car_price(change=change)

    # def delete_car(self, car_id: int):
    #     car = self.check_car_exists(car_id)
    #     self.db_session.delete(car)
    #     self.db_session.commit()
    #     return True