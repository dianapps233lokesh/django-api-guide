from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,TagViewSet,ProductViewSet


router=DefaultRouter()
router.register('categories',CategoryViewSet,basename='category')
router.register('tags',TagViewSet,basename='tag')
router.register('products',ProductViewSet,basename='product')

urlpatterns=router.urls