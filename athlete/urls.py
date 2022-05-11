from django.urls import path, include

app_name = 'athlete'

urlpatterns = [
    path('api/', include('athlete.api.urls')),
]