import base64
import json
import requests
from paypal.authorization import get_test_http_headers, get_productId

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/02/27 14:29

# https://developer.paypal.com/docs/api/subscriptions/v1/#plans_create
if __name__ == '__main__':

    data1 = {
        "product_id": get_productId(),
        "name": "Paypal测试环境周付9.99/服务器配置3天免费试用",
        "description": "Paypal测试环境周付9.99/服务器配置3天免费试用",
        "status": "ACTIVE",
        "billing_cycles": [
            {
                "frequency": {
                    "interval_unit": "DAY",
                    "interval_count": 3
                },
                "tenure_type": "TRIAL",
                "sequence": 1,
                "total_cycles": 1,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "0",
                        "currency_code": "USD"
                    }
                }
            },
            {
                "frequency": {
                    "interval_unit": "WEEK",
                    "interval_count": 1
                },
                "tenure_type": "REGULAR",
                "sequence": 2,
                "total_cycles": 0,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "9.9",
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

    data2 = {
        "product_id": get_productId(),
        "name": "Paypal测试环境季付29.99/服务器配置3天免费试用",
        "description": "Paypal测试环境季付29.99/服务器配置3天免费试用",
        "status": "ACTIVE",
        "billing_cycles": [
            {
                "frequency": {
                    "interval_unit": "DAY",
                    "interval_count": 3
                },
                "tenure_type": "TRIAL",
                "sequence": 1,
                "total_cycles": 1,
            },
            {
                "frequency": {
                    "interval_unit": "MONTH",
                    "interval_count": 3
                },
                "tenure_type": "REGULAR",
                "sequence": 2,
                "total_cycles": 0,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "29.9",
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

    data3 = {
        "product_id": get_productId(),
        "name": "Paypal测试环境周付7.49/服务器配置3天免费试用",
        "description": "Paypal测试环境周付7.49/服务器配置3天免费试用",
        "status": "ACTIVE",
        "billing_cycles": [
            {
                "frequency": {
                    "interval_unit": "DAY",
                    "interval_count": 3
                },
                "tenure_type": "TRIAL",
                "sequence": 1,
                "total_cycles": 1,
            },
            {
                "frequency": {
                    "interval_unit": "WEEK",
                    "interval_count": 1
                },
                "tenure_type": "REGULAR",
                "sequence": 2,
                "total_cycles": 0,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "7.49",
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

    data4 = {
        "product_id": get_productId(),
        "name": "Paypal测试环境季付22.49/服务器配置3天免费试用",
        "description": "Paypal测试环境季付22.49/服务器配置3天免费试用",
        "status": "ACTIVE",
        "billing_cycles": [
            {
                "frequency": {
                    "interval_unit": "DAY",
                    "interval_count": 3
                },
                "tenure_type": "TRIAL",
                "sequence": 1,
                "total_cycles": 1,
            },
            {
                "frequency": {
                    "interval_unit": "MONTH",
                    "interval_count": 3
                },
                "tenure_type": "REGULAR",
                "sequence": 2,
                "total_cycles": 0,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "22.49",
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
