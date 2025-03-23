import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from blog.models import Category,Post
from django.contrib.auth.models import User



from faker import Faker

def seed_category(n):
    fake=Faker()
    for _ in range(n):
        Category.objects.create(
            name=fake.name()
            
        )
def seed_post(n):
    fake=Faker()
    user=User.objects.all()
    image=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    category=Category.objects.all()
    for _ in range(n):
        Post.objects.create(
            title=fake.name(),
            user=user[random.randint(0,len(user)-1)],
            image=f'image_post/{image[random.randint(0,9)]}',
            content=fake.text(max_nb_chars=2000),
            category=category[random.randint(0,len(category)-1)],




        )
# seed_category(150)
seed_post(5)

    
    