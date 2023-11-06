import json
import pytest
from Apiframework.common.yaml_util import YamlUtil
from Apiframework.common.request_util import Request_util
from Apiframework.common.check_json import check_field


class Test_tokenapi:

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_yaml(
        "D:/sublime text3/webapitest_windows/Apiframework/data/token_data.yaml"))
    def test_token(self, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        params = caseinfo["request"]["params"]
        res = Request_util().all_send_requests(method=method, url=url, params=params)
        result = res.json()
        dic = {"access_token":result["access_token"]}
        YamlUtil().write_yaml(dic)

        res_except = caseinfo["request"]["except"]
        assert res_except in res.json()

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_yaml(
        "D:\sublime text3\webapitest_windows\Apiframework\data\Querymenu_data.yaml"))
    def test_querymenu(self, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"] + YamlUtil().read_yaml_value("access_token")
        res = Request_util().all_send_requests(method=method, url=url)

        res_except = caseinfo["request"]["except"]
        assert res_except in res.json()

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_yaml(
        "D:/sublime text3/webapitest_windows/Apiframework/data/tag_data.yaml"))
    def test_create_tag(self, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"] + YamlUtil().read_yaml_value("access_token")
        data = json.dumps(caseinfo["request"]["data"])
        res = Request_util().all_send_requests(method=method, url=url, data=data)
        res_except = caseinfo["request"]["except"]

        error = caseinfo["request"]["error_code"]
        error_value = check_field(error, res.json())

        if error_value:
            print("创建tag失败，失败错误码为：" + str(res.json()['errcode']))
        else:
            assert res_except in res.json()


