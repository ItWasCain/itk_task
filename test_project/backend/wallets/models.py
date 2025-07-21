from django.db import models, transaction
from rest_framework.exceptions import ValidationError


class Wallet(models.Model):
    wallet_uuid = models.CharField(
        primary_key=True, max_length=200
    )
    amount = models.PositiveIntegerField(
        'Балланс', default=0
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return str(self.wallet_uuid)

    def perform_operation(self, operation_type, amount):
        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(pk=self.pk)
            wallet.validate_active()

            if operation_type == 'DEPOSIT':
                wallet.amount += amount
            elif operation_type == 'WITHDRAW':
                wallet.validate_balance(amount)
                wallet.amount -= amount

            wallet.save()
            return wallet

    def validate_active(self):
        if not self.is_active:
            raise ValidationError('Кошелек не активен')

    def validate_balance(self, amount):
        if self.amount < amount:
            raise ValidationError('Недостаточно средств')
