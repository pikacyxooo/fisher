from flask import jsonify, request

from app.forms.book import SearchForm
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search')
def search():
    """
        q :  普通字符串/isbn
        page
    """
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    # 判断验证是否成功，如果成功返回True,执行接下来的语句
    if form.validate():
        # 获取form中q和page的data,即他的值
        q = form.q.data.strip()
        page = form.page.data
        # 判断q是isbn还是key
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
        # 上面得语句是flask自带的返回json的语句，大概等同于下面的语句
        # return json.dumps(result), 200, {'Content-Type': 'application/json'}
    else:
        return jsonify(form.errors)
