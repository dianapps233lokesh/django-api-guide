from django.urls import path
from .views import ProductListByUser,ProductListByURL,ProductListQueryParam,ProductListFilterBackend


urlpatterns=[
    path('products/',ProductListByUser.as_view()),
    path('products/<str:username>',ProductListByURL.as_view()),
    path('products-params/',ProductListQueryParam.as_view()),
    path('products-filter/',ProductListFilterBackend.as_view()),
]