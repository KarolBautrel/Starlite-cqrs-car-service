from starlite import Starlite
from db_config import Base, engine, sqlalchemy_plugin, engine
from sqlalchemy.orm import Session
from events.car_events import CarCreated
from controllers.car_controller import CarController
from datetime import datetime
from uuid import uuid4

def on_startup() -> None:
    """Initialize the database."""

    Base.metadata.create_all(engine)
    # with Session(engine) as session:
    #     car_creation_event1 = CarCreated(
    #         id=str(uuid4()),
    #         car_id=2,
    #         model="Opel",
    #         name="Astra",
    #         year=2008,
    #         price=25000,
    #         created=datetime.now(),
    #         sequence_number = 1
    #     )
    #     car_creation_event2 = CarCreated(
    #         id=str(uuid4()),
    #         car_id=3,
    #         model="Ford",
    #         name="Mustang",
    #         year=2015,
    #         price=45000,
    #         created=datetime.now(),
    #         sequence_number=1
    #
    #     )
    #     car_creation_event3 = CarCreated(
    #         id=str(uuid4()),
    #         car_id=4,
    #         model="Renault",
    #         name="Clio",
    #         year=2003,
    #         price=22000,
    #         created=datetime.now(),
    #         sequence_number=1
    #
    #     )
    #     for event in [car_creation_event1, car_creation_event2, car_creation_event3]:
    #         session.add(event)
    #         session.commit()


app = Starlite(
    route_handlers=[CarController], on_startup=[on_startup], plugins=[sqlalchemy_plugin]
)
