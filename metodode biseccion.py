# -*- coding: utf-8 -*-

#funcion para polinomios
def poli(x):
    y=pow(x,2)-(3*x)-4
    return(y)
#programa principal
print("este programa encuentra una raiz, por el metodo de biseccion")
xi=float(input('introduce el valor de xi'))
xs=float(input('introduce el valor de xs'))
error=float((input('introduce el error')))
xa=(xi+xs)/2.0 
i=0
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('i','xi','xs','xa','signos','cambio','error'))
while abs(poli(xa))>error:
    i=i+1
    print('{:^10}{:^10.4}{:^10.4}{:^10.4}{:^10}{:^10}{:^10.4}'.format(i,float(xi),float(xs),float(xa),signos, limites,float(poli(xa))))            
    xa=(xi+xs)/2.0
    if poli(xi)*poli(xa)<0:
        xs=xa
        signos="negativo"
        limites='superior'
    else:
        xi=xa
        signos='positivos'
        limites='inferior'
      

print("la raiz es:",xa)        
    
