from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from api.apps.authentication.views import LoginTrackTokenObtainPairView
from api.apps.posts.views import LikeAnalyticsView


urlpatterns = [
    path('api/', include([
        path('access-token/', LoginTrackTokenObtainPairView.as_view()),
        path('refresh-token/', TokenRefreshView.as_view()),
        path('accounts/', include('api.apps.accounts.urls')),
        path('posts/', include('api.apps.posts.urls')),
        path('like-analytics/', LikeAnalyticsView.as_view()),
    ])),
]
