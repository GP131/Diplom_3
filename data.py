from faker import Faker


class FakeData:
    _faker = None

    def __init__(self):
        if not FakeData._faker:
            FakeData._faker = Faker()

    @classmethod
    def email(cls):
        if cls._faker is None:
            cls._faker = Faker()
        return cls._faker.ascii_free_email()

    @classmethod
    def password(cls):
        if cls._faker is None:
            cls._faker = Faker()
        return cls._faker.password(length=10)

    @classmethod
    def name(cls):
        if cls._faker is None:
            cls._faker = Faker()
        return cls._faker.first_name()
