import base64
import json
import requests
from paypal.authorization import *

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 13:42

# https://developer.paypal.com/docs/api/orders/v2/#orders_get
if __name__ == '__main__':

    response = requests.get('https://api-m.sandbox.paypal.com/v2/checkout/orders/6G425611J5230925E', headers=get_test_http_headers())
    print(response.status_code)
    print(response.text)
