#projet level urls

from django.contrib import admin
from django.urls import path,include

from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [

	path('admin/', admin.site.urls),

	path('api/v1/',include('notes.urls')),

	#JWT endpoints
    path('api-token-auth/', obtain_jwt_token),
	path('api-token-refresh/', refresh_jwt_token),

	#rest auth endpoint
	path('api/v1/rest-auth/', include('rest_auth.urls')),
	path('api-auth/', include('rest_framework.urls')),


	#all auth endpoint
	path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
]
