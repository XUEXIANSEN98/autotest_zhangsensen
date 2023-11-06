import os
import yaml


class YamlUtil:
    # 读
    def read_yaml(self, yaml_path):
        with open(os.path.abspath(yaml_path), encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)   # FullLoader:加载完整的yaml语言
            return value

    # 写入数据
    def write_yaml(self, data):
        with open(os.path.abspath("D:/sublime text3/webapitest_windows/Apiframework/data/token.yaml"), encoding="utf-8", mode="a") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # 清除数据
    def clean_yaml(self):
        with open(os.path.abspath("D:/sublime text3/webapitest_windows/Apiframework/data/token.yaml"), encoding="utf-8", mode="w") as f:
            f.truncate()

    # 读取某个yaml数据值
    def read_yaml_value(self, key):
        with open(os.path.abspath("D:/sublime text3/webapitest_windows/Apiframework/data/token.yaml"), encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]




