import datetime
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from . import models
from . import serializers

from rest_framework.permissions import BasePermission, IsAuthenticated


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class ResendConfirmView(generics.GenericAPIView):

    serializer_class = serializers.ResendConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({'detail': "Email confirmation sent"})


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    class HisOwnProfile(BasePermission):
        def has_object_permission(self, request, view, obj):
            return obj.is_owner(request.user)

    permission_classes = (IsAuthenticated, HisOwnProfile)

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def update(self, request, pk):
        profile = self.get_queryset().get(pk=pk)
        serializer = serializers.ProfileSerializer(reservation, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class HitupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Hitup.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.HitupSerializer
        elif self.action == 'create':
            return serializers.NewHitupSerializer

    def get_queryset(self):
        #return models.Hitup.objects.all()
        return models.Hitup.objects.filter(hangee__user_id=self.request.user, 
                                           expiration__gt=datetime.datetime.now()).all()

    def create(self, request, *args, **kwargs):
        serializer = serializers.NewHitupSerializer(data=request.data, context={'request': request})
        serializer.is_valid()

        result = serializer.save()
        response = Response(status=status.HTTP_201_CREATED)

        return response

