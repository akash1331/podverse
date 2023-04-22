# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils import timezone

# class UserCustomManager(BaseUserManager):

#     use_in_migrations = True

#     def _create_user(self, phone_number, password, **extra_fields):
#         if not phone_number:
#             raise ValueError('The given phonenumber must be set')
#         user = self.model(phone_number=phone_number, username=phone_number, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, phone_number, password, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(phone_number, password, **extra_fields)

#     def create_superuser(self, phone_number, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(phone_number, password, **extra_fields)


# class User(AbstractUser):
#     # You have to remove 'username' and 'password'!
#     # username = None
#     # password = None
#     email = models.EmailField(null=True, blank=True)
#     is_superuser = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     phone_number = models.IntegerField(unique=True)
#     is_owner = models.BooleanField(default=False)
#     is_advisor = models.BooleanField(default=False)
#     name = models.CharField(max_length=40)
#     image = models.ImageField(blank=True, null=True)
#     data_join = models.DateTimeField(default=timezone.now)
#     code_agency = models.IntegerField(null=True, blank=True, default=0)

#     USERNAME_FIELD = 'phone_number'
#     # You must remove the 'phone_number' from REQUIRED_FIELDS!
#     # Here you can't repeat in the REQUIRED_FIELDS the same field that you put in USERNAME_FIELD, you can add other: 'email', etc ...
#     REQUIRED_FIELDS = []
    

#     objects = UserCustomManager()

#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'