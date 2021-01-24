from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bussinesspart import views

router = DefaultRouter()
router.register(prefix="viewsets", viewset=views.CourseViewSet)

urlpatterns = [

    path("", include(router.urls))
]