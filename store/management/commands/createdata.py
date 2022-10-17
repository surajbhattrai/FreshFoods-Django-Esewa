import random
import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from store.models import Product
from category.models import Category



CATEGORIES = [
    "Meat & Fish",
    "Dairy",
    "Vegetables and fruit",
    "Ice Cream",
    "Bread & bread spreads",
    "Dried Goods",
    "Snacks",
    "Care Products"
]


PRODUCTS = [
    "Turmeric powder - 100 gms",
    "Sugar - 1 kg",
    "Jaggery - 1/2 kg",
    "Idli rice/Boiled rice/Salem rice - 5-7 kgs",
    "Steamed rice or Raw rice/Sona masoori - 5-7 kgs",
    "High quality raw rice for Pongal - 1 kg",
    "Dosa rice ( optional) - 2 kgs",
    "Basmati rice - 1 to 2 kgs",
    "Brown rice(optional) - 1 kgs",
    "Pressed rice / Poha(thick or thin) -1 kgs",
    "Wheat flour - 2 kgs (North Indians, please increase atta to 5 kgs and reduce rice)",
    "Maida - 1/2 kg (For cakes and snacks)",
    "Ragi flour - 1 kg",
    "Millets varieties & oats - 1/2 kg each",
    "Rice flour - 1/2 kg",
    "Besan flour - 1/2 kg",
    "Bombay Rava/ Semolina or Chiroti rava - 1 kg",
    "Wheat rava / samba rava / bansi rava - 1 kg",
    "Idli rava - 1 kg (optional)",
    "Rice rava - 500 gms",
    "Vermicelli / Semiya - 1 packet big",
    "Instant rice sevai -1 big packet",
    "Sago/Javvarisi - 1/2 kg",
    "Tamarind - 1/2 kg",
    "Red chilli - 1/4 kg"
]


class Provider(faker.providers.BaseProvider):
    def ecommerce_category(self):
        return self.random_element(CATEGORIES)

    def ecommerce_products(self):
        return self.random_element(PRODUCTS)


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):

        fake = Faker(["en_US"])
        fake.add_provider(Provider)

        if Category.objects.all().count() == 0:
            for _ in range(8):
                d = fake.unique.ecommerce_category()
                Category.objects.create(category_name=d)
    
        for _ in range(20):
            items = list(Category.objects.all())
            random_item = random.choice(items)
            Product.objects.create(
                product_name=fake.unique.ecommerce_products(),
                description=fake.text(max_nb_chars=100),
                price= random.randint(100, 1500),
                category_id=random_item.id,
            )

        check_products = Product.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of products: {check_products}"))