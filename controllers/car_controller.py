from pydantic import UUID4
from starlite import Controller, Partial, get, post, put, patch, delete, HTTPException,Router,Response

from starlite.connection.request import  Request
from services.car_service import CarService
from sqlalchemy.orm import Session
from starlite.status_codes import HTTP_404_NOT_FOUND
from starlite import status_codes

from schemas.schemas import Car
from models.models import CarNoIdDTO, CarDTO
class CarController(Controller):
    path = "/cars"

    @post()
    def create_car(self, data: CarDTO) -> CarDTO:
        return data.to_model_instance()

    @get()
    def list_cars(self, db_session:Session) -> list[CarNoIdDTO]:
        return CarService(db_session).get_cars()

    @patch(path="/{car_id:int}")
    def update_car_price(self, car_id: int, db_session: Session, data: dict[str,int])->None:
        CarService(db_session).update_car_price(car_id, data)
        return Response(status_code=status_codes.HTTP_200_OK, content={"Status":"price updated"})
    @get(path="/{car_id:int}")
    def get_car(self, car_id: int, db_session: Session) -> CarNoIdDTO:
        car = CarService(db_session).get_car(car_id)
        if not car:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)
        return car

    @delete(path="/{car_id:int}")
    async def delete_user(self,db_session:Session, car_id: int) -> None:
        CarService(db_session).delete_car(car_id)
        return Response(status_code=status_codes.HTTP_200_OK, content={"Status": "Car deleted"})

