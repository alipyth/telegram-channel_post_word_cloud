import re
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import arabic_reshaper
import os

texts = []
# بارگذاری فایل‌های HTML
html_files_dir = "./"  # مسیر پوشه فایل‌های HTML را جایگزین کنید

for file in os.listdir(html_files_dir):
    if file.endswith(".html"):
        html_file_path = os.path.join(html_files_dir, file)
        with open(html_file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        # استخراج تمام متن‌ها از div با کلاس "text"
        texts.extend([div.get_text(strip=True) for div in soup.find_all("div", class_="text")])

# ترکیب همه متن‌ها در یک رشته
combined_text = " ".join(texts)

# حذف کاراکترهای غیرمجاز (فقط حروف فارسی و اعداد مجاز)
cleaned_text = re.sub(r"[^آ-ی۰-۹a-zA-Z ]", " ", combined_text)

# بازسازی و معکوس‌کردن متن فارسی
reshaped_text = arabic_reshaper.reshape(cleaned_text)  # بازسازی
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
).generate(reshaped_text)

# نمایش ابر کلمات
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
