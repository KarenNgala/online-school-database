from django.db import models
# Change to accommodate your user & profile creation requirements
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# write models here