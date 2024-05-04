# Student Name Identifier

import cv2
import pytesseract

# Carrega a imagem
image = cv2.imread('historico_escolar.jpg')

# Converte a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Usa o Pytesseract para extrair o texto da imagem
text = pytesseract.image_to_string(gray_image)

# Exibe o texto extraído
print("Text extracted from image:")
print(text)
