import unittest,logging,requests
from config import InitLog
from api.login01 import login_api
from parameterized import parameterized
from utils import read_data
from utils import assert_api

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass



    @parameterized.expand(read_data)
    def test_login(self,case,username,password,msg,result,status):
        #logging.info("读取数据：{0},{1},{2},{3},{4},{5}".format(case,username,password,msg,result,status))
        response = login_api(username,password)
        assert_api(self,response,status,msg,result)
        logging.info("{0}:{1}".format(case,response.json()))



