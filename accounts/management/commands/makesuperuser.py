from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(first_name="Suraj",last_name="Bhattarai",username="admin", email="admin@gmail.com", password="admin")
            self.stdout.write(self.style.SUCCESS('Successfully created superuser!'))
        else:
            self.stdout.write(self.style.NOTICE('Superuser already exists.'))


 
# class Command(BaseCommand):

#     def add_arguments(self, parser):
#         parser.add_argument("--user", required=True)
#         parser.add_argument("--password", required=True)
#         parser.add_argument("--email", default="admin@example.com")
 
#     def handle(self, *args, **options):
 
#         User = get_user_model()
#         if User.objects.exists():
#             return
 
#         username = options["user"]
#         password = options["password"]
#         email = options["email"]
 
#         User.objects.create_superuser(username=username, password=password, email=email)
 
#         self.stdout.write(f'Local user "{username}" was created')
