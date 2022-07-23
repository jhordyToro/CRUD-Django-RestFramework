from api.viewsets import CRUDViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('crud', CRUDViewset)