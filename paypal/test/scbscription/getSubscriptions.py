import base64
import json
import time

import requests
from paypal.authorization import get_test_http_headers


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/04 14:00

# https://developer.paypal.com/docs/api/subscriptions/v1/#subscriptions_get
if __name__ == '__main__':

    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-3E4DKBFF6MJS', headers=get_test_http_headers())
    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-A23XPN7GR5CG', headers=get_test_http_headers())
    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-UKV9W1WHAM0R', headers=get_test_http_headers())
    # 试用1天
    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-2C2VHYYUKEUD', headers=get_test_http_headers())
    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-M1JD5XEPE5FU', headers=get_test_http_headers())

    # 直接6.0付费 一天一续费
    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-KU7CK28UPP1H', headers=get_test_http_headers())
    #response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-RSL4P9XXS9GB', headers=get_test_http_headers())
    response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-115LRNB7KLY4', headers=get_test_http_headers())
    print(response.status_code)
    print(response.text)

    # 免费试用状态
    # {"status":"ACTIVE","status_update_time":"2024-03-04T09:23:04Z","id":"I-2C2VHYYUKEUD","plan_id":"P-93D29984R6424570HMXSZAXQ","start_time":"2024-03-04T09:20:35Z","quantity":"1","shipping_amount":{"currency_code":"USD","value":"0.0"},"subscriber":{"email_address":"gaoyanfeng@personal.example.com","payer_id":"P7SGLRUSEQN2S","name":{"given_name":"John","surname":"Doe"},"shipping_address":{"name":{"full_name":"yinpeng123"},"address":{"address_line_1":"2211 N First Street","address_line_2":"Building 17","admin_area_2":"San Jose","admin_area_1":"CN","postal_code":"95131","country_code":"US"}}},"billing_info":{"outstanding_balance":{"currency_code":"USD","value":"0.0"},"cycle_executions":[{"tenure_type":"TRIAL","sequence":1,"cycles_completed":1,"cycles_remaining":0,"current_pricing_scheme_version":1,"total_cycles":1},{"tenure_type":"REGULAR","sequence":2,"cycles_completed":0,"cycles_remaining":0,"current_pricing_scheme_version":1,"total_cycles":0}],"next_billing_time":"2024-03-05T10:00:00Z","failed_payments_count":0},"create_time":"2024-03-04T09:23:04Z","update_time":"2024-03-04T09:23:04Z","plan_overridden":false,"links":[{"href":"https://api.sandbox.paypal.com/v1/billing/subscriptions/I-2C2VHYYUKEUD/cancel","rel":"cancel","method":"POST"},{"href":"https://api.sandbox.paypal.com/v1/billing/subscriptions/I-2C2VHYYUKEUD","rel":"edit","method":"PATCH"},{"href":"https://api.sandbox.paypal.com/v1/billing/subscriptions/I-2C2VHYYUKEUD","rel":"self","method":"GET"},{"href":"https://api.sandbox.paypal.com/v1/billing/subscriptions/I-2C2VHYYUKEUD/suspend","rel":"suspend","method":"POST"},{"href":"https://api.sandbox.paypal.com/v1/billing/subscriptions/I-2C2VHYYUKEUD/capture","rel":"capture","method":"POST"}]}
    # 免费试用后第一次付款状态
