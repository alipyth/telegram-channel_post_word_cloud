import re
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import arabic_reshaper
import os

combined_text = ""
# بارگذاری فایل‌های HTML
html_files_dir = "./"  # مسیر پوشه فایل‌های HTML را جایگزین کنید

ls = os.listdir(html_files_dir)
#در صورت موجود بودن allText.txt در مسیر گفته شده، از متن داخل این فایل استفاده می‌شود.
if "allText.txt" in ls: 
    combined_text = open('allText.txt', 'r', encoding='utf-8').read() #خواندن فایل کلمات ذخیره شده
else:
    texts = []
    for file in ls:
        if file.endswith(".html"):
            html_file_path = os.path.join(html_files_dir, file)
            with open(html_file_path, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")

            # استخراج تمام متن‌ها از div با کلاس "text"
            texts.extend([div.get_text(strip=True) for div in soup.find_all("div", class_="text")])

    # ترکیب همه متن‌ها در یک رشته
    combined_text = " ".join(texts)

# حذف کاراکترهای غیرمجاز (فقط حروف فارسی)
cleaned_text = re.sub("[^آ-ی ]", " ", combined_text)

words = {}
listText = cleaned_text.split() #شمارش تکرار هر کلمه
for word in listText:
    if word in words: words[word] += 1
    else: words[word] = 1
    
sorted_dict = dict(sorted(words.items(), key=lambda item: item[1], reverse=True)) #مرتب سازی دیکشنری
keys = list(sorted_dict.keys())
for i in range(min(len(keys), 100)): #نمایش 100 کلمه اول از نظر تعداد
    print(f"{keys[i]} : {sorted_dict[keys[i]]}")

# بازسازی و معکوس‌کردن متن فارسی
reshaped_text = arabic_reshaper.reshape(cleaned_text)  # بازسازی

# تولید ابر کلمات
wordcloud = WordCloud(
    font_path="IRANSans_Bold.ttf",  # مسیر فونت فارسی
    width=800,
    height=400,
    background_color="white",
    max_words=100,
    min_word_length=4,
    repeat=False
).generate(reshaped_text)

# نمایش ابر کلمات
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
