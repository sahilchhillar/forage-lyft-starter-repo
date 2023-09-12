from car.car import Car
from datetime import date
from engines.capulet_engine import CapuletEngine
from battery.spindler_battery import SprindlerBattery
from car_factory.car_factory import CarFactory

if __name__ == "__main__":
    capuletEngine = CapuletEngine(current_mileage=60000, last_service_mileage=50000)
    sprindlerBattery = SprindlerBattery(last_service_date=date.today(), current_date=date.today())

    car = Car(engine=capuletEngine, battery=sprindlerBattery)
    callipe = CarFactory.create_calliope(current_date=sprindlerBattery.current_date, \
                                            last_service_date=sprindlerBattery.last_service_date, \
                                            current_mileage=capuletEngine.current_mileage, \
                                            last_service_mileage=capuletEngine.last_service_mileage)

    print(callipe.needs_service())