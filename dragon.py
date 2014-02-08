import hashlib
import urllib
from collections import OrderedDict
from decimal import Decimal


class DragonPay(object):
    """Dragonpay class"""

    production = "http://test.dragonpay.ph/Pay.aspx"
    test = "http://test.dragonpay.ph/Pay.aspx"

    def __init__(self, merchant, password, production=False):
        self.merchant = merchant
        self.password = password
        self.url = self.production if production else self.test

    def pay(self, transaction_id, amount, currency, description, email):
        """Pay method"""
        digest = self._digest_parameters(transaction_id,
                                         self._format_amount(amount),
                                         currency,
                                         description,
                                         email)
        parameters = urllib.urlencode(OrderedDict([
            ('merchantid', self.merchant),
            ('txnid', transaction_id),
            ('amount', self._format_amount(amount)),
            ('ccy', currency),
            ('description', description),
            ('email', email),
            ('digest', digest),
        ]))

        return "%s?%s" % (self.url, parameters)

    def _format_digest_parameters(self, transaction_id, amount, currency,
                                  description, email):
        return "%s:%s:%s:%s:%s:%s:%s" % (self.merchant, transaction_id, amount,
                                         currency, description, email,
                                         self.password)

    def _format_amount(self, amount):
        return "%.2f" % Decimal(amount)

    def _digest_parameters(self, transaction_id, amount, currency, description,
                           email):
        """Digests the parameters based on """
        s = "%s:%s:%s:%s:%s:%s:%s" % (self.merchant, transaction_id, amount,
                                      currency, description, email,
                                      self.password)
        return hashlib.sha1(s).hexdigest()
