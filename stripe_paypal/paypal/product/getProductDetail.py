# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 14:39

import stripe
from paypal.authorization import *

if __name__ == '__main__':

    # https://docs.stripe.com/api/products/retrieve
    stripe.api_key = get_test_apiKey()
    product=stripe.Product.retrieve("prod_LNn19OZ7dXj6ra")
    print(product)

