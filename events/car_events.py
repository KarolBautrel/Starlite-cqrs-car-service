from db_config import Base
from sqlalchemy import Column, DateTime, Integer, String, Float, UUID
from sqlalchemy.orm import Mapped, Session, declarative_base, relationship
from starlite import DTOFactory
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin

dto_factory = DTOFactory(plugins=[SQLAlchemyPlugin()])


class Car(Base):
    __tablename__ = "car"
    id: Mapped[int] = Column(Integer, primary_key=True)
    model: Mapped[str] = Column(String)
    name: Mapped[str] = Column(String)
    year: Mapped[int] = Column(Integer)
    price: Mapped[float] = Column(Float)


CarDTO = dto_factory("CarDTO", Car)
CarNoIdDTO = dto_factory("CarNoIdDTO", Car, exclude=["id"])



class CarCreated(Base):
    __tablename__ = "carCreated"
    id: Mapped[int] = Column(Integer, primary_key=True)
    car_id: Mapped[int] = Column(Integer)
    model: Mapped[str] = Column(String)
    name: Mapped[str] = Column(String)
    year: Mapped[int] = Column(Integer)
    price: Mapped[float] = Column(Float)
    created: DateTime = Column(DateTime, nullable=True)

class CarPriceChanged(Base):
    __tablename__ = "CarPriceChanged"
    id = Column(String, primary_key=True)
    car_id: Mapped[int] = Column(Integer)
    change: Mapped[int] = Column(Integer)
    created: DateTime = Column(DateTime,nullable=True)

car_events = [CarCreated, CarPriceChanged]