import base64
import json
import requests
from paypal.authorization import get_test_http_headers



# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 11:11

# https://developer.paypal.com/docs/api/subscriptions/v1/#subscriptions_transactions
if __name__ == '__main__':
    params = (
        ('start_time', '2018-01-21T07:50:20.940Z'),
        ('end_time', '2024-02-21T07:50:20.940Z'),
    )

    response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-M1JD5XEPE5FU/transactions', headers=get_test_http_headers(), params=params)
    print(response.status_code)
    print(response.text)