from datetime import timedelta

from django.shortcuts import render, redirect, reverse

# imports
import random
import string
from rest_framework import generics, authentication, permissions, status
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from . import models
from django.core.mail import send_mail
from django.utils import timezone

from authentication.serializers import (
    AuthTokenSerializer,
    UserProfileSerializer,
    UserRegSerializer,
    OTPSerializer, OTPcreateSerializer
)


class UserRegistration(CreateAPIView):
    """Create new user view"""
    serializer_class = UserRegSerializer


class CreateTokenView(ObtainAuthToken):
    """Create new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileView(generics.RetrieveUpdateAPIView):
    """Retrive and Update authenticated user profile"""
    # queryset = models.User.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrive and return authenticated user"""

        return models.User.objects.get(pk=self.request.user.pk)


def send_otp(email, otp):
    """Sends an OTP to the specified email address."""
    subject = 'Your OTP'
    message = f'Your OTP is: {otp}'
    from_email = 'your_email@example.com'  # Replace with your email
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def generate_otp(length=4):
    """Generates a random OTP of specified length."""
    characters = string.digits
    otp = ''.join(random.choice(characters) for i in range(length))
    return otp


class OTPGenerateView(generics.CreateAPIView):
    serializer_class = OTPcreateSerializer
    # permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        user = request.data.get('email')
        if user:
            otp = generate_otp()  # Replace with your OTP generation logic
            otp_obj = models.Otp.objects.get_or_create(email=user)[0]  # Adjust expiration time as needed

            otp_obj.pin = otp
            otp_obj.expired_at = timezone.now() + timedelta(minutes=5)
            otp_obj.save()

            send_otp(user, otp)  # Replace with your OTP sending logic
            return Response({'detail': 'OTP sent successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Error'}, status=status.HTTP_400_BAD_REQUEST)


class OTPVerifyView(generics.GenericAPIView):
    serializer_class = OTPSerializer
    # permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        user = request.data.get('email')
        otp = request.data.get('pin')
        try:
            otp_obj = models.Otp.objects.get(email=user, pin=otp, expired_at__gte=timezone.now())
            user = models.User.objects.get(email=user)
            user.is_active = True
            otp_obj.delete()
            user.save()
            return Response({'detail': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        except models.Otp.DoesNotExist:
            return Response({'detail': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)