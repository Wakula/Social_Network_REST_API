from django.urls import path

from api.apps.accounts import views


urlpatterns = [
    path('', views.RegistrationView.as_view()),
    path('<int:pk>/last-activity/', views.LastActivityView.as_view()),
]
