from faker import Faker
from data.data_countries import COUNTRY


class UserTestData:
    def __init__(self):
        self.random_user_data = None
        self.fake = Faker()

    @classmethod
    def get_random_user_data(cls):
        fake = Faker()
        return {
            'name': fake.name(),
            'email': fake.email(),
            'day_of_birth': "11",
            'month_of_birth': fake.month_name(),
            'year_of_birth': fake.year(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'password': fake.password(length=8),
            'company': fake.company(),
            'address1': fake.street_address(),
            'address2': fake.secondary_address(),
            'country': COUNTRY.CANADA,
            'city': fake.city(),
            'state': fake.state(),
            'zipcode': fake.zipcode(),
            'mobile_number': fake.phone_number()
        }