from starlite import Controller, get, patch, Response, post
from services.car.car_command_service import CarCommandService
from services.car.car_query_service import CarQueryService
from starlite import status_codes
from schemas.schemas import Car
from typing import List


class CarController(Controller):
    path = "/cars"

    @patch(path="/{car_id:int}")
    def update_car_price(self, car_id: int, data: dict[str, int]) -> Response:
        CarCommandService().update_car_price(car_id, data)
        return Response(status_code=status_codes.HTTP_200_OK, content={"Status": "price updated"})

    @get(path="/")
    def get_cars(self) -> List[Car]:
        cars = CarQueryService().get_cars()
        return cars

    @get(path="/{car_id:int}")
    def get_car(self, car_id: int) -> Car:
        car = CarQueryService().get_car(car_id)

        return car

    @post(path="/{car_id:int}", status_code=status_codes.HTTP_200_OK)
    def buy_car(self, car_id: int) -> None:
        CarCommandService().buy_car(car_id)

    @post(path="/{car_id:int}/cancel", status_code=status_codes.HTTP_200_OK)
    def cancel_car(self, car_id: int) -> None:
        CarCommandService().cancel_car(car_id)
