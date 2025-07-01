from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from oauth2_provider.views import TokenView,AuthorizationView


urlpatterns=[
    path('api-snippets/',views.SnippetList.as_view()),
    path('api-snippets/<int:pk>/',views.SnippetDetail.as_view()),
    path('api-token-auth/',obtain_auth_token),
    path('api-auth/',include('rest_framework.urls')),
    ]

urlpatterns+=[
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    ]

urlpatterns += [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

# 

# 