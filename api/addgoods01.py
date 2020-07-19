import unittest,requests,logging
#from api.login01 import session


def addgoods_api(goods_name,category_id):
    url = "http://192.168.1.160:5000/addgoods"
    data = {
            "goods_name": goods_name,
            "category_id": category_id,
            "main_image": "dfsfsfsafs",
            "price": "1680",
            "quantity": 999,
            "detail": "dffdsfsfsf",
            "status": 1,
           }
    headers = {"Content_Type": "appliction/json"}


    r = requests.post(url, json=data, headers=headers)
    return r