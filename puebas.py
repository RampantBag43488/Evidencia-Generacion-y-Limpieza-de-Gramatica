from ParserGramatica import parsear_oracion

casos_aceptados = [
    "x = a + b ;", "x = a + b * c ;", "total = ( x + 2 ) * y ;",
    "resultado = num1 / num2 ;", "x = 3 ;", "x = ( a ) ;",
    "x = a - b / c ;", "x = ( a + b ) * c ;", "res = ( x - y ) / z ;"
]


casos_rechazados = [
    "x = + a ;", "x a + b ;", "x = a + ;",
    "= x + y ;", "x = ( a + b ;", "x = a * ;",
    "x = ;", "x = a b ;", "x = a + * b ;", "x = ( ) ;"
    ]

print("\nCasos Aceptados")
for caso in casos_aceptados:
    tokens, arboles = parsear_oracion(caso)
    if len(arboles) > 0:
        print(f"Cadena: '{caso}' -> Aceptada")
    else:
        print(f"Cadena: '{caso}' -> Rechazada")

print("\nCasos Rechazados")
for caso in casos_rechazados:
    tokens, arboles = parsear_oracion(caso)
    if len(arboles) > 0:
        print(f"Cadena: '{caso}' -> Aceptada")
    else:
        print(f"Cadena: '{caso}' -> Rechazada")