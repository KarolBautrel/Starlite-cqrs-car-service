from starlite import Starlite, get
from db_config import Base, engine, sqlalchemy_plugin
from sqlalchemy.orm import Session
from models.models import Car
from controllers.car_controller import CarController


def on_startup() -> None:
    """Initialize the database."""
    Base.metadata.create_all(engine)
    # with Session(engine) as session:
    #     car = Car(id=3, model="Mercedes", name="a80", year=2005, price=45000)
    #     session.add(car)
    #     session.commit()


app = Starlite(route_handlers=[CarController],
               on_startup=[on_startup],
               plugins=[sqlalchemy_plugin])
