from car.car import Car
from car_factory.model.calliope import Callipe
from datetime import date
from engines.capulet_engine import CapuletEngine
from battery.spindler_battery import SprindlerBattery

if __name__ == "__main__":
    capuletEngine = CapuletEngine(current_mileage=60000, last_service_mileage=20000)
    sprindlerBattery = SprindlerBattery(last_service_date=date.today(), current_date=date.today())

    car = Car(engine=capuletEngine, battery=sprindlerBattery)
    callipe = Callipe(car=car)
    print(callipe.needs_service())
