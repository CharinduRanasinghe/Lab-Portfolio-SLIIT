import cv2
from PIL import Image

#test_img = cv2.imread('C:\\Users\\chari\\OneDrive\\Documents\\Sliit\\Y3S1\\DIP\\Lab 1\\test.jpg',0)

#cv2.imshow('no color', test_img)
#cv2.imwrite('C:\\Users\\chari\\OneDrive\\Documents\\Sliit\\Y3S1\\DIP\\Lab 1\\grayscale.jpg',test_img)
#cv2.waitKey(0)
#print(test_img.shape)
#print(test_img.size)
image = Image.open('C:\\Users\\chari\\OneDrive\\Documents\\Sliit\\Y3S1\\DIP\\Lab 1\\test.jpg')
image.show()


#cv2.imshow('edited', test_img)     

#cv2.waitKey(0); 