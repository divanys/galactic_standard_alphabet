import numpy as np
import matplotlib.pyplot as plt

def to_pictures(lst):
    for i, arr in enumerate(lst):
        plt.imshow(arr, cmap='gray_r', interpolation='nearest')
        plt.axis('off')  # Отключить оси координат
        plt.savefig(f'output_image{i}.png', dpi=100, bbox_inches='tight')  # Сохранить изображение
        plt.close()  # Закрыть текущее изображение
