from django.core.management import BaseCommand
from django.contrib.auth.models import User
import time

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('num_of_users',type=int) 


    def handle(self, *args, **kwargs):
        num  = kwargs.get('num_of_users')
        for item in range(num):
            user = User.objects.create_user(username='MitenT{}'.format(item),password='miten{}'.format(item),email='miten{}@yahoo.com'.format(item))
            print('{} added successfully'.format(user))
            time.sleep(1)
        print('All given users addedd successfully...')