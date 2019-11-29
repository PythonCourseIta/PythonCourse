def main():

	# Sintassi
	lista = [1, 2, 3, 4, "python", "course", [1, 2, 3, 4, "python", "course"]]

	# Le stringhe sono stringhe indipendentemente da quello che contengono. 
	# Tutto quello che è contenuto all'interno dei doppi apici iniziali è una stringa.
	s = "[1, 2, 3, 4, 'python', 'course', [1, 2, 3, 4, 'python', 'course']]"
	print(lista)

	# Grande differenza tra liste e stringhe è il numero ed il tipo di built-in methods che 
	# mettono a disposizione.
	print(dir(list))
	print(dir(str))

	# Possiblità di creare liste non ordinate
	lista = [4, 1, 3, 2]

	# Possibilità di fare indexing
	print(lista[3]) # 2
	print(lista[-1]) # 2
	print(lista[-4]) # 4

	# Possibilità di fare slicing
	print(lista[:-1]) # [4, 1, 3]
	print(lista[1:]) # [1, 3, 2]
	print(lista[1:-1]) # [1, 3]

	# Possibilità di estendere le liste
	lista = lista + [5, 6, 7, 8]
	print(lista)

	# Possibilità di eseguire dei cicli for sulle liste
	for x in lista:
		if x % 2 != 0:
			print("{} è dispari".format(x))
		else:
			print("{} è pari".format(x))

	print("FOR LOOP\n")

	# Possibilità di eseguire dei cicli while sulle liste
	count = 0
	while count < len(lista):
		if lista[count] % 2 != 0:
			print("{} è dispari".format(lista[count]))
		else:
			print("{} è pari".format(lista[count]))
		count += 1

	print("WHILE LOOP")

	return 0

if __name__ == "__main__":
	main()