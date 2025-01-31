import cv2
import numpy as np

def conv2d(image_path, kernel):

    image = cv2.imread(image_path)
    convolved = np.zeros((image.shape[0], image.shape[1])) # generated image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    kernel = np.fliplr(kernel) # flip horizontally
    kernel = np.flipud(kernel) # flip vertically, this could be one-line but it's more readable
    
    # pad the image to prevent out of bound errors

    pad = np.zeros((image.shape[0] + 2, image.shape[1] + 2)) # create padded base first
    pad[1:-1, 1:-1] =  image # locate the image on the base
    
    # this will be like 
    # [0 0 0 0]
    # [0 1 1 1]
    # [0 2 3 4]
    # [0 4 3 2]

    for x in range(image.shape[0]): # rows
        for y in range(image.shape[1]): # columns 
            # sum of products of elements in image overlapping kernel and kernel elements
            convolved[x, y]=(kernel * pad[x: x+3, y: y+3]).sum() 

    return convolved

kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]) # prewitt filter

cv2.imwrite('./lena_prewitt.png', conv2d("lena.png", kernel))