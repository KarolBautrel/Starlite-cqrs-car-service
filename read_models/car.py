from db_config import Base
from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.orm import Mapped
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
    created: DateTime = Column(DateTime, nullable=True)



CarDTO = dto_factory("CarDTO", Car)
CarNoIdDTO = dto_factory("CarNoIdDTO", Car, exclude=["id"])


