import base64
import json
import requests
from paypal.authorization import get_test_http_headers


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 10:58

# https://developer.paypal.com/docs/api/subscriptions/v1/#subscriptions_suspend
if __name__ == '__main__':

    # webhook 收到 event_type=BILLING.SUBSCRIPTION.SUSPENDED
    data = '{ "reason": "yinpeng suspend" }'
    response = requests.post(
        'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-M1JD5XEPE5FU/suspend', headers=get_test_http_headers(), data=data
        )
    print(response.status_code)
    print(response.text)