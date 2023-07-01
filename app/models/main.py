""" Car Rental models"""

from itertools import count
from app.utils.validators import OneOf, String, Number, Date
from datetime import datetime


class RentCarException(Exception):
    """used to raise exceptions related to CarRental class"""


class CarRental:
    """
        take care of Rental registrations
    """
    customer_name = String(5, 30)
    car_category_rented = {"Compact": False, "Premium": False, "Minivan": False}
    car_category = OneOf(car_category_rented)
    car_mileage_before = Number(1)
    date_rented = Date()
    rental_end_date = Date()
    _booking_no = count(1000)
    _base_day_rental = 10
    _per_km_price = 5

    def __init__(self, car_category):
        self.car_category = car_category

    @staticmethod
    def get_date_obj(date):
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        return date_obj

    def rent(self, customer_name, car_mileage_before, date_rented):
        if CarRental.car_category_rented.get(self.car_category, True):
            raise RentCarException(f'Car of {self.car_category} cannot be rented')

        CarRental.car_category_rented[self.car_category] = True
        self.customer_name = customer_name
        self.car_mileage_before = car_mileage_before
        self.date_rented = date_rented

    def no_of_days_rented(self):
        start_day = CarRental.get_date_obj(self.date_rented)
        end_day = CarRental.get_date_obj(self.rental_end_date)
        if start_day == end_day:
            number_of_days = 1
        else:
            number_of_days = end_day - start_day
        return number_of_days.days

    def km_travelled(self, car_mileage_after):
        # since 1 mileage = 1.609km.
        mileage = car_mileage_after - self.car_mileage_before
        return mileage * 1.609

    def calculate_price(self, car_mileage_after):

        if self.car_category == "Compact":
            total_price = CarRental._base_day_rental * self.no_of_days_rented()
        elif self.car_category == "Premium":
            total_price = (CarRental._base_day_rental * self.no_of_days_rented() * 1.2 +
                           CarRental._per_km_price * self.km_travelled(car_mileage_after))

        else:
            total_price = (CarRental._base_day_rental * self.no_of_days_rented() * 1.7 + (
                        CarRental._per_km_price * self.km_travelled(car_mileage_after) * 1.5))
        return total_price

    def return_car(self, car_mileage_after, rental_end_date):
        if not CarRental.car_category_rented[self.car_category]:
            raise RentCarException("Car is not rented")
        CarRental.car_category_rented[self.car_category] = True
        self.rental_end_date = rental_end_date
        return self.calculate_price(car_mileage_after)
        
