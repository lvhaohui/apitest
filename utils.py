import unittest,json,logging
from config import InitLog

def assert_api(self,response,status,msg,result):
    self.assertEqual(status,response.status_code)
    self.assertEqual(result,response.json().get("result"))
    self.assertIn(msg,response.json().get("msg"))

def read_data():
    jsonfile = "./data/logincase.json"
    with open (jsonfile,encoding="utf-8")as f:
        listdata = json.load(f)
        data_list = []
        for jsondata in listdata:
            case = jsondata.get("case")
            username = jsondata.get("username")
            password = jsondata.get("password")
            msg = jsondata.get("msg")
            result = jsondata.get("result")
            status = jsondata.get("status")

            data_list.append((case,username,password,msg,result,status))
    return data_list

def read_json_data():
    jsonfile = "./data/addgoods.json"
    with open (jsonfile,encoding="utf-8")as f:
        listdata = json.load(f)
        data_list = []
        for jsondata in listdata:
            case = jsondata.get("case")
            goods_name = jsondata.get("goods_name")
            category_id =  jsondata.get("category_id")
            status = jsondata.get("status")
            result = jsondata.get("result")
            msg = jsondata.get("msg")

            data_list.append((case,goods_name,category_id,status,msg,result))
    return data_list

