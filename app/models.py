from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

class MyAccountManager(BaseUserManager):
    """creating the user"""
    def create_user(self, first_name,last_name, username,email, password=None):
        if not email:
            raise ValueError('user most have a email')
        if not username:
            raise ValueError('user most have a username')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,


        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name, username,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password= password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True    
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20)

    """SOME OTHER REQUIED FIELD"""
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name','last_name', 'username']

    objects = MyAccountManager()
    
    def full_name(self):
         return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_lable):
        return True


    
class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100, blank=True)
    address_line_2 = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='user/profile')
    city = models.CharField(blank=True, max_length=20) 
    state = models.CharField(blank=True, max_length=30)
    country = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
         
       
