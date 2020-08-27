from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import time
import random
def get_radom_username():
    username = ''
    for i in range(1,random.randint(5,10)):
        username = username + chr(random.randint(50,100))
    return username

def create_users(num):
    for item in range(num):
        user = User.objects.create_user(username=get_radom_username(),
                                        password=get_radom_username(),
                                        email=get_radom_username()+'@gmail.com')
        print('Normal User--> {} added successfully'.format(user))
        time.sleep(1)


def create_super_users(num):
    for item in range(num):
        user = User.objects.create_superuser(username=get_radom_username(),
                                             password=get_radom_username(),
                                             email=get_radom_username()+'@yahoo.com')
        print('SuperUser--> {} added successfully'.format(user))
        time.sleep(1)

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('num_of_users',type=int)#mandatory
        parser.add_argument('-p','--typeofuser', type=str) #type-- staff - superuser

    def handle(self, *args, **kwargs):
        num  = kwargs.get('num_of_users')
        usertype =kwargs.get('typeofuser')#str
        flag = True
        if usertype:
            if usertype=='super':
                    create_super_users(num)
                    flag =False
        if flag:
            create_users(num)
        print('All given users addedd successfully...')