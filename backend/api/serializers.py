from django.contrib.auth.models import User
from rest_framework import serializers

from allauth.account.forms import ResetPasswordForm, default_token_generator, UserTokenForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import send_email_confirmation, user_pk_to_url_str, setup_user_email
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists

from .models import Review, Profile


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ('name', 'email')


class RegisterSerializer(serializers.Serializer):
    email=serializers.EmailField(required = allauth_settings.EMAIL_REQUIRED)
    name=serializers.CharField(required = True, write_only = True)
    password1=serializers.CharField(required = True, write_only = True)
    password2=serializers.CharField(required = True, write_only = True)

    def validate_email(self, email):
        email=get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(i18n.t('lang.errorMessages.auth.emailAlreadyExists'))

        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(i18n.t('lang.errorMessages.auth.twoPasswordShouldMatch'))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user


class PasswordResetSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if not email_address_exists(email):
            raise serializers.ValidationError(i18n.t('lang.errorMessages.auth.noEmailFound'))
        return email

    def save(self, *args, **kwargs):
        request = self.context.get('request')

        current_site = get_current_site(request)
        email = self.validated_data['email']

        user = User.objects.get(email__iexact=email)

        token_generator = kwargs.get(
            'token_generator', default_token_generator)
        temp_key = token_generator.make_token(user)

        path = f'/reset-password/{user_pk_to_url_str(user)}/{temp_key}'
        url = settings.BASE_URL + path
        context = {'current_site': current_site,
                   'user': user,
                   'password_reset_url': url,
                   'request': request}

        get_adapter().send_mail(
            'account/email/password_reset_key',
            email,
            context)

        return email


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    key = serializers.CharField()

    def validate_new_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, attrs):
        self.user_token_form = UserTokenForm(
            data={'uidb36': attrs['uid'], 'key': attrs['key']})

        if not self.user_token_form.is_valid():
            raise serializers.ValidationError(i18n.t('lang.errorMessages.auth.invalidToken'))

        if attrs['new_password1'] != attrs['new_password2']:
            raise serializers.ValidationError(i18n.t('lang.errorMessages.auth.twoPasswordShouldMatch'))

        self.password = attrs['new_password1']

        return attrs

    def save(self):
        user = self.user_token_form.reset_user
        get_adapter().set_password(user, self.password)
        return user


class ResendConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password_reset_form_class = ResetPasswordForm

    def validate(self, attrs):
        self.reset_form = self.password_reset_form_class(
            data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return attrs

    def save(self):
        request = self.context.get('request')
        email = self.reset_form.cleaned_data['email']
        user = User.objects.get(email__iexact=email)
        send_email_confirmation(request, user, True)
        return email


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'