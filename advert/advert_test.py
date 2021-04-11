import pytest
import advert
import json


def test_ok():
    input_json = """{
    "title": "python",
    "price": 10,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    actual = advert.obj_from_dict(json.loads(input_json), advert.Advert)
    expected_address = "город Москва, Лесная, 7"
    assert actual.location.address == expected_address


def test_ok_without_price_in_json():
    input_json = """{
    "title": "python",
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    actual = advert.obj_from_dict(json.loads(input_json), advert.Advert)
    expected_price = 0
    assert actual.price == expected_price


def test_fail_invalid_price_scan():
    input_json = """{
    "title": "python",
    "price": -10,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    with pytest.raises(ValueError):
        advert.obj_from_dict(json.loads(input_json), advert.Advert)


def test_fail_invalid_price_set():
    input_json = """{
    "title": "python",
    "price": 10,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""

    adv = advert.obj_from_dict(json.loads(input_json), advert.Advert)
    with pytest.raises(ValueError):
        adv.price = -1
