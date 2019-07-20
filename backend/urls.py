"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import path, include

from rest_framework import routers

from .api.views import index_view, ReviewViewSet, ResendConfirmView

router = routers.DefaultRouter()
router.register('reviews', ReviewViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    path('api/auth/', include('rest_auth.urls')),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView, name='password_reset_confirm'),
    path('api/auth/registration/', include('rest_auth.registration.urls')),
    path('api/auth/resend-confirmation/', ResendConfirmView.as_view(), name='resend_confirm_view'),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
]
