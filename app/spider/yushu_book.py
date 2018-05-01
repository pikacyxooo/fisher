from app.libs.my_http import HTTP
from flask import current_app


class YuShuBook:
    per_page = 15
    # 两个url，一个是关键字查询url，一个是isbn号查询url
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'

    @classmethod
    def search_by_keyword(cls, keyword, page):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        res = HTTP.get(url)
        # 在python返回json后变成dict类型
        return res

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        res = HTTP.get(url)
        return res

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']



