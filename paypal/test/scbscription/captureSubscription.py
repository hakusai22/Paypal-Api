import base64
import json
import requests
from paypal.authorization import get_test_http_headers

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 11:14

if __name__ == '__main__':

    data = '{ "note": "yinpeng capture", "capture_type": "OUTSTANDING_BALANCE", "amount": { "currency_code": "USD", "value": "100" } }'
    response = requests.post('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-M1JD5XEPE5FU/capture', headers=get_test_http_headers(), data=data)
    print(response.status_code)
    print(response.text)
