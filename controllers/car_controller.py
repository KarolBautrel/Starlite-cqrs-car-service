from starlite import Controller, get, post,  patch, delete, HTTPException,Response
from services.car_service import CarService
from sqlalchemy.orm import Session
from starlite.status_codes import HTTP_404_NOT_FOUND
from starlite import status_codes
from events.car_events import CarNoIdDTO, CarDTO
from schemas.schemas import  Car
from repository.car_repository import CarRepository

class CarController(Controller):
    path = "/cars"

    @patch(path="/{car_id:int}")
    def update_car_price(self, car_id: int, db_session: Session, data: dict[str,int])->Response:
        CarService().update_car_price(car_id, data)
        return Response(status_code=status_codes.HTTP_200_OK, content={"Status":"price updated"})
    @get(path="/{car_id:int}")
    def get_car(self, car_id:int) -> Car:
        car = CarService().get_car(car_id)
        return Car(model=car.model,name= car.name,year =  car.year,price= car.price)

