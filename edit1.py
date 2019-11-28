import cv2,pygame

# vw=cv2.VideoCapture('E:\\SK2017072831-3d animation.avi')
vw=cv2.VideoCapture('111.mp4')
c=1

fps = vw.get(cv2.CAP_PROP_FPS)
size = (int(vw.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(vw.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print(fps,size)


vout=cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,size)

if vw.isOpened():  # 判断是否正常打开
    rval, frame = vw.read()
    # cv2.imshow("a",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("1.jpg",frame)
else:
    rval = False

while rval:  # 循环读取视频帧
    rval, frame = vw.read()

    if (c>=200 and c<=700):
        print(c)
        vout.write(frame)
    c = c + 1
    cv2.waitKey(1)
vw.release()
