"""检查JSON中是否存在某个字段"""


def check_field(field, data):
    if field in data:
        return True
    else:
        return False
