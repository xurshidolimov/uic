from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('blog.urls')),
    path('student/', include('students.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('dj_rest_auth/', include('dj_rest_auth.urls')),
]
