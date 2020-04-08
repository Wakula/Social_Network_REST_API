from django.urls import path

from api.apps.posts import views


urlpatterns = [
    path('', views.PostListView.as_view()),
    path('<int:pk>/', views.PostView.as_view()),
    path('<int:pk>/like/', views.LikeView.as_view()),
]
