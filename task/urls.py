from rest_framework import routers
from .api import ItemViewSet

router = routers.DefaultRouter()
router.register('api/item', ItemViewSet)

urlpatterns = router.urls
