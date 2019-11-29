import cv2,pygame

# vw=cv2.VideoCapture('E:\\SK2017072831-3d animation.avi')
vw=cv2.VideoCapture('video2.avi')
fps = vw.get(cv2.CAP_PROP_FPS)
size = (int(vw.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(vw.get(cv2.CAP_PROP_FRAME_HEIGHT)))
vout=cv2.VideoWriter('jd1.avi',cv2.VideoWriter_fourcc(*'XVID'),fps,size)

def print_frame(n_frame=200):
    vw = cv2.VideoCapture('video2.avi')
    n=0
    while n<n_frame:
        rval, frame = vw.read()
        n+=1
    cv2.imshow('img_%s' % n_frame, frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    vw.release()

def new_film(start=10,end=370):
    c=0
    vw = cv2.VideoCapture('video2.avi')
    while c<=end:  # 循环读取视频帧
        rval, frame = vw.read()
        if (c>=start and c<=end):
            if c%2==0:
                print(c)
                vout.write(frame)
        c = c + 1
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    vw.release()

def add_film(start=400,end=490):
    c = 0
    vw = cv2.VideoCapture('video2.avi')
    while c <= end:  # 循环读取视频帧
        rval, frame = vw.read()
        if c>=start and c<=end:
            print(c)
            vout.write(frame)
        c = c + 1
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    vw.release()

def print_part(n_frame=385,h1=80,h2=850,w1=330,w2=1860):
    vw = cv2.VideoCapture('video2.avi')
    n = 0
    while n < n_frame:
        rval, frame = vw.read()
        n += 1
    frame=frame[h1:h2,w1:w2]
    # cv2.imshow('img_%s' % n_frame, frame)
    # cv2.waitKey(0)
    can=deal_img()
    cv2.imshow('img_%s' % n_frame, can)
    cv2.waitKey(0)
    for i,row in enumerate(can):
        for j ,val in enumerate(row):
            if val==0:
                frame[i][j]=255
    cv2.imshow('img_%s' % n_frame, frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    vw.release()

def deal_img():
    vw = cv2.VideoCapture('video2.avi')
    c=0
    while c<=385:
        rval, frame = vw.read()
        c+=1
    frame=frame[80:850,330:1860]
    can=cv2.Canny(frame,200,300)
    shape = []
    for i, row in enumerate(can):
        min, max = 0, 0
        for j, val in enumerate(row):
            if val != 0 and min == 0:
                min = j - 1
                break
        for j, val in enumerate(row[1400::-1]):
            if val != 0 and max == 0:
                max = 1400 - j
                break
        if i>296 and i<533:
            max=1390
        shape.append([min, max])
    print(shape)
    for i,row in enumerate(can):
        if i<=102:
            for j,val in enumerate(row):
                can[i][j]=0
        if 102<i<212:
            for j, val in enumerate(row):
                if j<=shape[i][0] or j>=shape[i][1]:
                    can[i][j]=0
                else:
                    can[i][j]=255
        if 212<=i<=543:
            for j, val in enumerate(row):
                if j>1417:
                    can[i][j]=255
                else:
                    if j <= shape[i][0] or j >= shape[i][1]:
                        can[i][j] = 0
                    else:
                        can[i][j] = 255
        if i>543 and i<=759:
            for j, val in enumerate(row):
                if j<=shape[i][0] or j>=shape[i][1]:
                    can[i][j]=0
                else:
                    can[i][j]=255
        if i>759:
            for j, val in enumerate(row):
                can[i][j] = 0
    img_out=can
    return img_out

def tran_film():
    c=0
    vw = cv2.VideoCapture('three_12s.avi')
    fps = vw.get(cv2.CAP_PROP_FPS)
    size = (int(vw.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(vw.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(fps,size)
    vout = cv2.VideoWriter('jd2.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (1860-330,850-80))
    while c<=361:  # 循环读取视频帧
        rval, frame = vw.read()
        frame=frame[80:850,330:1860]
        vout.write(frame)
        c = c + 1
        print(c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    vw.release()

def reduce_frame():
    c = 0
    vw = cv2.VideoCapture('three_12s_30.avi')
    fps = vw.get(cv2.CAP_PROP_FPS)
    size = (int(vw.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(vw.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    vout = cv2.VideoWriter('three_12s_15.avi', cv2.VideoWriter_fourcc(*'XVID'), 15, size)
    while c <= 361:  # 循环读取视频帧
        rval, frame = vw.read()
        if c%2==0:
            vout.write(frame)
        c = c + 1
        print(c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    vw.release()


def tran_film_new():
    c = 0
    vw = cv2.VideoCapture('three_12s_30.avi')
    fps = vw.get(cv2.CAP_PROP_FPS)
    size = (int(vw.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(vw.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    vout = cv2.VideoWriter('three_12s_15_new.avi', cv2.VideoWriter_fourcc(*'XVID'), 15, size)
    can=deal_img()
    while c <= 361:  # 循环读取视频帧
        rval, frame = vw.read()
        if c % 2 == 0:
            for i,row in enumerate(can):
                for j,val in enumerate(row):
                    if val==0:
                        frame[i][j]=255
            vout.write(frame)
        c = c + 1
        print(c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    vw.release()



if __name__=='__main__':
    # print_frame(385)
    # new_film(25,385)
    # add_film(400,490)
    # add_film(580, 670)
    print_part(385,80,850,330,1860)
    # tran_film()
    # reduce_frame()
    # tran_film_new()
