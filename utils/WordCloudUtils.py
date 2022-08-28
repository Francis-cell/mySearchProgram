# coding=gbk
# �������ģ��(����ʹ�ÿ�)
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
    ����˵�������ɴ���
    '''
    def createCloudWord(self):
        # ����ͣ�ô�
        STOPWORDS = {"��", "��", "��", "��", "����", "��", "��", "����", "����", "ʱ", "��", "��", "��", "��", "��", "��",
                     "��", "����", "��", "��", "��", "��", "ĳЩ", "ͨ��", "��Ϊ", "Ҳ", "��"}

        # ���ñ���ͼƬ
        img = np.array(Image.open('../pngs/t03.png'))
        # 1����ȡ�ı��ļ�����
        text_from_file = open("../txts/tempTxt01.txt", encoding='utf-8').read()
        # ͨ��jieba�ִʽ��зִʲ�ͨ���ո�ָ�
        Word_spilt_jieba = jieba.cut(text_from_file, cut_all=True)
        word_space = ' '.join(Word_spilt_jieba)

        # ����Wordcloud����
        my_wordcloud = WordCloud(
            # ���ñ�����ɫ
            background_color='white',
            # ����ͼƬ
            mask=img,
            # ���������ʾ����
            max_words=300,
            # ����ͣ�ô�
            stopwords=STOPWORDS,
            # ���������ʽ(��Ҫ֧������)
            font_path="../fonts/����ҵ���˼.ttf",
            # �����������ֵ
            max_font_size=100,
            # �����������״̬������������ɫ����
            random_state=50
        ).generate(word_space)

        # ����ͼƬ���ɴ�����ɫ
        image_colors = ImageColorGenerator(img)
        # ����������ɫΪͼƬ������ɫ
        my_wordcloud.recolor(color_func=image_colors)

        # �������ɵ�ͼƬ�����ر�ͼƬʱ����Ч���жϳ��򲻻ᱣ��
        my_wordcloud.to_file('../pngs/' + self.key_words + '.png')