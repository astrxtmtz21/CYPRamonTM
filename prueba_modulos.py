#import modulos
#modulos.mi_print("Hola")

from modulos import *
import time
import sys
from asciistuff import Banner 

mi_print("Hola de nuevo")
otro_print("Otro print usado")
print(sumar(4 , 5))
print(restar(10 , 7))

for i in range (10, 0, -1):
    print( i , "...")
    time.sleep(000000000000000.1)
print(Banner ("WOOOW!!!"))

print(sys.platform)
