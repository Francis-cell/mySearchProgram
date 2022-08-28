# coding=gbk
# 导入相关模块(词云使用库)
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import jieba
import numpy as np
from PIL import Image

class WordCloudUtils(object):
    def __init__(self, key_words):
        super(WordCloudUtils, self).__init__()
        self.key_words = key_words

    def get_words(self):
        return self.key_words

    def set_words(self, key_words):
        self.key_words = key_words

    '''
    方法说明：生成词云
    '''
    def createCloudWord(self):
        # 设置停用词
        STOPWORDS = {"的", "在", "有", "了", "部分", "被", "如", "它们", "可以", "时", "与", "可", "其", "它", "能", "中",
                     "个", "包括", "是", "和", "而", "或", "某些", "通过", "称为", "也", "等"}

        # 设置背景图片
        img = np.array(Image.open('../pngs/t03.png'))
        # 1、读取文本文件内容
        text_from_file = open("../txts/tempTxt01.txt", encoding='utf-8').read()
        # 通过jieba分词进行分词并通过空格分割
        Word_spilt_jieba = jieba.cut(text_from_file, cut_all=True)
        word_space = ' '.join(Word_spilt_jieba)

        # 配置Wordcloud参数
        my_wordcloud = WordCloud(
            # 设置背景颜色
            background_color='white',
            # 背景图片
            mask=img,
            # 设置最大显示词数
            max_words=300,
            # 设置停用词
            stopwords=STOPWORDS,
            # 设置字体格式(需要支持中文)
            font_path="../fonts/你给我的奶思.ttf",
            # 设置字体最大值
            max_font_size=100,
            # 设置随机生成状态，即多少种配色方案
            random_state=50
        ).generate(word_space)

        # 根据图片生成词云颜色
        image_colors = ImageColorGenerator(img)
        # 设置字体颜色为图片背景颜色
        my_wordcloud.recolor(color_func=image_colors)

        # 保存生成的图片，当关闭图片时才生效，中断程序不会保存
        my_wordcloud.to_file('../pngs/' + self.key_words + '.png')