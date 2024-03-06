import base64
import json
import requests
from paypal.authorization import get_test_http_headers, get_productId

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/02/27 14:29

if __name__ == '__main__':

    data1 = {
        "product_id": get_productId(),
        "name": "Paypal测试环境周付6.0/服务器配置无免费试用",
        "description": "Paypal测试环境周付6.0/服务器配置无免费试用",
        "status": "ACTIVE",
        "billing_cycles": [
            {
                "frequency": {
                    "interval_unit": "DAY",
                    "interval_count": 1
                },
                "tenure_type": "REGULAR",
                "sequence": 1,
                "total_cycles": 0,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "6.0",
                        "currency_code": "USD"
                    }
                }
            }
        ],
        "payment_preferences": {
            "auto_bill_outstanding": True,
            "setup_fee_failure_action": "CONTINUE",
            "payment_failure_threshold": 3
        }
    }

    response = requests.post('https://api-m.sandbox.paypal.com/v1/billing/plans', headers=get_test_http_headers(), data=json.dumps(data1))
    print(response.status_code)
    print(response.text)

    # {"id":"P-93D29984R6424570HMXSZAXQ","product_id":get_productId(),"name":"Paypal测试环境周付9.99/服务器配置1天免费试用","status":"ACTIVE","description":"Paypal测试环境周付9.99/服务器配置1天免费试用","usage_type":"LICENSED","create_time":"2024-03-04T09:11:58Z","links":[{"href":"https://api.sandbox.paypal.com/v1/billing/plans/P-93D29984R6424570HMXSZAXQ","rel":"self","method":"GET","encType":"application/json"},{"href":"https://api.sandbox.paypal.com/v1/billing/plans/P-93D29984R6424570HMXSZAXQ","rel":"edit","method":"PATCH","encType":"application/json"},{"href":"https://api.sandbox.paypal.com/v1/billing/plans/P-93D29984R6424570HMXSZAXQ/deactivate","rel":"self","method":"POST","encType":"application/json"}]}

    # {"id":"P-9JU57009UP429752MMXTP3YA","product_id":"PROD-3A2390258F673684H","name":"Paypal测试环境周付6.0/服务器配置无免费试用","status":"ACTIVE","description":"Paypal测试环境周付6.0/服务器配置无免费试用","usage_type":"LICENSED","create_time":"2024-03-05T11:11:28Z","links":[{"href":"https://api.sandbox.paypal.com/v1/billing/plans/P-9JU57009UP429752MMXTP3YA","rel":"self","method":"GET","encType":"application/json"},{"href":"https://api.sandbox.paypal.com/v1/billing/plans/P-9JU57009UP429752MMXTP3YA","rel":"edit","method":"PATCH","encType":"application/json"},{"href":"https://api.sandbox.paypal.com/v1/billing/plans/P-9JU57009UP429752MMXTP3YA/deactivate","rel":"self","method":"POST","encType":"application/json"}]}
