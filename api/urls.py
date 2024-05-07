from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import  PatientViewSet, ScanViewSet
from api.views import PatientViewSet, ScanViewSet


router = DefaultRouter()



router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'scans', ScanViewSet, basename='scan')




urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(router.urls)),  
]
