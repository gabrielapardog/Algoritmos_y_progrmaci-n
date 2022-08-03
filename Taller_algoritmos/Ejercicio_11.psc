Algoritmo Nota_final
	Escribir "Indicame la nota de tu primer parcial"
	Leer n_0
	Escribir "Ahora la nota de tu segundo parcial"
	Leer n_1
	Escribir "Y la nota de tu tercer parcial"
	Leer n_2
	parciales = ((n_0+n_1+n_2)/3)*0.55
	Escribir "¿Cuál fue la nota de tu parcial final?"
	Leer Ex_0
	examenf = Ex_0*0.30
	Escribir "Nota de tu trabajo final"
	Leer work
	trabajof = work*0.15
	Notaf = parciales+examenf+trabajof
	Escribir "Tu nota final es " Notaf
FinAlgoritmo
