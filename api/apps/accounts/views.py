from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView


from api.apps.accounts import serializers
from api.apps.accounts.models import User


class LoginTrackTokenObtainPairView(TokenObtainPairView):
    def post(self, request):
        result = super().post(request)
        if result.status_code == 200:
            UserModel = get_user_model()
            user = UserModel.objects.get(email=request.data['email'])
            user.update_last_login()
        return result


class RegistrationView(APIView):
    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LastActivityView(generics.RetrieveAPIView):
    serializer_class = serializers.UserActivitySerializer
    queryset = User.objects.all()
