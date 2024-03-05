import requests
from paypal.authorization import get_test_http_headers

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 10:10

# https://developer.paypal.com/docs/api/webhooks/v1/#webhooks_list
if __name__ == '__main__':

    response = requests.get('https://api-m.sandbox.paypal.com/v1/notifications/webhooks', headers=get_test_http_headers())
    print(response.status_code)
    print(response.text)
