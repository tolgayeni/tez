import cv2
import numpy as np
import time

from numpy.typing import _128Bit
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
lower_red = np.array([160, 100, 100])
upper_red = np.array([179, 255, 255])
lower_green = np.array([30,150,100])
upper_green = np.array([60,255,255])
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
xk=0
yk=0
xk_medium=0
yk_medium=0
wk=0
hk=0
xm=0
ym=0
xm_medium=0
ym_medium=0
wm=0
hm=0
xkkontrol=-10
ykkontrol=-10
xmkontrol=-10
ymkontrol=-10
kirmiziislem=0
maviislem=0
###robotkonumx=int(input("Robotun x konumunu pixel olarak giriniz"))
#robotkonumy=int(input("Robotun y konumunu pixel olarak giriniz"))
#xbyk=int(input("Kameranin genisligini (x acisindan buyuklugunu) giriniz Orn: 20 cm'lik bir x ekseninde goruse sahip"))
#xpixel=int(input("Kameranin x eksenindeki pixel sayisini giriniz eger bilmiyorsaniz sik kullanilan deger olan 480i giriniz"))
#ybyk=int(input("Kameranin genisligini (y acisindan buyuklugunu) giriniz Orn: 20 cm'lik bir y ekseninde goruse sahip"))
#ypixel=int(input("Kameranin y eksenindeki pixel sayisini giriniz eger bilmiyorsaniz sik kullanilan deger olan 600u giriniz"))
#xpixeluzun=xbyk/xpixel
###ypixeluzun=ybyk/ypixel###
while True:
    #time.sleep(0.1)
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    frame_blur=cv2.GaussianBlur(frame, (7,7),1)
    hsv_frame=cv2.cvtColor(frame_blur,cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv_frame,lower_red,upper_red)
    contours, _= cv2.findContours(red_mask, cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    deneme=0
    for cnt in contours:
        (xk, yk, wk, hk) = cv2.boundingRect(cnt)
        (a,b)=cv2.minEnclosingCircle(cnt)
        xk_medium = int((xk + xk + wk) / 2)
        yk_medium = int((yk + yk + hk) / 2)
        
        if cv2.contourArea(cnt)<350:
            continue
        else:
            #print(cnt)
            print("bitti kirmizi")
            cv2.rectangle(frame, (xk, yk), (xk+wk, yk+hk), (255, 255, 0), 2)
            
            c=int(a[0])
            d=int(a[1])
            f=int(b)
            #cv2.circle(frame,(c,d),f,(255,0,0),1)
            print(cv2.contourArea(cnt),"cnt area")
            print(len(contours))
            print(deneme,". contour")
            deneme=deneme+1
            fk=wk*hk
            print(fk,"carpim",cv2.contourArea(cnt),"cnt area")
    """
    cv2.line(frame, (xk_medium, 0), (xk_medium, 480), (0, 0, 255), 2)
    cv2.line(frame, (0,yk_medium), (590, yk_medium), (0, 0, 255), 2)
    blue_mask=cv2.inRange(hsv_frame,lower_blue,upper_blue)
    contours, _= cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda z:cv2.contourArea(z), reverse=True)
    """
    """
    for cnt in contours:
        (xm, ym, wm, hm) = cv2.boundingRect(cnt)        
        xm_medium = int((xm + xm + wm) / 2)
        ym_medium = int((ym + ym + hm) / 2)
        break
       
    cv2.line(frame, (xm_medium, 0), (xm_medium, 480), (0, 0, 255), 2)
    cv2.line(frame, (0,ym_medium), (750, ym_medium), (0, 0, 255), 2)
    """
    
    
    cv2.imshow("Frame", frame)    
    print("xk ",xk," yk ",yk,"wk",wk,"hk",hk,"xkkontrol",xkkontrol,"ykkontrol",ykkontrol)
    print("xm ",xm," ym ",ym,"wm",wm,"hm",hm,"xmkontrol",xmkontrol,"ymkontrol",ymkontrol)
    
    
    if abs(xkkontrol-xk)<5 and abs(ykkontrol-yk)<5:
        if yk >420 or yk<60 or xk>540 or 60>xk:
            print("kirmizi cisim kontrol mesafesinde degil")
            xk=0
            yk=0
        else:
            print("kirmizi cisim sabit islem baslayabilir")
            xk=0
            yk=0
            kirmiziislem=1
    else:
        print("krmizi cisim sabit degil sabit olmasi bekleniyor")
        if xk==0 and yk==0:
            print("kirmizi cisim tespit edilemedi")
        else:
            xkkontrol=xk
            ykkontrol=yk




    if abs(xmkontrol-xm)<5 and abs(ymkontrol-yk)<5:
        if ym >420 or ym<60 or xm>540 or 60>xm:
            print("mavi cisim kontrol mesafesinde degil")
            xm=0
            ym=0
        else:
            print("mavi cisim sabit islem baslayabilir")
            xm=0
            ym=0
            maviislem=1
    else:
        print("mavi cisim sabit degil sabit olmasi bekleniyor")
        if xm==0 and ym==0:
            print("mavi cisim tespit edilemedi")
        else:
            xmkontrol=xm
            ymkontrol=ym
    

    if kirmiziislem == 1 :
        print("kirmizi cisim icin islem basladi")
        #mesafex=xk-robotkonumx
        #mesafey=yk-robotkonumy
        #print("robot cisimden x ekseninde ",mesafex," birim uzaklikta")
        #print("robot cisimden y ekseninde ",mesafey," birim uzaklikta")
        #print("robot cisimden uzaklikta",((mesafex**2)+(mesafey**2))**(1/2))
        kirmiziislem=0
    elif maviislem == 1:
        print("navi cisim icin islem basladi")
        #mesafex=xm-robotkonumx
        #mesafey=ym-robotkonumy
        #print("robot cisimden x ekseninde ",mesafex," birim uzaklikta")
        #print("robot cisimden y ekseninde ",mesafey," birim uzaklikta")
        #print("robot cisimden uzaklikta",((mesafex**2)+(mesafey**2))**(1/2))
        maviislem=0
    else:
        print("iki renkteki cisim de kontrol yerinde tespit edilemedi veya sabit durmadigi icin islem baslamadi.")


    cv2.imshow("mask",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()