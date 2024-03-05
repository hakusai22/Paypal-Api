import base64
import json
import requests
from paypal.authorization import get_test_http_headers


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/04 14:00

# https://developer.paypal.com/docs/api/subscriptions/v1/#subscriptions_create
if __name__ == '__main__':

    data = {
        # 免费试用3天
        #"plan_id": "P-51J87956H28500615MXSWO7I",
        # 直接付费
        #"plan_id": "P-1J535022XM050613GMXSX2TY",
        # 免费试用1天
        "plan_id": "P-93D29984R6424570HMXSZAXQ",
        "quantity": "1",
        "subscriber": {
            "name": {
                "given_name": "yinpeng1",
                "surname": "yinpeng2"
            },
            "email_address": "yinpeng@lollitech.com",
            "shipping_address": {
                "name": {
                    "full_name": "yinpeng123"
                },
                "address": {
                    "address_line_1": "2211 N First Street",
                    "address_line_2": "Building 17",
                    "admin_area_2": "San Jose",
                    "admin_area_1": "CN",
                    "postal_code": "95131",
                    "country_code": "US"
                }
            }
        },
        "application_context": {
            "brand_name": "walmart",
            "locale": "en-US",
            "shipping_preference": "SET_PROVIDED_ADDRESS",
            "user_action": "SUBSCRIBE_NOW",
            "payment_method": {
                "payer_selected": "PAYPAL",
                "payee_preferred": "IMMEDIATE_PAYMENT_REQUIRED"
            },
            "return_url": "https://example.com/returnUrl",
            "cancel_url": "https://example.com/cancelUrl"
        }
    }

    print(json.dumps(data))
    response = requests.post('https://api-m.sandbox.paypal.com/v1/billing/subscriptions', headers=get_test_http_headers(), data=json.dumps(data))
    print(response.status_code)
    print(response.text)

# 免费试用9.9
# {"status":"APPROVAL_PENDING","id":"I-M1JD5XEPE5FU","create_time":"2024-03-04T06:20:40Z","links":[{"href":"https://www.sandbox.paypal.com/webapps/billing/subscriptions?ba_token=BA-5WH765411T940525E","rel":"approve","method":"GET"},{"href":"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-M1JD5XEPE5FU","rel":"edit","method":"PATCH"},{"href":"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-M1JD5XEPE5FU","rel":"self","method":"GET"}]}

# 免费试用9.9
# {"status":"APPROVAL_PENDING","id":"I-3E4DKBFF6MJS","create_time":"2024-03-04T06:45:00Z","links":[{"href":"https://www.sandbox.paypal.com/webapps/billing/subscriptions?ba_token=BA-6GH318450X148254E","rel":"approve","method":"GET"},{"href":"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-3E4DKBFF6MJS","rel":"edit","method":"PATCH"},{"href":"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-3E4DKBFF6MJS","rel":"self","method":"GET"}]}

# 直接付费9.9
# {"status":"APPROVAL_PENDING","id":"I-UKV9W1WHAM0R","create_time":"2024-03-04T07:51:25Z","links":[{"href":"https://www.sandbox.paypal.com/webapps/billing/subscriptions?ba_token=BA-2VA59456S0448474G","rel":"approve","method":"GET"},{"href":"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-UKV9W1WHAM0R","rel":"edit","method":"PATCH"},{"href":"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-UKV9W1WHAM0R","rel":"self","method":"GET"}]}

# 免费试用1天 9.9
# {"status":"APPROVAL_PENDING","id":"I-2C2VHYYUKEUD","create_time":"2024-03-04T09:20:35Z","links":[{"href":"https://www.sandbox.paypal.com/webapps/billing/subscriptions?ba_token=BA-0L899469X45215113","rel":"approve","method":"GET"},{"href":"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-2C2VHYYUKEUD","rel":"edit","method":"PATCH"},{"href":"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-2C2VHYYUKEUD","rel":"self","method":"GET"}]}
