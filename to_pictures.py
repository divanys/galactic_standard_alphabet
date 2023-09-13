def to_pictures(lst):
    import numpy as np
    import matplotlib.pyplot as plt
    for arr in lst:
        plt.imshow(arr, cmap='gray_r', interpolation='nearest')
        plt.show()
