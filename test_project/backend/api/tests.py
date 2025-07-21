from http import HTTPStatus

from django.urls import reverse
from django.test import Client, TestCase

from wallets.models import Wallet


class WalletAPITestCase(TestCase):
    WALLET_UUID = '123'
    AMOUNT = 100

    # @classmethod
    def setUp(self):
        self.guest_client = Client()

    @classmethod
    def setUpTestData(cls):
        # cls.guest_client = Client()
        cls.wallet = Wallet.objects.create(
            wallet_uuid=cls.WALLET_UUID,
            amount=cls.AMOUNT,
        )

    def test_wallet_exists(self):
        response = self.guest_client.get('/api/v1/wallets/123/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_wallet_not_exists(self):
        response = self.guest_client.get('/api/v1/wallets/321/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_wallet_deposit(self):
        data = {'operation_type': 'DEPOSIT', 'amount': int(100)}
        url = reverse(
            'api:wallet_operation',
            kwargs={"wallet_uuid": self.wallet.wallet_uuid}
        )
        response = self.guest_client.post(
            url, data=data
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_wallet_withdraw(self):
        data = {'operation_type': 'WITHDRAW', 'amount': 100}
        url = reverse(
            'api:wallet_operation',
            kwargs={"wallet_uuid": self.wallet.wallet_uuid}
        )
        response = self.guest_client.post(
            url, data=data
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_wallet_withdraw_zero_balance(self):
        data = {'operation_type': 'WITHDRAW', 'amount': 200}
        url = reverse(
            'api:wallet_operation',
            kwargs={"wallet_uuid": self.wallet.wallet_uuid}
        )
        response = self.guest_client.post(
            url, data=data
        )
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
