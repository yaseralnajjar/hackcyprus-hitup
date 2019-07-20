from django.db import models
from rest_framework import serializers


class Review(models.Model):
    #reviewer = models.ForeignKey(User, related_name='reviews', on_delete=django_models.CASCADE)
    #reviewee = models.ForeignKey(User, related_name='reviews', on_delete=django_models.CASCADE)
    details = models.CharField(max_length=500)


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
