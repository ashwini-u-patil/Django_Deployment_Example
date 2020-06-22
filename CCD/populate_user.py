import  os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'CCD.settings')

import  django
django.setup()

from Coffee_Shop.models import User
from faker import Faker

fake = Faker()

def populate(n):
    for entry in range(n):
        fake_name = fake.name().split()
        first_name = fake_name[0]
        last_name = fake_name[1]
        fake_email = fake.email()

        user = User.objects.get_or_create(first_name= first_name,last_name=last_name,email=fake_email)[0]

if __name__ == '__main__':
    print('Populating Database')
    populate(20)
    print("Completed!!!")
