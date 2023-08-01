from rest_framework import routers
from .api import ProjectViewSet
router = routers.DefaultRouter()

router.register("api/tasks",ProjectViewSet,"tasks")


urlpatterns = router.urls