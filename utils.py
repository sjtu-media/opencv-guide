import numpy as np;
import matplotlib.pyplot as plt

def show_images(rows, cols, images, figsize=(16, 16), titles=[]):
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    for i,title in enumerate(titles):
        if rows > 1:
            axes[0, i].set_title(title)
        else:
            axes[i].set_title(title)
    for i,ax in enumerate(axes.flat):
        if i < len(images): ax.imshow(images[i])

def gray_to_color(image):
    return np.stack([image, image, image], 2)
