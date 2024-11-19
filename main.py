import re
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

# بارگذاری فایل HTML
html_file_path = "example.html"  # مسیر فایل HTML را جایگزین کنید

with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# استخراج تمام متن‌ها از div با کلاس "text"
texts = [div.get_text(strip=True) for div in soup.find_all("div", class_="text")]

# ترکیب همه متن‌ها در یک رشته
combined_text = " ".join(texts)

# حذف کاراکترهای غیرمجاز (فقط حروف فارسی و اعداد مجاز)
cleaned_text = re.sub(r"[^آ-ی۰-۹a-zA-Z ]", " ", combined_text)

# بازسازی و معکوس‌کردن متن فارسی
reshaped_text = arabic_reshaper.reshape(cleaned_text)  # بازسازی
bidi_text = get_display(reshaped_text)  # معکوس‌کردن
stopwords_file_path = "persianST.txt"  # مسیر فایل کلمات ایست
with open(stopwords_file_path, "r", encoding="utf-8") as file:
    stop_words = set(file.read().splitlines())  # کلمات را به مجموعه تبدیل می‌کنیم

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


