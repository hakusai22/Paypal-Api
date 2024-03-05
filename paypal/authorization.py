import base64
import os
import yaml

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/05 10:29

def get_test_http_headers():
    # 设置请求头
    headers = {
        "Content-Type": "application/json"
    }
    # 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    fs = open(os.path.join(curPath, "config.yaml"), encoding="UTF-8")
    datas = yaml.safe_load(fs)
    client_id = datas['test']['client_id']
    secret = datas['test']['secret']
    authorization = client_id + ":" + secret
    auth_encode = base64.b64encode(authorization.encode()).decode()
    final_auth = f"Basic {auth_encode}"
    headers["Authorization"] = final_auth
    return headers

def get_prod_http_headers():
    # 设置请求头
    headers = {
        "Content-Type": "application/json"
    }
    # 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    fs = open(os.path.join(curPath, "config.yaml"), encoding="UTF-8")
    datas = yaml.safe_load(fs)
    client_id = datas['prod']['client_id']
    secret = datas['prod']['secret']
    authorization = client_id + ":" + secret
    auth_encode = base64.b64encode(authorization.encode()).decode()
    final_auth = f"Basic {auth_encode}"
    headers["Authorization"] = final_auth
    return headers

def get_productId():
    curPath = os.path.dirname(os.path.realpath(__file__))
    fs = open(os.path.join(curPath, "config.yaml"), encoding="UTF-8")
    datas = yaml.safe_load(fs)
    product_id = datas['test']['product_id']
    return product_id

def get_prod_productId():
    curPath = os.path.dirname(os.path.realpath(__file__))
    fs = open(os.path.join(curPath, "config.yaml"), encoding="UTF-8")
    datas = yaml.safe_load(fs)
    product_id = datas['prod']['product_id']
    return product_id

def get_test_apiKey():
    curPath = os.path.dirname(os.path.realpath(__file__))
    fs = open(os.path.join(curPath, "config.yaml"), encoding="UTF-8")
    datas = yaml.safe_load(fs)
    api_key = datas['api_key']
    return api_key
