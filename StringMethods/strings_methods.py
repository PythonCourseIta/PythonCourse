def main():

	stringa = "python course"
	fstringa1 = "python course by {0} {1}"
	fstringa2 = "python course by {} {}"
	fstringa3 = "python course by {n} {s}"
	ljstringa = "   python course"
	data = "18 Novembre 2019"
	print_str = "Questo è il risultato di "

	# Capitalize : str -> str
	print(print_str + ".capitalize: " + stringa.capitalize())

	# Count : Str x Str -> int
	print(print_str + ".count: " + str(stringa.count("o")))

	# Endswith : Str x Str -> booleano
	print(print_str + ".endswith: " + str(stringa.endswith(" course")))

	# Find : Str x Str -> int
	print(print_str + ".find: " + str(stringa.find("ou")))

	# Format : Str x Str1 x ... x Strn -> Str
	print(print_str + ".format 1: " + fstringa1.format("Riccardo", "La Marca"))
	print(print_str + ".format 2: " + fstringa2.format("Riccardo", "La Marca"))
	print(print_str + ".format 3: " + fstringa3.format(n="Riccardo", s="La Marca"))

	# Index : Str x Int -> Int
	print(print_str + ".index: " + str(stringa.index("ou")))

	# Isalnum : Str -> boolean
	print(print_str + ".isalnum: " + str(stringa.isalnum()))

	# Isnumeric : Str -> boolean
	print(print_str + ".isnumeric: " + str(stringa.isnumeric()))

	# Istitle : Str -> boolean
	print(print_str + ".istitle: " + str(stringa.istitle()))

	# Isupper : Str -> boolean
	print(print_str + ".isupper: " + str(stringa.isupper()))

	# Islower : Str -> boolean
	print(print_str + ".islower: " + str(stringa.islower()))

	# Ljust : Str x Int -> Str
	print(print_str + ".ljust: " + ljstringa.ljust(len(stringa) + 4).__repr__())

	# Lower : Str -> Str
	print(print_str + ".lower: " + stringa.lower())

	# Upper : Str -> Str
	print(print_str + ".upper: " + stringa.upper())

	# Replace : Str x Str x Str -> Str
	print(print_str + ".replace: " + stringa.replace("course", "language"))

	# Strip : Str -> Str
	print(print_str + ".strip: " + ljstringa.strip())

	# Split : Str x Str -> List
	print(print_str + ".split: " + str(data.split())) 	

	# Join : Str x Iter -> Str
	print(print_str + ".join: " + "/".join(data.split()))

	return 0

if __name__ == "__main__":
	main()