import base64
import json
import requests
from paypal.authorization import get_test_http_headers


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/04 14:00

# https://developer.paypal.com/docs/api/subscriptions/v1/#subscriptions_get
if __name__ == '__main__':

    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-3E4DKBFF6MJS', headers=get_test_http_headers())
    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-A23XPN7GR5CG', headers=get_test_http_headers())
    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-UKV9W1WHAM0R', headers=get_test_http_headers())
    # 试用1天
    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-2C2VHYYUKEUD', headers=get_test_http_headers())
    response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-M1JD5XEPE5FU', headers=get_test_http_headers())
    print(response.status_code)
    print(response.text)

