from app.models.main import CarRental
import pytest


class TestCompactType:

    def setup_class(self):
        self.car_rental = CarRental(car_category="Compact")

    @staticmethod
    @pytest.fixture
    def customer_details():
        return {"customer_name": "Test user",
                "car_mileage_before": 5,
                "date_rented": "2023-07-01"}

    def test_create_car_rental(self):
        assert self.car_rental.car_category == "Compact"

    def test_rent_params(self, customer_details):
        self.car_rental.rent(**customer_details)
        for param, value in customer_details.items():
            assert getattr(self.car_rental, param) == value

    def test_category_true_after_rent(self, customer_details):
        self.car_rental.rent(**customer_details)
        assert self.car_rental.car_category_rented["Compact"]

    def test_km_travelled(self, customer_details):
        self.car_rental.rent(**customer_details)
        assert self.car_rental.km_travelled(10) == 8.045

    def test_return(self, customer_details):
        self.car_rental.rent(**customer_details)
        assert self.car_rental.return_car(10, "2023-8-01") == 310


class TestPremiumType:

    def setup_class(self):
        self.car_rental = CarRental(car_category="Premium")

    @staticmethod
    @pytest.fixture
    def customer_details():
        return {"customer_name": "Test user",
                "car_mileage_before": 5,
                "date_rented": "2023-07-01"}

    def test_create_car_rental(self):
        assert self.car_rental.car_category == "Premium"

    def test_category_true_after_rent(self, customer_details):
        self.car_rental.rent(**customer_details)
        assert self.car_rental.car_category_rented["Premium"]

    def test_return(self, customer_details):
        self.car_rental.rent(**customer_details)
        assert self.car_rental.return_car(10, "2023-8-01") == 412.225


class TestMinivanType:

    def setup_class(self):
        self.car_rental = CarRental(car_category="Minivan")

    @staticmethod
    @pytest.fixture
    def customer_details():
        return {"customer_name": "Test user",
                "car_mileage_before": 5,
                "date_rented": "2023-07-01"}

    def test_create_car_rental(self):
        assert self.car_rental.car_category == "Minivan"

    def test_category_true_after_rent(self, customer_details):
        self.car_rental.rent(**customer_details)
        assert self.car_rental.car_category_rented["Minivan"]

    def test_return(self, customer_details):
        self.car_rental.rent(**customer_details)
        assert self.car_rental.return_car(10, "2023-8-01") == 587.3375
