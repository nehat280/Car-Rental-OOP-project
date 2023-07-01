"""Contains validators for all datatypes used in model"""

from abc import ABC, abstractmethod
import datetime


class Validator(ABC):
    """This class acts as abstract class for all validators"""
    def __set_name__(self, owner_class, prop_name):
        self.property_name = '_' + prop_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return getattr(instance, self.property_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.property_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class OneOf(Validator):
    def __init__(self, options_dict):
        self.options = set(options_dict.keys())

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"Expected {value!r} to be one of {self.options}")


class String(Validator):
    def __init__(self, min_len, max_len=None):
        self.min_len = min_len if min_len > 1 else 1
        self.max_len = max_len if max_len > 1 else 1

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"{value} must be of string type")
        if self.min_len is not None and len(value) < self.min_len:
            raise ValueError(f"Expected {value!r} must not be smaller than {self.min_len}")
        if self.max_len is not None and len(value) > self.max_len:
            raise ValueError(f"Expected {value!r} must not be greater than {self.max_len}")


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Expected {value!r} to be at least {self.minvalue!r}'
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f'Expected {value!r} to be no more than {self.maxvalue!r}'
            )


class Date(Validator):
    def validate(self, value):
        date_format = "%Y-%m-%d"

        try:
            datetime.datetime.strptime(value, date_format)
        except ValueError:
            raise ValueError("Incorrect string format, should be YY-MM-DD")
