from engines.engine import Engine
from battery.battery import Battery
from servicable.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine: Engine = None, battery: Battery = None) -> None:
        super().__init__()
        self.engine = engine
        self.battery = battery
    
    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
    
