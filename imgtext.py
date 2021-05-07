import cv2
import pytesseract


img = cv2.imread('/home/skprints/public_html/Captcha/aadharcaptcha.jpeg')

text = pytesseract.image_to_string(img)


print(text.replace(" ",""))
