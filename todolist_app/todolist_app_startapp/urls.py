from rest_framework.routers import DefaultRouter
from todolist_app_startapp.views import TodolistViewSet

# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter()

app_name = "todolistapp"


router.register(
    prefix="todolists",
    viewset=TodolistViewSet,
    basename="todolists",
)

urlpatterns = router.urls
