import base64
import json
import requests
from paypal.authorization import get_test_http_headers, get_productId

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 10:54

# https://developer.paypal.com/docs/api/subscriptions/v1/#plans_deactivate
if __name__ == '__main__':

    response = requests.post('https://api-m.sandbox.paypal.com/v1/billing/plans/P-16T534592Y776154BMLL44GY/deactivate', headers=get_test_http_headers())
    print(response.status_code)
    print(response.text)

    response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/plans/P-16T534592Y776154BMLL44GY', headers=get_test_http_headers())
    print(response.status_code)
    print(response.text)
