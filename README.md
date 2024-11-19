# telegram-channel_post_word_cloud
با این پروژه میتونید از پیامهای کانال تلگرام یا چت هاتون خروجی بگیرید و در نهایت یک ابر کلمه از پر تکرار ترین کلمات چت یا کانالتون بسازید 

# تولید ابر کلمات فارسی از فایل HTML

این پروژه برای استخراج متن از فایل HTML، پردازش آن، و تولید ابر کلمات فارسی طراحی شده است. مراحل انجام کار به‌صورت کامل در این راهنما توضیح داده شده است.

---

## پیش‌نیازها

برای اجرای این پروژه، نیاز است تا کتابخانه‌های زیر را نصب کنید:

```bash
pip install beautifulsoup4 wordcloud matplotlib arabic-reshaper
```
## مراحل
1. با استفاده از تلگرام دسکتاپ، از چت مورد نظر، یک خروجی بگیرید (استفاده از Export chat history). پیشنهاد می‌شود انتخاب تمام گزینه‌ها را بردارید تا روند خروجی گرفتن سریعتر شود.
2. فایل main.py و فونت (IRANSans_Bold.ttf) را در پوشه‌ی چت خروجی گرفته شده بگذارید (معمولا به صورت ChatExport_yyyy-mm-dd است) و سپس فایل main را اجرا کنید و منتظر بمانید تا ابر کلمات درست شود.
(همچنین می‌توانید مقدار متغیر html_files_dir را برابر مسیر پوشه چت خروجی گرفته شده بگذراید)
---
این پروژه ابتدا یک فایل به نام allText.txt از چت مورد نظر ساخته و آن را ذخیره کرده و سپس ابر را نمایش می‌دهد. همچنین اگر در مسیر گفته شده، فایل allText.txt موجود باشد، از متن داخل این فایل استفاده کرده و فایل‌های html را بررسی نخواهد کرد.
