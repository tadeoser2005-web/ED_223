historial = []
historial.append("google.com")
historial.append("facebook.com")
historial.append("instagram.com")

print("Historial",historial)

pagina_actual = historial[2]
print("Pagina actual: ", pagina_actual)
pagina_salida = historial.pop()
print("Sliendo de pagina ", pagina_salida)
print("Historial actualizado: ",historial)