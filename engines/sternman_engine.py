from engines.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, current_mileage: int = None, last_service_mileage: int = None, warning_light_on: bool = None) -> None:
        super().__init__(current_mileage, last_service_mileage, warning_light_on)
    
    def needs_service(self) -> bool:
        return self.warning_light_on

    