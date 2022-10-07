import math
import PIL

WIDTH , HEIGHT = 500 , 500
ORIGIN = (WIDTH//2,HEIGHT//2)
num = 10000

list , count = [1,2,3] , 3
print("start")
while count <= num:
 count += 2
 for prime in list[2:math.ceil(math.sqrt(count))] :
  if count%prime == 0 :
   break
 else:
   list.append(count)

def polr2cartsn(polarCoords) :
    # polar : (radius,deg)
    r = polarCoords[0]
    deg = polarCoords[1]
    return (round(r*math.cos(deg)//100)+ORIGIN[0],round(r*math.sin(deg)//100)+ORIGIN[1])