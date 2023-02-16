import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def addUsers(N = 20):
    for user in range(N):
        FirstName = fakegen.first_name()
        LastName = fakegen.last_name()
        Email = fakegen.email()

        User.objects.get_or_create(FirstName = FirstName, LastName = LastName, Email = Email)[0]

if __name__== '__main__':
    print('Populating Users')
    addUsers()
    print('Population Complete!')
