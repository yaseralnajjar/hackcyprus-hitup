import datetime

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class Profile(models.Model):
    IN_RELATIONSHIP = '0'
    SINGLE = '1'
    STATUS_CHOICE = (
                        (IN_RELATIONSHIP, 'in-a-relationship'),
                        (SINGLE, 'single')
                    )

    MALE = '0'
    FEMALE = '1'
    SEX = (
        (MALE, 'male'),
        (FEMALE, 'female')
          )

    photo = models.ImageField(upload_to='')
    name = models.CharField(max_length=80)
    rate = models.IntegerField(default = 0)
    sex = models.CharField(max_length=2, choices=SEX, default= MALE)
    friendly = models.IntegerField(default = 0)
    cheerful = models.IntegerField(default = 0)
    smarty = models.IntegerField(default = 0)
    age = models.IntegerField(default = 0)
    martial = models.CharField(max_length=2, choices=STATUS_CHOICE, default= SINGLE)
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def is_owner(self, user):
        return self.user == user

    def __str__(self):
        return f'{self.pk}: {self.name}'


@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        new_profile = Profile(user=instance, name=instance.name)
        new_profile.save()


class Review(models.Model):
    reviewer = models.ForeignKey(Profile, related_name='reviewers', on_delete=models.CASCADE)
    reviewee = models.ForeignKey(Profile, related_name='reviewees', on_delete=models.CASCADE)
    details = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.reviewer.name} says to {self.reviewee.name}: {self.details}'


class Hitup(models.Model):
    hanger = models.ForeignKey(Profile, related_name='hangers', on_delete=models.CASCADE)
    hangee = models.ForeignKey(Profile, related_name='hangees', on_delete=models.CASCADE)
    expiration = models.DateTimeField()
    allow_review = models.DateTimeField()
    acceptance_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.hanger.name} hangs with {self.hangee.name} ends at {self.expiration}'