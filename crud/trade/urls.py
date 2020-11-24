from rest_framework.routers import DefaultRouter
from trade.views import tradeViewSet, get_data, update_data
from django.urls import path, include


router = DefaultRouter()
router.register(r'', tradeViewSet)

urlpatterns = [
    path('all/', get_data, name='get_data'),
    path('update/', update_data, name='get_data'),
] 

urlpatterns += router.urls
