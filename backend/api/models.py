from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name='reviewers', on_delete=models.CASCADE)
    reviewee = models.ForeignKey(User, related_name='reviewees', on_delete=models.CASCADE)
    details = models.CharField(max_length=500)


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
    user = models.IntegerField(default = 0)
