from rest_framework import serializers
from .models import Todo
import re


class TodoCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    text = serializers.CharField(
        max_length=100, min_length=1, write_only=True)
    class Meta:
        model = Todo
        fields = '__all__'

    def validate(self, attrs):
        email = attrs.get('email', '')
        text = attrs.get('text', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, text=text)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'username': user.username,
        }


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ['email', 'text']



        def validate_email(self, email):
            if not re.match("[^@]+@[^@]+\.[^@]+", email):
                raise serializers.ValidationError('email-fake')
            return email

        def validate_text(self, text):
            if not re.findall('\d{100,}',text):
                raise serializers.ValidationError('text<100 ')
            return text


        