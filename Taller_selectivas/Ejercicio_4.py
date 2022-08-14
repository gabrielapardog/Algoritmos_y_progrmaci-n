# Entradas 
a = float(input("\nDime el valor total de la compra "))

# Caja negra 
if a > 5000000:
    b = float(a*.55)
    c = float(a*.25)
    e = float(a*.30)
    d = float(c*.20)
else:
    b = float(a*.70)
    c = float(a*.30)
    d = float(c*.20)
    e = 0

# Salida 
print(f"\nLos fondos utilizados de la empresa son: {b} \nEl credito al fabricante es de: {c} \nPor intereses del fabricante tenemos {d}\nEl prestamo del banco es: {e}\n")