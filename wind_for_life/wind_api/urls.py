from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    
    # The Api Urls
    path('anemometers-readings/add', views.WindReadingCreateView.as_view(), name='anemometer-readings-add'),
    
    path('anemometers-readings/average/<str:name>', views.AnemometerReadingsAverageView.as_view(), name='anemometer-readings-avg'),
    path('anemometers-readings/<int:id>', views.AnemometerAllReadingsListView.as_view(), name='anemometer-readings-list'),
    path('anemometers-readings', views.AnemometerReadingsListView.as_view(), name='anemometer-readings'),
    path('anemometers/<str:name>', views.AnemometerDetailView.as_view(), name='anemometer-detail'),
    path('anemometers', views.AnemometerListCreateView.as_view(), name='anemometer-list-create'),

    # The Token Urls
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # The Swagger Urls
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]