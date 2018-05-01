# urllib
# requests
import requests


# 最好使用requests
class HTTP:
    # get方法没有用到self，所以提示使用静态method,使用@staticmethod后可以将函数参数中得self删除
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text()
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''
        # 简化代码得
        if r.status_code != 200:
            return {} if return_json else ''
        else:
            return r.json() if return_json else r.text