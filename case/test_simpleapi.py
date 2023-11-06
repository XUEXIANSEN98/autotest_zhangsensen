import pytest
from Apiframework.common.yaml_util import YamlUtil
from Apiframework.common.request_util import Request_util


class Test_simpleapi:

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_yaml("D:\sublime text3\webapitest_windows\Apiframework\data\simple_data.yaml"))
    def test_one(self, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        data = caseinfo["request"]["data"]
        res_expect = caseinfo["request"]["except"]
        res = Request_util().all_send_requests(method=method, url=url, data=data)
        assert res_expect in res.json()




