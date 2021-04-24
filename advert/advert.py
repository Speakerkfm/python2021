import json
import keyword


class ColorizeMixin:
    """
    Print title and price attribute with yellow color
    """
    repr_color_code = 33

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};1m' \
               + super(ColorizeMixin, self).__repr__() + \
               f'\033[0;1;1m'


class BaseAdvert:
    repr_color_code = 32  # green

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Advert(ColorizeMixin, BaseAdvert):
    """
    Contains advert info
    """
    _price = 0

    def __setattr__(self, key, value):
        if keyword.iskeyword(key):
            key = key + "_"
        super.__setattr__(self, key, value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, var: int):
        if var < 0:
            raise ValueError("must be >= 0")
        self._price = var


def obj_from_dict(data: dict, cls: object) -> object:
    """
    Convert dict to object
    :param data: dict
    :param cls: class description
    :return: object ob cls
    """
    obj = cls()
    for a, b in data.items():
        if isinstance(b, (list, tuple)):
            setattr(obj, a, [obj_from_dict(x, cls)
                             if isinstance(x, dict)
                             else x for x in b])
        else:
            setattr(obj, a, obj_from_dict(b, cls)
            if isinstance(b, dict) else b)
    return obj


lesson_str = """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
}"""

if __name__ == '__main__':
    lesson = json.loads(lesson_str)
    corgi = obj_from_dict(lesson, Advert)
    print(corgi.class_)
    print(corgi)
    print(corgi.location.address)
