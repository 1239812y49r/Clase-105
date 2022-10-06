from turtle import width
import cv2
# Definir el video 
video = cv2.VideoCapture("AnthonyShkrab.mp4")
# Si el video no se puede leer 
if(video.isOpened() == False):
    print("No se pudo reproducir el video ")
# dimensiones 
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
# para ver los fps
fps = int(video.get(cv2.CAP_PROP_FPS))
print(fps)
# Crear un video nuevo 
out = cv2.VideoWriter('Boxing.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))

while(True):
    ret, frame = video.read()
    cv2.imshow("Video", frame)
    out.write(frame)

    if cv2.waitKey(25) == 32:
        break

# liberar out y video 
video.release()
out.release()
cv2.destroyAllWindows()


# intalar la biblioteca cv2 
#pip3 install opencv-python