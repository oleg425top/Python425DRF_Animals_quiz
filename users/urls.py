from django.urls import path
from rest_framework.urls import app_name
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.serializers import UserCreateSerializer
from users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, UserDestroyAPIView, UserRetrieveAPIView, UserTokenObtainPairView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='users_list'),
    path('create/', UserCreateAPIView.as_view(), name='users_create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user_delete'),

]