import base64
import json
import requests
from paypal.authorization import get_test_http_headers



# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 11:06

# https://developer.paypal.com/docs/api/subscriptions/v1/#subscriptions_activate
if __name__ == '__main__':

    data = '{ "reason": "yinpeng activity subscription" }'
    response = requests.post('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-M1JD5XEPE5FU/activate', headers=get_test_http_headers(), data=data)

    print(response.status_code)
    print(response.text)