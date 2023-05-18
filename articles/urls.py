from articles.views import TaskView, CreateUserView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('tasks', TaskView)
router.register('createUser', CreateUserView)

urlpatterns = router.urls
