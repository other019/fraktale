# -*- coding: utf-8 -*-
from array import *
import time
import png
#zmienne rysowania

przesx=int()
przesy=int()
width=int() #szerokość w pikselach
height=int() #wysokość w pikselach

x=int(raw_input("Podaj wysokosc w ukladzie wsp:"))
y=int(raw_input("Podaj szerokosc w ukladzie wsp:"))
width=int(raw_input("Podaj rozdzielczosc pionowa:"))
height=int(raw_input("Podaj rozdzielczosc pozioma:"))
przesx=float(raw_input("Podaj przesuniecie pionowe:"))
przesy=float(raw_input("Podaj przesuniecie poziome:"))

x=3 #długość układu współrzędnych w osi y
y=3#długość układu współrzędnych w osi x
niter=100 #liczba iteracji 


tablica=[[0 for z in range (height)] for z in range (width)]

unitx=float()
unity=float()

unitx=float(float(x)/float(width)) #obliczamy ile ma jednostka w poziomie
unity=float(float(y)/float(height)) #obliczamy ile ma jednostka w pionie

##--DBG--##
#print "od razu unitx"+str(unitx)+" unity"+str(unity)


REs=int()#stara część rzeczywista
IMs=int()#stara część urojona
REn=int()#nowa część rzeczywista
IMn=int()#nowa część urojona
REp=int()#część rzeczywista punktu
IMp=int()#część urojona punktu


REps=-(x/2)-przesx#tu moze być przesuwanie
IMps=-(y/2)-przesy
IMp=IMps


for i in range(0,height): #przesuwamy sie w pionie
	IMp+=unity
	REp=REps
	for j in range(0,width): #przesuwamy sie w poziomie
		REs=0	
		IMs=0	
		REn=0	
		IMn=0
		REp+=unitx

		##--DBG--##
		#print "j:"+str(j)+" i:"+str(i)
		#print "REp: "+str(REp)+" IMp"+str(IMp)
		#print "unitx"+str(unitx)+" unity"+str(unity)

		n2=-1
		REs=REp
		IMs=IMp
		for n in range(0,niter): #wykonujemy kolejne iteracje
			#kwadracimy liczbę zespoloną
			REn=REs**2-IMs**2
			IMn=2*(REs*IMs)
			REn+=REp
			IMn+=IMp
			REs=REn
			IMs=IMn
			n2+=1
			#sprawdzamy czy moduł mniejszy od 2 (4 zeby nie pierwiastkować niepotrzebnie)
			
			##--DBG--##
			#print "RE:"+str(REn)+" IM:"+str(IMn)+" MOD:"+str(REn**2+IMn**2)
			#print str(n)

			if(REn**2+IMn**2>=4):
				break;
		tablica[j][i]=n2*(255/niter)
		##--DBG--##
		#print "i"+str(i)+" j"+str(j)		
#print (tablica)
f=open("fraktal.png","wb")
w=png.Writer(width,height,greyscale=True)
w.write(f,tablica)
f.close()