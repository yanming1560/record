import cv2,numpy as np
from PIL import ImageGrab

fps=30
size=ImageGrab.grab().size
print(size)
vout=cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'XVID'),fps,size)

c=1

while(c<=200):
    screen=np.array(ImageGrab.grab())
    # print(screen.shape,screen.size)
    # break
    # cv2.imshow("window", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    # if cv2.waitKey(25) & 0xFF == ord("q"):
    #     cv2.destroyAllWindows()
    #     break
    vout.write(cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    c+=1
    print(c)
vout.release()
cv2.destroyAllWindows()
