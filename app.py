import streamlit as st
import random
import string
from captcha.image import ImageCaptcha
from io import BytesIO
from PIL import Image

# CAPTCHA yaratish funksiyasi
def generate_captcha():
    image_captcha = ImageCaptcha(width=280, height=90)
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    image = image_captcha.generate_image(captcha_text)
    return captcha_text, image

# CAPTCHA tekshirish funksiyasi
def verify_captcha(user_input, actual_captcha):
    return user_input.strip().upper() == actual_captcha

# Interfeys
st.title("CAPTCHA Tekshiruvi")
st.write("Quyidagi CAPTCHA-ni kiriting")

# CAPTCHA yaratish
captcha_text, captcha_image = generate_captcha()
st.image(captcha_image, caption="CAPTCHA matnini kiriting")
captcha_input = st.text_input("CAPTCHA-ni kiriting:")

# CAPTCHA tasdiqlash
if st.button("Tekshirish"):
    if not captcha_input:
        st.warning("Iltimos, CAPTCHA-ni kiriting!")
    elif not verify_captcha(captcha_input, captcha_text):
        st.error("CAPTCHA noto‘g‘ri! Iltimos, qaytadan urinib ko‘ring.")
    else:
        st.success("CAPTCHA to‘g‘ri kiritildi!")
