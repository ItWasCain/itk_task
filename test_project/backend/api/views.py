import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from wallets.models import Wallet

from .serializers import WalletOperationSerializer, WalletSerializer


class WalletOperation(generics.GenericAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletOperationSerializer
    lookup_url_kwarg = 'wallet_uuid'
    lookup_field = 'wallet_uuid'

    def post(self, request, *args, **kwargs):
        wallet = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            updated_wallet = wallet.perform_operation(
                operation_type=serializer.validated_data['operation_type'],
                amount=serializer.validated_data['amount']
            )

            return Response(
                WalletSerializer(updated_wallet).data,
                status=status.HTTP_200_OK
            )

        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class WalletDetail(generics.RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_url_kwarg = 'wallet_uuid'
    lookup_field = 'wallet_uuid'

    def get_object(self):
        wallet = get_object_or_404(
            self.get_queryset(),
            wallet_uuid=self.kwargs.get(self.lookup_url_kwarg)
        )
        wallet.validate_active()
        return wallet
