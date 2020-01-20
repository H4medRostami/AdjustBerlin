from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Adjust API  ",
      default_version='v1',
      description="A d j u s t",
      contact=openapi.Contact(email="hamedrostami@tuta.io"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   authentication_classes=(BasicAuthentication,),
   permission_classes=(permissions.IsAuthenticated,),

)
