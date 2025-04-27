from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
# # In serializers.py
from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer
# from rest_framework import serializers

class LoginSerializer(DefaultLoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        if email:
            attrs['username'] = email
        return super().validate(attrs)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'department',
            'avatar'
        )