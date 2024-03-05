import base64
import json
import requests
from paypal.authorization import *


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 10:51

# https://developer.paypal.com/docs/api/subscriptions/v1/#plans_list
if __name__ == '__main__':

    params = (
        ('product_id', get_prod_productId()),
        ('page_size', '20'),
        ('page', '1'),
        ('total_required', True),
    )
    response = requests.get('https://api.paypal.com/v1/billing/plans', headers=get_prod_http_headers(), params=params)
    print(response.status_code)
    print(response.text)
