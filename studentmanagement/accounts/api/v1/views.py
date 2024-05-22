# management/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import User, Class, Student
from .serializers import UserSerializer, ClassSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from accounts.disable_csrf import CsrfExemptSessionAuthentication
from rest_framework.generics import (
    GenericAPIView, CreateAPIView, ListAPIView,
)
from django.contrib.auth import (
    authenticate,
    get_user_model,
    logout, login)
from rest_framework import status
import binascii
import os




def generate_auth_token_key():
    """
    generate token for users
    """
    return binascii.hexlify(os.urandom(20)).decode()




class GetClassView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    # permission_classes = [permissions.IsAdminUser]

class RegisterStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class LoginView(GenericAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication)
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        user = User.objects.filter(phone=phone).first()

        if not user:
            return Response(data={'message': 'USER_NOT_REGISTERED' }, status=status.HTTP_406_NOT_ACCEPTABLE)
        elif phone and password:
            user = authenticate(request, username=phone, password=password)
      
        else:
            return Response(data={'message': 'INVALID_CREDENTIALS'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if not user:
            return Response(data={'message': 'INVALID CREDENTIALS'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        key = generate_auth_token_key() # generatetoken for user 
        if hasattr(user, 'auth_token'):
            Token.objects.filter(user=user).update(key=key)
        else:
            Token.objects.create(user=user, key=key)
        data = UserSerializer(user).data
        data.update(auth_key=key)
        login(self.request, user) 
        return Response(data={'message': 'Logged In Successfully', 'data': data}, status=status.HTTP_200_OK)

class UpdateProfileView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_object(self):
    #     return self.request.user

