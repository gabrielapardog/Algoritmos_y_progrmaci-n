Algoritmo Cambio_de_velocidad
	i = 0
	Escribir "�Cu�l es la distancia entre los dos veh�culos?"
	Leer x
	Mientras i = 0 Hacer
		Escribir "�Cu�l es la velocidad del veh�culo de atr�s?"
		Leer v_0
		Escribir "�Cu�l es la velocidad del veh�culo de adelante?"
		Leer v_1
		Si v_0 < v_1 o v_0 = v_1 Entonces
			Escribir "--> La velocidad del veh�culo de atr�s debe ser mayor y diferente que la del veh�culo de adelante, de otra forma no podr� alcanzarlo"
			Escribir " "
			
		SiNo
			
			i = 1
			
		FinSi
		
	FinMientras
	Tiempo = x/(v_0-v_1)
	Tm = Tiempo*60
	Escribir "El veh�culo de atr�s tardar� " Tm "m en alcanzar al de adelante"
FinAlgoritmo
