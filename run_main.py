import os
import pytest

if __name__ == '__main__':

    # 生成allure报告的数据源文件，json格式;--clean是每次清空
    pytest.main(["-v", '--alluredir', "C:/Users/v_zhangsen/.jenkins/workspace/zhangsen/results", '--clean-alluredir'])
    # 生成allure报告，此处的--clean是保证在一个目录里重复生成allure报告（不加的话，只能生成一次，为了误操作覆盖）;
    # 此处的-o 是输出报告，./report
    # allure generat + 数据源文件目录 -o + 报告的目录;
    os.system("allure generate C:/Users/v_zhangsen/.jenkins/workspace/zhangsen/results -o C:/Users/v_zhangsen/.jenkins/workspace/zhangsen/report --clean")





#
#
# if __name__ == '__main__':
#     # 生成allure报告的数据源文件，json格式;--clean是每次清空
#     pytest.main(['--alluredir', './results', '--clean-alluredir'])
#     # 生成allure报告，此处的--clean是保证在一个目录里重复生成allure报告（不加的话，只能生成一次，为了误操作覆盖）;
#     # 此处的-o 是输出报告，./report
#     # allure generat + 数据源文件目录 -o + 报告的目录;
#     os.system('allure generate ./results -o ./report --clean')