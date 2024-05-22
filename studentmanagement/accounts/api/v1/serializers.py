# management/serializers.py

from rest_framework import serializers
from accounts.models import User, Class, Student
from drf_extra_fields.fields import Base64ImageField

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'phone', 'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'status', 'image']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    student_class=ClassSerializer()

    class Meta:
        model = Student
        fields = ['user', 'student_class']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student
    
    
    def update(self, instance, validated_data):
        data = self.context.get('request').data
        user=instance.user
        user.first_name=data['first_name']
        user.last_name=data['last_name']
        user.phone=data['phone']
        user.email=data['email']
        user.date_of_birth=data['date_of_birth']
        if user.image:
            user.image=data['image'] if data['image'] !='' else user.image
        else:
            user.image=data['image']
        user.save()

        cl = instance.student_class
        cl.name=data['class']
        cl.save()
        return instance
