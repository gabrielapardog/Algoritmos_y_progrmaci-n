Algoritmo Cambio_de_velocidad
	i = 0
	Escribir "¿Cuál es la distancia entre los dos vehículos?"
	Leer x
	Mientras i = 0 Hacer
		Escribir "¿Cuál es la velocidad del vehículo de atrás?"
		Leer v_0
		Escribir "¿Cuál es la velocidad del vehículo de adelante?"
		Leer v_1
		Si v_0 < v_1 o v_0 = v_1 Entonces
			Escribir "--> La velocidad del vehículo de atrás debe ser mayor y diferente que la del vehículo de adelante, de otra forma no podrá alcanzarlo"
			Escribir " "
			
		SiNo
			
			i = 1
			
		FinSi
		
	FinMientras
	Tiempo = x/(v_0-v_1)
	Tm = Tiempo*60
	Escribir "El vehículo de atrás tardará " Tm "m en alcanzar al de adelante"
FinAlgoritmo
