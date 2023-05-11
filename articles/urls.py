from articles.views import TaskView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('tasks', TaskView)

urlpatterns = router.urls
