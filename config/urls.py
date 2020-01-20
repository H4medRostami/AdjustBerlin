
from django.conf.urls import url
from authentication.views import SignUp, UserManagement, MyProfile, EditMyProfile
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from swagger import schema_view
from rest_framework.routers import DefaultRouter
from adjustHT.views import Filter

# DRF Default router
router = DefaultRouter()
# client side urls :
router.register(r'v1/father/users', UserManagement, 'user_operation')
# admin side urls :
router.register(r'v1/signup', SignUp, 'signup',)
router.register(r'v1/myprofile', MyProfile, 'my_profile')
router.register(r'v1/editprofile', EditMyProfile, 'edit_my_profile')
router.register(r'v1/Filter', Filter, 'Filter_Dataset')


urlpatterns = [
        url(r'^v1/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('', include(router.urls)),

        url(r'^v1/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
        path('v1/api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('v1/api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

              ]

