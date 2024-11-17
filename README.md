# telegram-channel_post_word_cloud
با این پروژه میتونید از پیامهای کانال تلگرام یا چت هاتون خروجی بگیرید و در نهایت یک ابر کلمه از پر تکرار ترین کلمات چت یا کانالتون بسازید 

# تولید ابر کلمات فارسی از فایل HTML

این پروژه برای استخراج متن از فایل HTML، پردازش آن، و تولید ابر کلمات فارسی طراحی شده است. مراحل انجام کار به‌صورت کامل در این راهنما توضیح داده شده است.

---

## پیش‌نیازها

برای اجرای این پروژه، ابتدا نیاز است تا کتابخانه‌های زیر را نصب کنید:

```bash
pip install beautifulsoup4 wordcloud matplotlib arabic-reshaper python-bidi
