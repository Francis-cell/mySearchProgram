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
            resultTemp = baidus(proxies, key_words).baiduSpider()
            # 2、使用wiki查询
            # resultTemp = wikis(key_words).wikiSpiderUtil()
            # 将数据缓存起来
            d_save.setData(innerKey=key_words, innerValue=resultTemp)
            # result= d_save.reverseDict()
            resultTemp = d_save.withNumDict()
            result = d_save.reverseDict(resultTemp)
            return render_template('myLayoutDesign.html', result=result)


def mains(proxy):
    global d_save
    # 最多保存n条数据
    d_save = Dsave(3)
    global proxies
    proxies = proxy
    app.run(debug=True, host="0.0.0.0")