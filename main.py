from starlite import Starlite, get
from db_config import Base, engine, sqlalchemy_plugin
from sqlalchemy.orm import Session
from models.models import Car


def on_startup() -> None:
    """Initialize the database."""
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        peter = Car(id=1, model="Ford", name="Mustang", year=2005, price=45000)
        session.add(peter)
        session.commit()


app = Starlite(route_handlers=[hello_world],
               on_startup=[on_startup],
               plugins = [sqlalchemy_plugin])
