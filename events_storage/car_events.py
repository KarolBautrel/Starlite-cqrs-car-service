from db_config import Base
from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.orm import Mapped
from starlite import DTOFactory
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin

dto_factory = DTOFactory(plugins=[SQLAlchemyPlugin()])


class CarCreated(Base):
    __tablename__ = "carCreated"
    id: Mapped[int] = Column(Integer, primary_key=True,autoincrement=True)
    car_id: Mapped[int] = Column(Integer, unique=True)
    model: Mapped[str] = Column(String)
    name: Mapped[str] = Column(String)
    year: Mapped[int] = Column(Integer)
    price: Mapped[float] = Column(Float)
    created: DateTime = Column(DateTime, nullable=True)
class CarBought(Base):
    __tablename__ = "carBought"
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    car_id: Mapped[int] = Column(Integer, unique=True)
    created: DateTime = Column(DateTime, nullable=True)

class CarCancelled(Base):
    __tablename__ = "carBought"
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    car_id: Mapped[int] = Column(Integer, unique=True)
    created: DateTime = Column(DateTime, nullable=True)
class CarPriceChanged(Base):
    __tablename__ = "CarPriceChanged"
    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id: Mapped[int] = Column(Integer)
    change: Mapped[int] = Column(Integer)
    created: DateTime = Column(DateTime,nullable=True)

car_events = [CarBought, CarPriceChanged, CarCreated]