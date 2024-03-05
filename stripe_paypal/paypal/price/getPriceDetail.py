# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 15:56

if __name__ == '__main__':
    import stripe
    from paypal.authorization import *

    # https://docs.stripe.com/api/prices/create
    stripe.api_key = get_test_apiKey()
    price = stripe.Price.retrieve("price_1Kh1QzL82ItW9euJ4sRwKpTZ")
    print(price)
