from django.urls import path
from .views import ArticleList, ArticleDetail,PostListPage,PostListLargePage,PostListLimitOffset,PostListCursor,PostListCustom


urlpatterns=[
    path('articles/',ArticleList.as_view(),name='article-list'),
    path('articles/<int:pk>',ArticleDetail.as_view(),name='article-detail'),
    # path('my-articles/',ArticleListByUser.as_view()),
]

urlpatterns += [
    path('posts/', PostListPage.as_view()),
    path('posts-large/', PostListLargePage.as_view()),
    path('posts-limit/', PostListLimitOffset.as_view()),
    path('posts-cursor/', PostListCursor.as_view()),
    path('posts-custom/', PostListCustom.as_view()),
]