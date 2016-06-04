"""Script defined to test the Customer class."""


import unittest
import httpretty

from paystackapi.transaction import Transaction


class TestTransaction(unittest.TestCase):
    """Method defined to test transaction initialize."""

    @httpretty.activate
    def test_initialize(self):
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/transaction/initialize",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Transaction.initialize(
            reference='getupall', amount=12000,
            email='samuel.james@andela.com')
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_charge(self):
        httpretty.register_uri(
            httpretty.POST,
            "https://api.paystack.co/transaction/charge_authorization",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Transaction.charge(
            reference='getupall', authorization_code='authorization_code',
            email='email', amount='amount')
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_charge_token(self):
        httpretty.register_uri(
            httpretty.POST,
            "https://api.paystack.co/transaction/charge_token",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Transaction.charge_token(
            reference='getupall', token='token',
            email='email', amount=100000)
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_get(self):
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/transaction/4013",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Transaction.get(transaction_id=4013)
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/transaction",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Transaction.list()
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_totals(self):
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/transaction/totals",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Transaction.totals()
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_verify(self):
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/transaction/verify/reference",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Transaction.verify('reference')
        self.assertTrue(response['status'])
