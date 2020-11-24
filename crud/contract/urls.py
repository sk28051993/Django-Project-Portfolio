from rest_framework.routers import DefaultRouter
from contract.views import ContractViewSet, get_data, update_data
from django.urls import path, include


router = DefaultRouter()
router.register(r'', ContractViewSet)

urlpatterns = [
    path('all/', get_data, name='get_data'),
    path('update/', update_data, name='get_data'),
] 

urlpatterns += router.urls
