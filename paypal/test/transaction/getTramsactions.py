import base64
import json
import requests
from paypal.authorization import get_test_http_headers, get_productId


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 14:16

# https://developer.paypal.com/docs/api/transaction-search/v1/#search_get
if __name__ == '__main__':

    params = (
        ('start_date', '2014-07-01T00:00:00-0700'),
        ('end_date', '2014-07-30T23:59:59-0700'),
        ('transaction_id', '5TY05013RG002845M'),
        ('fields', 'all'),
        ('page_size', '100'),
        ('page', '1'),
    )

    response = requests.get('https://api-m.sandbox.paypal.com/v1/reporting/transactions', headers=get_test_http_headers(), params=params)
    print(response.status_code)
    print(response.text)