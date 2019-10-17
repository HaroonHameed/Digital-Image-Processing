import numpy as np
import cv2
import math

def main():
    #Monotonically increasing new histogram
    def cumulative_histogram( input_hist ):
        new_hist = input_hist.copy()

        for num in np.arange(1, 256):
            new_hist[num] = new_hist[num - 1] + new_hist[num]
        return new_hist


    #Histogram for our image
    def histogram(input_image):
        height = input_image.shape[0]
        width = input_image.shape[1]
        hist = np.zeros((256))
        for x in np.arange(height):
            for y in np.arange(width):
                intensity = input_image.item(x, y)
                hist[intensity] += 1

        return hist

    #reading our image
    image = cv2.imread('pollen_light.tif', cv2.IMREAD_GRAYSCALE)

    #calcuating total size (pixels) of the image
    height = image.shape[0]
    width = image.shape[1]
    total_pixels = width * height

    #And Finally Historgram equlization for better information
    hist = histogram(image)
    histogram_cum = cumulative_histogram(hist)
    for x in np.arange(height):
        for y in np.arange(width):
            intensity = image.item(x,y)
            round = math.floor(histogram_cum[intensity] * 255.0 / total_pixels)
            image.itemset((x,y), round)




    cv2.imwrite('pollen_light_output.tif', image)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()