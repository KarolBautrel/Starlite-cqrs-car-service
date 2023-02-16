from pydantic import UUID4
from starlite import Controller, Partial, get, post, put, patch, delete

from starlite_project.models.models import Car, CarDTO,CarNoIdDTO


class CarController(Controller):
    path = "/cars"

    @post()
    async def create_car(self, data: CarDTO) -> Car:
        return data.to_model_instance()

    @get()
    async def list_users(self) -> list[Car]:
        return

    @patch(path="/{car_id:int}")
    async def partial_update_user(self, car_id: int, data: Partial[Car]) -> Car:
        ...

    @put(path="/{car_id:int}")
    async def update_user(self, car_id: int, data: Car) -> Car:
        ...

    @get(path="/{car_id:int}")
    async def get_car(self, car_id: int) -> CarNoIdDTO:
        return

    @delete(path="/{car_id:int}")
    async def delete_user(self, car_id: int) -> None:
        ...
