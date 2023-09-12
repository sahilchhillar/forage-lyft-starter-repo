from battery.battery import Battery
from datetime import date, datetime

class SprindlerBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date) -> None:
        super().__init__(current_date, last_service_date)
    
    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < self.current_date