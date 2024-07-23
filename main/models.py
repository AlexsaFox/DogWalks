import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint


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


class DogAge (models.IntegerChoices):
    NEWBORN = 1, "новорожденный щенок"
    PUPPY = 2, "щенок"
    ADULT = 3, "взрослая собака"
    OLD = 4, "старенький пес"


class DogSize(models.IntegerChoices):
    SMALL = 1, 'маленький, от 1 до 10 кг'
    MIDDLE = 2, 'средний, от 11 до 45 кг'
    BIG = 3, 'крупный, от 46 до 70 кг'
    HUGE = 4, 'очень крупный, от 71 кг'


class DogColor(models.IntegerChoices):
    LIGHT = 1, "светлый"
    RED = 2, "рыжий"
    DARK = 3, "темный"


class Dog (models.Model):
    age = models.IntegerField(choices=DogAge.choices, default=DogAge.PUPPY)
    breed = models.TextField(default="дворняга", max_length="200")
    size = models.IntegerField(choices=DogSize.choices, default=DogSize.MIDDLE)
    color = models.IntegerField(choices=DogColor)
    activity = models.TextField(max_length="500")
    relations_with_cats = models.BooleanField(null=True)
    relations_with_dogs = models.BooleanField(null=True)
    relations_with_kids = models.BooleanField(null=True)
    relations_with_adults = models.BooleanField(null=True)
    curator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    gender = models.BooleanField(help_text="true - девочка, false - мальчик")
    name = models.TextField(max_length="100")
    address = models.TextField(max_length="100")
    description = models.TextField(max_length="1000")


class DogPhoto(models.Model):
    url = models.FileField(upload_to="dogsphotos")
    dog = models.ForeignKey(to=Dog, on_delete=models.CASCADE)


class Walk(models.Model):
    start = models.DateTimeField(null=False)
    finish = models.DateTimeField(null=True)

    def clean(self):
        if self.finish is None:
            self.finish = self.start + datetime.timedelta(hours=1)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class WalkUserDog(models.Model):
    walk = models.ForeignKey(to=Walk, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    dog = models.ForeignKey(to=Dog, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['walk', 'user', 'dog'], name='unique_user_for_dog')
        ]




