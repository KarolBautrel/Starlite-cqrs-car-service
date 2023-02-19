from db_config import Base
from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.orm import Mapped
from starlite import DTOFactory
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin

dto_factory = DTOFactory(plugins=[SQLAlchemyPlugin()])


class CarCreated(Base):
    __tablename__ = "carCreated"
    id: Mapped[str] = Column(String, primary_key=True)
    car_id: Mapped[int] = Column(Integer, unique=True)
    model: Mapped[str] = Column(String)
    name: Mapped[str] = Column(String)
    year: Mapped[int] = Column(Integer)
    price: Mapped[float] = Column(Float)
    created: DateTime = Column(DateTime, nullable=True)
    sequence_number = Column(Integer, nullable=True)
class CarPriceChanged(Base):
    __tablename__ = "CarPriceChanged"
    id = Column(String, primary_key=True)
    car_id: Mapped[int] = Column(Integer)
    change: Mapped[int] = Column(Integer)
    created: DateTime = Column(DateTime,nullable=True)
    sequence_number = Column(Integer, nullable=True)

car_events = [CarCreated, CarPriceChanged]