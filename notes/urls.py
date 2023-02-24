from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.NoteViewSet, basename='notes')

# URLConf
urlpatterns = router.urls