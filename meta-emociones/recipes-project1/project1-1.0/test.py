import cv2
print("nombre de la imagen:")
imgname=str(input())
img = cv2.imread(imgname,1)
cv2.imshow(imgname ,img)
cv2.waitKey()
cv2.destroyAllWindows()
