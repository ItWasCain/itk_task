from django.urls import path
from .views import WalletDetail, WalletOperation


app_name = 'api'

urlpatterns = [
    path(
        'v1/wallets/<wallet_uuid>/operation',
        WalletOperation.as_view(),
        name='wallet_operation'
    ),
    path(
        'v1/wallets/<wallet_uuid>/',
        WalletDetail.as_view(),
        name='wallet_detail'
    ),
]
