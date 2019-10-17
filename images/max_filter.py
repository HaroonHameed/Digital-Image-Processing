import numpy as np
import cv2

def main():
    #reading image
    image = cv2.imread( 'White-Bars.png' , cv2.IMREAD_GRAYSCALE)
    image_out = image.copy()

    #calculating width and height
    H = image.shape[0]
    W = image.shape[1]

    #applying max filter
    for x in np.arange( 3 , H-2):
        for y in np.arange( 3 , W-2):
            max  =  0

            for a in np.arange(-3, 2):
                for b in np.arange(-3, 2):
                    intensity = image.item( x + a, y + b)
                    if intensity > max:
                        max  =  intensity

            res  =  max
            image_out.itemset((x , y ), res)


    #output for the image and display
    cv2.imwrite('output_maxfilter.png', image_out)
    cv2.imshow('image',image_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()