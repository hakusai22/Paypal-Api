import requests
from paypal.authorization import get_test_http_headers

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 10:44

if __name__ == '__main__':
    # https://developer.paypal.com/api/rest/webhooks/event-names/#subscriptions
    # https://developer.paypal.com/docs/api/webhooks/v1/#webhooks_update
    # 30045293K5481613S
    data = '[{"op": "add", "path": "/event_types", "value": [{"name":"PAYMENT.SALE.COMPLETED","description":"yinpeng","status":"ENABLED"},{"name":"BILLING.SUBSCRIPTION.ACTIVATED","description":"A billing agreement is activated.","status":"ENABLED"},{"name":"BILLING.SUBSCRIPTION.CANCELLED","description":"A billing agreement is canceled.","status":"ENABLED"},{"name":"BILLING.SUBSCRIPTION.CREATED","description":"A billing agreement is created.","status":"ENABLED"},{"name":"BILLING.SUBSCRIPTION.EXPIRED","description":"A billing agreement is expired.","status":"ENABLED"},{"name":"BILLING.SUBSCRIPTION.PAYMENT.FAILED","description":"Subscription payment failure will trigger this webhook event.","status":"ENABLED"},{"name":"BILLING.SUBSCRIPTION.RE-ACTIVATED","description":"A billing agreement is re-activated.","status":"ENABLED"},{"name":"BILLING.SUBSCRIPTION.SUSPENDED","description":"A billing agreement is suspended.","status":"ENABLED"},{"name":"BILLING.SUBSCRIPTION.UPDATED","description":"A billing agreement is updated.","status":"ENABLED"}]}]'

    response = requests.patch('https://api-m.sandbox.paypal.com/v1/notifications/webhooks/30045293K5481613S', headers=get_test_http_headers(), data=data)
    print(response.status_code)
    print(response.text)

