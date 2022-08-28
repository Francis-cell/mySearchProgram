# coding=gbk

from utils.BaiduBaikeSpiderUtils import BaiduBaikeSpiderUtils as baidus
from utils.WikiSpiderUtils import WikiSpiderUtils as wikis
from utils.DataSaveUtils import DataSaveUtils as Dsave
from flask import Flask, render_template, request

app = Flask(__name__, static_folder="./staticFiles", template_folder="./templates")

@app.route("/")
def index():
    # 向模板中传输数据
    return render_template("myLayoutDesign.html")


@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        key_words = request.form["searchContents"]
        if key_words == "":
            return render_template("myLayoutDesign.html")
        else:
            # 1、调用百度查询
            # resultTemp = baidus(proxies, key_words).baiduSpider()
            # 2、使用wiki查询
            resultTemp = wikis(key_words).wikiSpiderUtil()
            # 将数据缓存起来
            d_save.setData(innerKey=key_words, innerValue=resultTemp)
            result = d_save.reverseDict()
            # result = list(tuple(result.items()))
            # print("tempValues的值为：", result)
            # return render_template('myLayoutDesign.html', result=result, key_words=key_words)
            return render_template('myLayoutDesign.html', result=result)


def mains(proxy):
    global d_save
    d_save = Dsave()
    global proxies
    proxies = proxy
    # print("======", proxies)
    app.run(debug=True)