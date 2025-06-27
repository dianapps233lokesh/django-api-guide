from django.urls import path
from .views import ItemView,ListUsers,hello_word

urlpatterns = [
    path('items/', ItemView.as_view()),
    path('users/', ListUsers.as_view()),
    path('hello/', hello_word),
]