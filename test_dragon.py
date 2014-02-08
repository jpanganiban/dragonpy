import unittest
from dragon import DragonPay
from decimal import Decimal


class TestDragon(unittest.TestCase):

    def setUp(self):
        self.dragon = DragonPay("merchant", "password")

    def tearDown(self):
        self.dragon = None

    def test_format_amount(self):
        self.assertEqual(self.dragon._format_amount(5), "5.00")
        self.assertEqual(self.dragon._format_amount(5.25), "5.25")
        self.assertEqual(self.dragon._format_amount("5.25"), "5.25")
        self.assertEqual(self.dragon._format_amount(Decimal("5")), "5.00")
        self.assertEqual(self.dragon._format_amount(float("5")), "5.00")

    def test_format_digest_parameters(self):
        string = self.dragon._format_digest_parameters('transaction_id', '5.00', 'currency',
                                                       'description hello', 'email')
        self.assertEqual(string, "merchant:transaction_id:5.00:currency:description hello:email:password")

    def test_digest_parameters(self):
        digest = self.dragon._digest_parameters('transaction_id', '5.00', 'currency',
                                                'description hello', 'email')
        self.assertEqual(digest, "21c562afc9d79ebc9f516f42055904f85466a61d")

    def test_pay(self):
        url = self.dragon.pay('transaction_id', 5, 'currency',
                              'description hello', 'email')
        self.assertEqual(url, 'http://test.dragonpay.ph/Pay.aspx?merchantid=merchant&txnid=transaction_id&amount=5.00&ccy=currency&description=description+hello&email=email&digest=21c562afc9d79ebc9f516f42055904f85466a61d')


if __name__ == '__main__':
    unittest.main()
