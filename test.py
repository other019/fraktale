from array import *
import png
height=10000
width=10000
tablica=[[0 for x in range (height)] for x in range (width)]

for x in range(0,height):
	for y in range(0,width):
		print 'x:'+str(x)+' y:'+str(y)+' suma:'+str(x*4+y)+ ' mod:'+str((x*4+y)%2)
		if(((x*4+y)+x%2)%2==0):
			tablica[x][y]=255
		if(((x*4+y)+x%2)%2==1):
			tablica[x][y]=0


f=open("fraktal.png","wb")
w=png.Writer(height,width,greyscale=True)
w.write(f,tablica)
f.close()