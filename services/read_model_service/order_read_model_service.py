from db_config import engine
from sqlalchemy.orm import sessionmaker


class OrderReadModelService:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.db_session = Session()
        self.order = None

    def handle_event(self, event):
        exact_event = event.get("event")
        if exact_event == "create_order":
            return self.handle_create_order(event)
        self.find_order_by_id(event.get("id", None))
        if exact_event == "order_status_changed":
            self.handle_change_status(event)


    def find_order_by_id(self,id:int):
        pass

    def handle_create_order(self, event):
        pass

    def handle_change_status(self, event):
        pass
