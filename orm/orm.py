from simple_orm import SqliteDatabase, Model, fields

db = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = db


class Advert(BaseModel):
    title = fields.CharField(max_length=180)
    price = fields.IntegerField(min_value=0)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    db.connect()
    db.create_tables([Advert])
    a1 = Advert.create(title='iPhone X', price=100)
    print(a1.price)
    adverts = Advert.select()
    assert str(adverts[0]) == 'iPhone X | 100 ₽'
    db.close()
