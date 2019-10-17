import numpy as np
import cv2
import math

def main():

    #Monotonically increasing new image_histogram
    def cumulative_image_histogram(image_hist):

        cum_hist = image_hist.copy()

        for num in np.arange(1, 256):
            cum_hist[num] = cum_hist[num - 1] + cum_hist[num]
        return cum_hist

    #Histogram for our image
    def image_histogram(img):

        height = img.shape[0]
        width = img.shape[1]

        image_hist = np.zeros((256))
        for n in np.arange(height):
            for m in np.arange(width):
                a = img.item(n, m)
                image_hist[a] += 1

        return image_hist

    #reading our images
    img = cv2.imread('pollen_low_contrast.tif', cv2.IMREAD_GRAYSCALE)
    img_ref = cv2.imread('pollen_dark.tif', cv2.IMREAD_GRAYSCALE)

    #calcuating total size (pixels) of the image1
    height = img.shape[0]
    width = img.shape[1]
    pixels = width * height

    #calcuating total size (pixels) of the image2
    height_ref = img_ref.shape[0]
    width_ref = img_ref.shape[1]
    pixels_ref = width_ref * height_ref

    #plotting Histogram of image1
    image_hist = image_histogram(img)
    image_hist_ref = image_histogram(img_ref)

    #plotting Histogram of image2
    cum_hist = cumulative_image_histogram(image_hist)
    cum_hist_ref = cumulative_image_histogram(image_hist_ref)

    #finding Probablity of pixels for image 1
    prob_hist = cum_hist / pixels

    #finding Probablity of pixels fixels for image 1
    prob_hist_ref = cum_hist_ref / pixels_ref

    K = 256
    new_values = np.zeros((K))


    #image_histogram matching
    for a in np.arange(K):
        j = K - 1
        while True:
            new_values[a] = j
            j = j - 1
            if j < 0 or prob_hist[a] > prob_hist_ref[j]:
                break

    for x in np.arange(height):
        for y in np.arange(width):
            intensity = img.item(x,y)
            new_intensity = new_values[intensity]
            img.itemset((x , y) , new_intensity)

    cv2.imwrite('images/image_hist_matched.jpg', img)

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()