from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserPass (models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    id_card = models.IntegerField(null=True, help_text="если null - то нельзя выгуливать собаку в одиночку")
    is_valid_until_1 = models.DateTimeField(null=False)
    is_valid_until_2 = models.DateTimeField(null=True)
    is_valid_until_3 = models.DateTimeField(null=True)


class UserType (models.IntegerChoices):
    VOLUNTEER = 1, "волонтёр"
    CURATOR = 2, "куратор"


class UserSettings (models.Model):
    type = models.IntegerField(choices=UserType.choices, default=UserType.VOLUNTEER)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone = models.TextField(max_length=20)
    telegram = models.TextField(max_length=200)
    is_validated = models.BooleanField(default=False)






