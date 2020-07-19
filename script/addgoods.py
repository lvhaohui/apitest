import unittest,logging,requests
from api.addgoods01 import addgoods_api
from config import InitLog
from utils import assert_api
from utils import read_json_data
from parameterized import parameterized





class AddGoods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @parameterized.expand(read_json_data)

    def test_addgoods(self,case,goods_name,category_id,status,msg,result):
        response = addgoods_api(goods_name, category_id)
        assert_api(self, response, status, msg, result)
        logging.info("{0}{1}".format(case,response.json()))


