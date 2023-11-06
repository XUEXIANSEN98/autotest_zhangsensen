"""请求方式的封装"""
import requests
from Apiframework.common.yaml_util import YamlUtil


class Request_util:

    sess = requests.session()

    # 通用请求方式
    def all_send_requests(self, method, url, **kwargs):
        res = Request_util.sess.request(method, url, **kwargs)
        return res

# a = Request_util()
# url = YamlUtil().read_test_yaml("url3", "../data/url.yaml")
# res = a.post_api(url, data=YamlUtil().read_test_yaml("url3_data", "../data/url.yaml"))
# print(res)


