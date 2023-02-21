from starlite import Starlite
from db_config import Base, engine, sqlalchemy_plugin, engine
from sqlalchemy.orm import Session
from controllers.car_controller import CarController
from datetime import datetime
from events_storage.car_events import CarCreated
from read_models.car import Car
def on_startup() -> None:
    """Initialize the database."""

    Base.metadata.create_all(engine)
    # with Session(engine) as session:
    #     car_creation_event1 = CarCreated(
    #         car_id=2,
    #         model="Opel",
    #         name="Astra",
    #         year=2008,
    #         price=25000,
    #         created=datetime.now(),
    #
    #     )
    #     car_creation_event2 = CarCreated(
    #
    #         car_id=3,
    #         model="Ford",
    #         name="Mustang",
    #         year=2015,
    #         price=45000,
    #         created=datetime.now(),
    #
    #     )
    #     car_creation_event3 = CarCreated(
    #         car_id=4,
    #         model="Renault",
    #         name="Clio",
    #         year=2003,
    #         price=22000,
    #         created=datetime.now(),
    #
    #     )
    #     car1 = Car(
    #         id = car_creation_event1.id,
    #         model = "Opel",
    #         name = "Astra",
    #         year = 2008,
    #         price = 25000,
    #         created = datetime.now(),
    #     )
    #     car2 = Car(
    #         id = car_creation_event2.id,
    #         model="Ford",
    #         name="Mustang",
    #         year=2015,
    #         price=45000,
    #         created=datetime.now(),
    #     )
    #     car3 = Car(
    #         id = car_creation_event3.id,
    #         model="Renault",
    #         name="Clio",
    #         year=2003,
    #         price=22000,
    #         created=datetime.now(),
    #     )
    #     for event in [car_creation_event1, car_creation_event2, car_creation_event3, car1, car2, car3]:
    #         session.add(event)
    #         session.commit()


app = Starlite(
    route_handlers=[CarController], on_startup=[on_startup], plugins=[sqlalchemy_plugin]
)
