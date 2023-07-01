from app.models.main import CarRental
import pytest


class TestCompactType:

    @staticmethod
    @pytest.fixture
    def car_rental():
        return CarRental(car_category="Compact")

    @staticmethod
    @pytest.fixture
    def customer_details():
        return {"customer_name": "Test user",
                "car_mileage_before": 5,
                "date_rented": "2023-07-01"}

    def test_create_car_rental(self, car_rental):
        assert car_rental.car_category == "Compact"

    def test_rent_params(self,car_rental, customer_details):
        car_rental.rent(**customer_details)
        for param, value in customer_details.items():
            assert getattr(car_rental, param) == value

    def test_category_true_after_rent(self, car_rental, customer_details):
        car_rental.rent(**customer_details)
        assert car_rental.car_category_rented["Compact"]

    def test_km_travelled(self, car_rental, customer_details):
        car_rental.rent(**customer_details)
        assert car_rental.km_travelled(10) == 8.045

    def test_return(self, car_rental, customer_details):
        car_rental.rent(**customer_details)
        assert car_rental.return_car(10, "2023-8-01") == 310




