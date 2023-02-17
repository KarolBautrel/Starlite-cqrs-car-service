from starlite import Starlite
from db_config import Base, engine, sqlalchemy_plugin, engine
from sqlalchemy.orm import Session
from events.car_events import CarCreated
from controllers.car_controller import CarController


def on_startup() -> None:
    """Initialize the database."""
    Base.metadata.create_all(engine)
    # with Session(engine) as session:
    #     car1 = CarCreated(id=2, model="Opel", name="Astra", year=2008, price=25000)
    #     car2 = CarCreated(id=3, model="Ford", name="Mustang", year=2015, price=45000)
    #     car3 = CarCreated(id=4, model="Renault", name="Clio", year=2003, price=22000)
    #     for car in [car1,car2,car3]:
    #         session.add(car)
    #         session.commit()


app = Starlite(
    route_handlers=[CarController], on_startup=[on_startup], plugins=[sqlalchemy_plugin]
)
