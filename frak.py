# -*- coding: utf-8 -*-
from array import *
import time
import png
#zmienne rysowania

width=128 #szerokość w pikselach
height=128 #wysokość w pikselach
x=4 #długość układu współrzędnych w osi x
y=4 #długość układu współrzędnych w osi y
niter=10 #liczba iteracji 


#tablica=[[0 for x in range (height+1)] for x in range (width+1)]
#tablica=[[0 for x in range (255)] for x in range (255)]
tablica=[[0 for x in range (height)] for x in range (width)]

unitx=float()
unity=float()

unitx=float(float(x)/float(width)) #obliczamy ile ma jednostka w poziomie
unity=float(float(y)/float(height)) #obliczamy ile ma jednostka w pionie


##--DBG--##
#print "unitx"+str(unitx)+" unity"+str(unity)
#print "x"+str(x)+" y"+str(y)
#print "height"+str(height)+" width"+str(width)
#time.sleep(1)


tablica=array('b')#tworzymy tablice 
#powinien byc rzadek i tablica tablic?

REs=int()#stara część rzeczywista
IMs=int()#stara część urojona
REn=int()#nowa część rzeczywista
IMn=int()#nowa część urojona
REp=int()#część rzeczywista punktu
IMp=int()#część urojona punktu

for i in range(0,height): #przesuwamy sie w pionie
	for j in range(0,width): #przesuwamy sie w poziomie
		REs=0	
		IMs=0	
		REn=0	
		IMn=0
		REp=i*unity
		IMp=j*unitx	

		##--DBG--##
		#print "j:"+str(j)+" i:"+str(i)
		#print "unitx"+str(unitx)+" unity"+str(unity)

		n2=0
		for n in range(0,niter): #wykonujemy kolejne iteracje
			#kwadracimy liczbę zespoloną
			REn=REs**2+IMs**2
			IMn=2*REs*IMs
			REn+=REp
			IMn+=IMp
			n2+=1
			#sprawdzamy czy moduł mniejszy od 2 (4 zeby nie pierwiastkować niepotrzebnie)
			
			##--DBG--##
			#print "RE:"+str(REp)+" IM:"+str(IMp)


			if(REn**2+IMn**2>4):
				break;
		tablica[j][i]=n2
		##--DBG--##
		#print "i"+str(i)+" j"+str(j)		
#print (tablica)
f=open("fraktal.png","wb")
w=png.Writer(width,height,greyscale=True)
w.write(f,tablica)
f.close()