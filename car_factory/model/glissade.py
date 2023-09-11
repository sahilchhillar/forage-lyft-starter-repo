from battery.battery import Battery
from car.car import Car
from engines.engine import Engine

class Glissade(Car):
    def __init__(self, engine: Engine = None, battery: Battery = None) -> None:
        super().__init__(engine, battery)
    
    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
    
    