import pytest
from Apiframework.common.yaml_util import YamlUtil

# 使用fixture固件，作用于conftest文件，每次会话执行前都执行一遍该方法
@pytest.fixture(scope="session", autouse=True)
def execute_sql():
    YamlUtil().clean_yaml()
