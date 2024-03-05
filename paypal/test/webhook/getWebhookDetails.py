import requests
from paypal.authorization import get_test_http_headers

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 10:44

if __name__ == '__main__':
    response = requests.get('https://api-m.sandbox.paypal.com/v1/notifications/webhooks/30045293K5481613S', headers=get_test_http_headers())
    print(response.status_code)
    print(response.text)

