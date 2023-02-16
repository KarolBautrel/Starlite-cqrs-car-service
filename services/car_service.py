from models.models import Car
from starlite import status_codes
from starlite import  HTTPException

class CarService:

    def __init__(self, db_session):
        self.db_session = db_session


    def check_car_exists(self, car_id):
        car = self.db_session.query(Car).filter(Car.id == car_id).first()
        if not car:
            raise HTTPException(status_code=status_codes.HTTP_404_NOT_FOUND)
        return car

    def get_car(self, car_id:int):
       return self.check_car_exists(car_id)

    def get_cars(self):
        return self.db_session.query(Car).all()

    def update_car_price(self, car_id:int, data:dict[str, int]):
        car = self.check_car_exists(car_id)
        if data.get("price",0) < 0:
            raise  HTTPException(status_code=status_codes.HTTP_404_NOT_FOUND,detail="Price must be a positive number" )
        car.price = data.get("price",0)
        self.db_session.commit()
        return True


    def delete_car(self, car_id:int):
        car = self.check_car_exists(car_id)
        self.db_session.delete(car)
        self.db_session.commit()
        return True