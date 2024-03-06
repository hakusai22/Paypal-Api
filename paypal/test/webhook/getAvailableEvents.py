import requests
from paypal.authorization import get_test_http_headers

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 10:47


if __name__ == '__main__':

    response = requests.get('https://api-m.sandbox.paypal.com/v1/notifications/webhooks-event-types', headers=get_test_http_headers())
    print(response.status_code)
    print(response.text)
    # PAYMENT.SALE.COMPLETED