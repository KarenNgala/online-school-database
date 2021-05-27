from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# from django.db.models.signals import post_save
# from django.dispatch import receiver


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff, 
            is_active=True,
            is_superuser=is_superuser, 
            last_login=now,
            date_joined=now, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
      return self._create_user(email, password, False, False, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
      user=self._create_user(email, password, True, True, **extra_fields)
      user.save(using=self._db)
      return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)



class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Year_Of_Study(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Unit(models.Model):
    name = models.CharField(max_length=255)
    course = models.ManyToManyField(Course)
    uni = models.ForeignKey(University, on_delete=models.CASCADE)
    year = models.ForeignKey(Year_Of_Study, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name}"


class File(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    # year_created = 

    def __str__(self):
        return f"{self.name}"