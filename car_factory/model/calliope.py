from car.car import Car

class Callipe():
    def __init__(self, car: Car = None) -> None:
        super().__init__()
        self.car = car
    
    def needs_service(self) -> bool:
        return self.car.engine.needs_service() or self.car.battery.needs_service()
    
    