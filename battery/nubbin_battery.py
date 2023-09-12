from battery.battery import Battery
from datetime import datetime, date

class NubbinBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date) -> None:
        super().__init__(current_date, last_service_date)
    
    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date()