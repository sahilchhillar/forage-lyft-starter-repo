from servicable.serviceable import Serviceable
from datetime import date

class Battery(Serviceable):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        return super().needs_service()