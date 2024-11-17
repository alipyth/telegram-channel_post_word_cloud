import re
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

with open('bb.txt', "r", encoding="utf-8") as file:
    text = file.read()
# حذف کاراکترهای غیرمجاز (فقط حروف فارسی و اعداد مجاز)
cleaned_text = re.sub(r"[^آ-ی۰-۹a-zA-Z ]", " ", text)

# بازسازی و معکوس‌کردن متن فارسی
reshaped_text = arabic_reshaper.reshape(cleaned_text)  # بازسازی
bidi_text = get_display(reshaped_text)  # معکوس‌کردن
stop_words = ["میکنم", "من", "تو" , 'برای' , 'شاید' , 'داره' ,  'حتما' , 'باشه' , 'امشب']

# تولید ابر کلمات
wordcloud = WordCloud(
    font_path="IRANSans_Bold.ttf",  # مسیر فونت فارسی
    width=800,
    height=400,
    background_color="white",
    max_words=80,
    min_word_length=4,
    repeat=False
).generate(bidi_text)

# نمایش ابر کلمات
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


