# Entradas
a = float(input("\nHola cuanto dinero tienes invertido en el banco "))
b = float(input("Cuales son los intereses (%) de tu banco por inversión "))

# Caja negra 
b = b/100
c = a * b
d = c + a 

# Salidas 
print("\nEl dinero de tu cuenta es",d,"\n")  if c > 100000 else print("\nEl dinero de tu cuenta es",a,"\n")