import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from blog.models import Category,Post
from django.contrib.auth.models import User


from product.models import Product,Brand



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

def seed_brand(n):
    fake=Faker()
    image=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'image_brand/{image[random.randint(0,9)]}'
        )
def seed_product(n):
    fake=Faker()
    flag=['New','Sale','Feature']
    image=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    brand=Brand.objects.all()
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            flag=flag[random.randint(0,2)],
            price=round(random.uniform(5.55,99.99),2),
            sku=random.randint(100,1000000),
            subtitle=fake.text(max_nb_chars=4000),
            descriptions=fake.text(max_nb_chars=40000),
            image=f'image_product/{image[random.randint(0,9)]}',

            brand=brand[random.randint(0,len(brand)-1)],
            quantity=round(random.uniform(5.5,99.9),2)

        )



# seed_category(150)
# seed_post(5)
# seed_brand(200)
seed_product(1500)

    
    