from app.utils.validators import OneOf, String, Number, Date
import pytest
import string
import random


class TestOneOfValidator:

    @staticmethod
    def create_test_class(options_dict):
        obj = type('TestClass', (), {'category': OneOf(options_dict)})
        return obj()

    def test_valid(self):
        options_dict = {"option1": True, "option2": False}
        obj = TestOneOfValidator.create_test_class(options_dict)
        obj.category = "option1"
        assert obj.category == "option1"

    def test_invalid(self):
        options_dict = {"option1": True, "option2": False}
        obj = TestOneOfValidator.create_test_class(options_dict)

        with pytest.raises(ValueError):
            obj.category = "option"


class TestNumberValidator:

    @staticmethod
    def create_test_class(minvalue, maxvalue):
        obj = type('TestClass', (), {"name": Number(minvalue, maxvalue)})
        return obj()

    @pytest.mark.parametrize('minvalue, maxvalue', [(-10,10),(0,5)])
    def test_within_range(self, minvalue, maxvalue):
        l_range = range(0, maxvalue+1)
        obj = self.create_test_class(minvalue, maxvalue)
        for num in l_range:
            obj.name = num
            assert obj.name == num

    @pytest.mark.parametrize('minvalue, maxvalue', [(-5, 10), (0, 5)])
    def test_out_of_range(self, minvalue, maxvalue):
        l_range = range(minvalue-5,  maxvalue+5)
        obj = self.create_test_class(minvalue, maxvalue)
        with pytest.raises(ValueError):
            for num in l_range:
                obj.name = num
                assert obj.name == num


class TestStringValidator:

    @staticmethod
    def random_string(n):
        s = ''.join(random.choices(string.ascii_lowercase, k=n))
        return s

    @staticmethod
    def create_test_class(min_len, max_len):
        obj = type('TestClass', (), {"name": String(min_len, max_len)})
        return obj()

    @pytest.mark.parametrize('min_len, max_len', [(-10, 10), (0, 5)])
    def test_within_range(self, min_len, max_len):
        obj = self.create_test_class(min_len, max_len)
        l_range = range(1, max_len)
        for num in l_range:
            s = TestStringValidator.random_string(num)
            obj.name = s
            assert obj.name == s

    @pytest.mark.parametrize('min_len, max_len', [(-5, 10), (0, 5)])
    def test_out_of_range(self, min_len, max_len):
        l_range = range(0, max_len+5)
        obj = self.create_test_class(min_len, max_len)
        with pytest.raises(ValueError):
            for num in l_range:
                s = TestStringValidator.random_string(num)
                obj.name = s
                assert obj.name == s


class TestDateValidator(Date):

    @staticmethod
    def create_test_class():
        obj = type("TestClass", (), {"date": Date()})
        return obj()

    def test_valid_test(self):
        obj = self.create_test_class()
        date = "2023-03-12"
        obj.date = date
        assert obj.date == date

    @pytest.mark.parametrize('date', ["2023/03/12", "2023/35/12"])
    def test_invalid_test(self,date):
        obj = self.create_test_class()
        with pytest.raises(ValueError):
            obj.date = date



