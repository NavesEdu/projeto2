import cv2
from matplotlib import pyplot as plt


img = cv2.imread('trabalhoCGI2.png')
# Aplicando o filtro de mediana da biblioteca OpenCV
# que é importada como cv2 e atribuindo a variavel median
# utilizando uma mascara 5x5
median = cv2.medianBlur(img,5)

# Codigo reponsavel por plotar a imagem original e
# o resultado lado a lado a nivel de comparacao
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Mediana')
plt.xticks([]), plt.yticks([])
plt.show()
