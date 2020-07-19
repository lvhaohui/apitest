import unittest,time
from script.login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
from script.addgoods import AddGoods

#格式化测试套件
suite = unittest.TestSuite()
#把测试类添加到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(AddGoods))
#设置报告生成路径和文件名
report_file = "./report/yuze{}.html".format(time.strftime("%Y%m%d %H%M%S"))
#打开报告
with open(report_file,"wb")as f:
    #实例化HTMLTestRunner对象
    runner = HTMLTestRunner(f,title="接口自动化测试报告",description="宇泽购物流程")
    runner.run(suite)