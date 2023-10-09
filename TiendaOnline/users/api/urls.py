from django.urls import path
from users.api.api_views import UserAPIView, user_api_view, user_detail_api_view, UserDetailAPIView
from users.views import homeUser
urlpatterns = [    
    #URLS users
    path('userHome/', homeUser,name='userHome'),
    path('user/', UserAPIView.as_view(),name='usuario_api'),
    path('user/<int:pk>/', UserDetailAPIView.as_view(),name='UserDetailAPIView'),
    path('api/users/', user_api_view,name='usuario_api_view'),
    path('api/users/<int:pk>/', user_detail_api_view,name='user_detail_api_view'),
    ]

