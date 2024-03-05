import requests
from paypal.authorization import *

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 10:44

if __name__ == '__main__':

    response = requests.get('https://api.paypal.com/v1/notifications/webhooks/2V6117150C271980E', headers=get_prod_http_headers())
    print(response.status_code)
    print(response.text)

