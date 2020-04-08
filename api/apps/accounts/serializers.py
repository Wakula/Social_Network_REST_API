from rest_framework import serializers
from api.apps.accounts.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'passwords do not match'})

        user = User(
            email=self.validated_data['email'],
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name')
        )

        user.set_password(password)
        user.save()
        return user


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_login', 'last_activity']
