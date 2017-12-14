from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

text = open(path.join(d, 'Is.txt')).read()

Is_mask = np.array(Image.open(path.join(d, 'Is3.jpg')))

wc = WordCloud(background_color="white", max_words=3000, mask=Is_mask)
wc.generate(text)

#保存图片
wc.to_file(path.join(d, 'test3.png'))

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(Is_mask, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()