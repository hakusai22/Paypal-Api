import base64
import json
import requests
from paypal.authorization import get_test_http_headers, get_productId

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 14:13

# https://developer.paypal.com/docs/api/transaction-search/v1/#balances_get
if __name__ == '__main__':
    params = (
        ('currency_code', 'ALL'),
        ('as_of_time', '2024-02-22T00:00:00-0700'),
        ('include_crypto_currencies', 'true'),
    )
    response = requests.get('https://api-m.sandbox.paypal.com/v1/reporting/balances', headers=get_test_http_headers(), params=params)
    print(response.status_code)
    print(response.text)