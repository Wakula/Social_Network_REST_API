from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model


class LoginTrackTokenObtainPairView(TokenObtainPairView):
    def post(self, request):
        result = super().post(request)
        if result.status_code == 200:
            UserModel = get_user_model()
            user = UserModel.objects.get(email=request.data['email'])
            user.update_last_login()
        return result
