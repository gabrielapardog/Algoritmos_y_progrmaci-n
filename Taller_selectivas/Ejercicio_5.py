#entrada
s=int(input("digite el sueldo base: "))
vrd1=int(input("digite el numero de ventas realizadas por el departamento1: "))
vrd2=int(input("digite el numero de ventas realizadas por el departamento2: "))
vrd3=int(input("digite el numero de ventas realizadas por el departamento3: "))
#caja negra
vt=(vrd1+vrd2+vrd3)
por=(vt*33/100)
if (vrd1>por):
    s1=s+s*0.20
    print("ventas mayor al 33%: ", s1)
else:
    print("venta menor al 33%: ", s)
if (vrd2>por):    
    s2=s+s*0.20
    print("ventas mayor al 33%: ", s2)
else:
    print("venta menor al 33%: ", s)
if (vrd3>por):    
    s3=s+s*0.20
    print("ventas mayor al 33%: ", s3)
else:
    print("venta menor al 33%: ", s)