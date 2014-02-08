Dragon.py
=========

A Dragonpay client.


Usage
-----

```
from flask import redirect
from dragon import DragonPay


# To use test, just change production to False
d = DragonPay("MERCHANTID", "PASSWORD", production=True)

@app.route('/pay')
def pay_controller():
    return redirect(d.pay("TRANSACTIONID", "AMOUNT", "CURRENCY", "DESCRIPTION",
                          "EMAIL"))
```
