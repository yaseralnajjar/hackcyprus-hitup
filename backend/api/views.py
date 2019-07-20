from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets, generics

from . import models
from . import serializers


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
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
