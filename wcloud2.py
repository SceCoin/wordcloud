from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#获得当前目录
d = path.dirname(__file__)

#读取文件
text = open(path.join(d, 'Is.txt')).read()

#读取mask
Is_coloring = np.array(Image.open(path.join(d, 'Is2.png')))

#设置停用词 ? 读取的文章篇幅太长时使用
# stopwords = set(STOPWORDS)
# stopwords.add('said')

wc = WordCloud(background_color="white", max_words=2000, mask=Is_coloring,
                 max_font_size=40, random_state=42)
#分词
wc.generate(text)

#颜色来自图片本身
image_colors = ImageColorGenerator(Is_coloring)

#在只设置mask的情况下, 得到一张图片形状的词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
wc.to_file('test21.png')
#通过构造函数直接给颜色, 通过这种方式可以将按照给定的图片颜色布局生成的策略
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
wc.to_file('test22.png')
# 输出原图
plt.imshow(Is_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()