# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 15:56

if __name__ == '__main__':
    import stripe
    from paypal.authorization import *

    # https://docs.stripe.com/api/prices/create
    stripe.api_key = get_test_apiKey()

    price = stripe.Price.create(
        currency="usd",
        unit_amount=1000,
        product="prod_LNn19OZ7dXj6ra",
        recurring={
            "interval": "week",
            "interval_count": 1,
            "trial_period_days": 1,
            "usage_type": "licensed"
        },
    )
    print(price)
