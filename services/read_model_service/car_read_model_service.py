from db_config import engine
from sqlalchemy.orm import sessionmaker
from read_models.car import Car


class CarReadModelService:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.db_session = Session()
        self.car = None

    def handle_event(self, event):
        exact_event = event.get("event")
        if exact_event == "create_car":
            return self.handle_create_car(event)
        self.find_car_by_id(event.get("id", None))
        if exact_event == "price_changed":
            self.handle_change_price(event)


    def find_car_by_id(self,id:int):
        if id == None:
            raise Exception
        possible_car = self.db_session.query(Car).filter(Car.id == id).first()
        if not possible_car:
            raise Exception
        self.car = possible_car

    def handle_create_car(self, event):
        self.db_session.add(
            Car(
                model=event.get("model"),
                name=event.get("name"),
                year=event.get("year"),
                price=event.get("price"),
            )
        )
        self.db_session.commit()

    def handle_change_price(self, event):
        price = event.get("price")

        self.car.price = price
        self.db_session.commit()
