import requests
from paypal.authorization import get_test_http_headers

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 21:33

if __name__ == '__main__':

    params = (
        ('page_size', '10'),
        ('start_time', '2024-03-01T11:00:00Z'),
        ('end_time', '2024-03-05T14:12:05Z'),
        ('event_type', 'PAYMENT.SALE.COMPLETED'),
    )

    response = requests.get(
        'https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events',
        headers=get_test_http_headers()
        )
    print(response.status_code)
    print(response.text)