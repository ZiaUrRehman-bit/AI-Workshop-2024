# Description: Sketching the picture using openCV

import  cv2

# get the image location


zayan_img = input("Enter the name of image e.g.(imgname.jgp) : ")

# read image
img = cv2.imread(zayan_img)


hight = img.shape[0]
width = img.shape[1]
print(hight, width)
# get the dimension
dimension = img.shape   # shape returns size of image width and height

# resize img
# img = cv2.resize(img, (int(dimension[0]/3), int(dimension[1]/4.5)))

# convert to grayscaled
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# invert the image
inverted_grayscaled_img = 255 - grayscaled_img

# blur the image using gaussian function
blured_img = cv2.GaussianBlur(inverted_grayscaled_img, (21, 21), 0)

# invert the blurd image
inverted_blurd_img = 255 - blured_img

# create the pencil sketch
pencil_blurd_img = cv2.divide(grayscaled_img, inverted_blurd_img, scale = 256.0)
pencil_blurd_img = cv2.putText(pencil_blurd_img, "Engr. Zia Ur Rehman", (width-200, hight-50), 1, 1, (0, 0, 0), 2)

# save image
new_img = zayan_img[0] + "new2.jpg"
cv2.imwrite(new_img, pencil_blurd_img)

# show image
cv2.imshow('Zayan Original Image', img)
# cv2.imshow('Zayan Grayscaled Image', grayscaled_img)
# cv2.imshow('Zayan Inverted Image', inverted_grayscaled_img)
# cv2.imshow('Zayan blurd Image', blured_img)
# cv2.imshow('Zayan inverted blurd Image', inverted_blurd_img)
cv2.imshow('Zayan sketch Image', pencil_blurd_img)


cv2.waitKey(0)


cv2.destroyAllWindows()
print("Code Completed!")