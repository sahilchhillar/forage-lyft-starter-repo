from servicable.serviceable import Serviceable

class Engine(Serviceable):
    def __init__(self, current_mileage: int = None, last_service_mileage: int = None, \
                    warning_light_on: bool = None) -> None:
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on
    
    def needs_service(self):
        return super().needs_service()