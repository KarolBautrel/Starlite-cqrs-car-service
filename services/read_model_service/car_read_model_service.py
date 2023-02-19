from db_config import engine
from sqlalchemy.orm import sessionmaker
from read_models.car import Car
class CarReadModelService:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.db_session = Session()
        self.car = None
    def update_car_model(self, event):
        car_id = event.get("id")
        self.car = self.db_session.query(Car).filter(Car.id == car_id).first()
        if event.get("event") == "price_changed":
            self.handle_change_price_model_save(event)


    def handle_change_price_model_save(self,event):
        price = event.get("price",0)
        self.car.price = price

        self.db_session.commit()
