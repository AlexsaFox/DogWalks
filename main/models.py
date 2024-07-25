import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint
from django.shortcuts import get_object_or_404


# Create your models here.


class UserPass (models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    id_card = models.IntegerField(null=False)
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

    def get_walked_dogs(self):
        wuds = WalkUserDog.objects.filter(user=self.user, walk__start__lte=datetime.datetime.now())
        dogs = []
        for wud in wuds:
            dogs.append(wud.dog)
        return dogs

    def get_type(self):
        return UserType(self.type).label


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
    color = models.IntegerField(choices=DogColor.choices)
    activity = models.TextField(max_length="500")
    relations_with_cats = models.BooleanField(null=True)
    relations_with_dogs = models.BooleanField(null=True)
    relations_with_kids = models.BooleanField(null=True)
    relations_with_adults = models.BooleanField(null=True)
    curator = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    gender = models.BooleanField(help_text="true - девочка, false - мальчик")
    name = models.TextField(max_length="100")
    address = models.TextField(max_length="100")
    description = models.TextField(max_length="1000")
    is_actual = models.BooleanField(default=True)

    @staticmethod
    def get_all_dogs(is_actual=True):
        return Dog.objects.filter(is_actual=is_actual)

    def get_last_walk(self):
        dog_walks = self.walks
        if dog_walks.count() == 0:
            return None
        return dog_walks.order_by("-start").first()




class DogPhoto(models.Model):
    url = models.FileField(upload_to="dogsphotos")
    dog = models.ForeignKey(to=Dog, on_delete=models.CASCADE)


class Walk(models.Model):
    start = models.DateTimeField(null=False)
    finish = models.DateTimeField(null=True)

    def clean(self):
        if self.finish is None:
            self.finish = self.start + datetime.timedelta(hours=1)

        if self.finish < self.start:
            raise ValidationError('конец прогулки не может быть раньше её начала')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @staticmethod
    def create_walk(start, user_dogs, finish=None):
        walk = Walk.objects.create(start=start, finish=finish)
        walk.save()
        for user_id in user_dogs.keys():
            dogs = user_dogs[user_id]
            for dog_id in dogs:
                walk.add_dog(dog_id, user_id)

    @staticmethod
    def update_time(walk_id, start=None, finish=None):
        walk = get_object_or_404(Walk, id=walk_id)
        if start is not None:
            walk.start = start
        if finish is not None:
            walk.finish = finish
        walk.save()

    def add_dog(self, dog_id, user_id):
        dog = get_object_or_404(Dog, id=dog_id)
        user = get_object_or_404(User, id=user_id)
        if WalkUserDog.objects.filter(walk=self, dog=dog).count() > 0:
            raise ValidationError('Собака уже гуляет')
        if WalkUserDog.objects.filter(walk=self, user=user).count() > 2:
            raise  ValidationError('У тебя уже есть две собаки')
        wud = WalkUserDog.objects.create(walk=self, user=user, dog=dog)
        wud.save()

    def del_dog(self, dog_id, user_id):
        dog = get_object_or_404(Dog, id=dog_id)
        user = get_object_or_404(User, id=user_id)
        wud = get_object_or_404(WalkUserDog, walk=self, user=user, dog=dog)
        wud.delete()

    def del_user(self, user_id):
        user = get_object_or_404(User, id=user_id)
        wuds = WalkUserDog.objects.filter(walk=self, user=user)
        for wud in wuds:
            wud.delete()


class WalkUserDog(models.Model):
    walk = models.ForeignKey(to=Walk, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    dog = models.ForeignKey(to=Dog, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['walk', 'user', 'dog'], name='unique_user_for_dog')
        ]

    # нужна проверка на количество собак на одного волонтера (не больше двух)

