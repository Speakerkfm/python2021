import pytest
from .fields import CharField, IntegerField


def test_char_field_ok():
    title_field = CharField(max_length=5)
    title_field._name = 'title'

    class Advert:
        _data = {'title': {}}
        title = title_field

    a = Advert()
    a.title = 'test'

    assert a.title == 'test'


def test_char_field_invalid_length():
    title_field = CharField(max_length=5)
    title_field._name = 'title'

    class Advert:
        _data = {'title': {}}
        title = title_field

    a = Advert()

    with pytest.raises(ValueError):
        a.title = 'test_test_test'

    assert a.title == ''


def test_int_field_ok():
    price_field = IntegerField(min_value=100)
    price_field._name = 'price'

    class Advert:
        _data = {'price': {}}
        price = price_field

    a = Advert()
    a.price = 123

    assert a.price == 123


def test_int_field_invalid_length():
    price_field = IntegerField(min_value=100)
    price_field._name = 'price'

    class Advert:
        _data = {'price': {}}
        price = price_field

    a = Advert()

    with pytest.raises(ValueError):
        a.price = 99

    assert a.price == 100
