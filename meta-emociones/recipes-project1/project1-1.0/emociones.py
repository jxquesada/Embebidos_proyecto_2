import cv2



       
baseline_image=None
status_list=[None,None]
camara= cv2.VideoCapture("video.mp4")

fondo = None
img_c=0;
count=0;
while True:
    (grabbed, frame) = camara.read()
    
    status=0   
    if grabbed == False: break
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gris = cv2.GaussianBlur(gris, (21, 21), 0)
    if fondo is None:
        fondo = gris 
        continue
    resta = cv2.absdiff(fondo, gris)
    umbral = cv2.threshold(resta, 25, 255, cv2.THRESH_BINARY)[1]
    umbral2 = cv2.dilate(umbral, None, iterations=2)
    contornosimg = umbral2.copy()
    contornos, hierarchy = cv2.findContours(contornosimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    
    for c in contornos:
        if cv2.contourArea(c) < 500:
            continue
        status=1
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    status_list.append(status)
    
    if status_list[-1]==1 and status_list[-2]==0:
        img_name="foto_{}.png".format(img_c)
        cv2.imwrite(img_name,frame)
        img_c+=1
    cv2.imshow("Camara", frame)
   # key=cv2.waitKey(1)

    #if key==ord('q'):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()

#detection de movimiento
##https://programarfacil.com/blog/vision-artificial/deteccion-de-movimiento-con-opencv-python/
#Alarma
##https://towardsdatascience.com/build-a-motion-triggered-alarm-in-5-minutes-342fbe3d5396
#capturas
##https://www.youtube.com/watch?v=IhRfqiC29Ds&ab_channel=CodingShiksha
