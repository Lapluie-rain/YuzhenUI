import time
import unittest
from common import HTMLTestRunner


def report_out(test_dir, report_dir, name_project):
    """
    :param test_dir:    用例路径
    :param report_dir:  报告路径
    :param name_project:    项目名称=>用于报告命名及描述
    :return:
    """

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')        # 加载测试用例
    report_name = report_dir + now + '__' + name_project + '_test_report.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                               title="WebUI Auto Testing Report",
                                               description=(name_project + u"系统自动化功能测试"),
                                               verbosity=2)
        runner.run(discover)
        f.close()

    """
    stream：要操作的文件
    title：测试报告标题
    description：报告描述
    verbosity：报告级别
    """
