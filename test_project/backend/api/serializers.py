from rest_framework import serializers

from wallets.models import Wallet


OPERATIONS = (
        ('DEPOSIT', 'DEPOSIT'),
        ('WITHDRAW', 'WITHDRAW'),
    )


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        read_only_fields = ('wallet_uuid', 'amount')
        exclude = ('is_active',)


class WalletOperationSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(
        choices=OPERATIONS,
    )
    amount = serializers.IntegerField(min_value=0)

    class Meta:
        fields = ('wallet_uuid', 'amount')
