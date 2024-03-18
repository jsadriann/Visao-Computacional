import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Abrir a imagem
filename = sys.argv[1]
im = cv2.imread(filename)

# Converter para o espaço de cores HSV
im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

# Dividir os canais de cor
h, s, v = cv2.split(im_hsv)

# Definir os valores de matiz para azul e verde
BLUE_HUE = [90,109]
GREEN_HUE = [23,68]

# Identificar os pixels azuis e verdes usando máscaras
blue_mask = np.logical_and(h >= BLUE_HUE[0], h <= BLUE_HUE[1])
green_mask = np.logical_and(h >= GREEN_HUE[0], h <= GREEN_HUE[1])

# Trocar os valores de matiz dos pixels azuis e verdes
h[blue_mask] = 47
h[green_mask] = 109

# Combinar os canais de cor novamente
im_hsv_changed = cv2.merge([h, s, v])

# Converter de volta para o espaço de cores BGR
im_changed = cv2.cvtColor(im_hsv_changed, cv2.COLOR_HSV2BGR)

# Exibir as imagens
plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(im_changed, cv2.COLOR_BGR2RGB))
plt.title('Imagem com Troca de Cores')

plt.show()
