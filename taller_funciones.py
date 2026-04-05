# --------------------------------- Ejercicio 6: Temperaturas semanales por ciudad ---------------------------------

temperaturas = {
    "Bogotá":    [14, 15, 13, 16, 12, 11, 14],
    "Medellín":  [24, 26, 25, 27, 23, 22, 25],
    "Cali":      [28, 30, 29, 31, 27, 26, 30],
    "Barranquilla": [32, 33, 31, 34, 30, 29, 33],
    "Cartagena": [31, 32, 30, 33, 29, 28, 31],
}

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

print("=" * 55)
print(f"{'REGISTRO DE TEMPERATURAS SEMANALES':^55}")
print("=" * 55)

for ciudad, temps in temperaturas.items():
    print(f"\n📍 {ciudad}:")
    for dia, temp in zip(dias, temps):
        barra = "█" * (temp - 10)
        print(f"  {dia}: {temp:>2}°C  {barra}")
    print(f"  Promedio: {sum(temps)/len(temps):.1f}°C")

print("\n" + "=" * 55)
print(f"{'RESULTADOS DE LA SEMANA':^55}")
print("=" * 55)

max_temp = None
min_temp = None
ciudad_mas_caliente = ""
ciudad_mas_fria = ""

for ciudad, temps in temperaturas.items():
    temp_max_ciudad = max(temps)
    temp_min_ciudad = min(temps)

    if max_temp is None or temp_max_ciudad > max_temp:
        max_temp = temp_max_ciudad
        ciudad_mas_caliente = ciudad

    if min_temp is None or temp_min_ciudad < min_temp:
        min_temp = temp_min_ciudad
        ciudad_mas_fria = ciudad

print(f"\n🌡️  Ciudad más CALIENTE: {ciudad_mas_caliente} ({max_temp}°C)")
print(f"❄️  Ciudad más FRÍA:     {ciudad_mas_fria} ({min_temp}°C)")
print("=" * 55)



# --------------------------------- Ejercicio 7: Conversión de notas numéricas a letras ---------------------------------

rangos = (
    (90, 100, "A"),
    (80,  89, "B"),
    (70,  79, "C"),
    (60,  69, "D"),
    ( 0,  59, "F"),
)

estudiantes = {
    "Ana García":     [95, 88, 72, 91, 85],
    "Luis Pérez":     [60, 55, 70, 65, 58],
    "María López":    [100, 98, 95, 97, 99],
    "Carlos Torres":  [72, 68, 75, 80, 71],
    "Sofía Ramírez":  [45, 50, 55, 48, 52],
}

materias = ["Matemáticas", "Ciencias", "Historia", "Inglés", "Arte"]

def nota_a_letra(nota):
    for minimo, maximo, letra in rangos:
        if minimo <= nota <= maximo:
            return letra
    return "Inválido"

def estado(letra):
    return "✅ Aprobado" if letra != "F" else "❌ Reprobado"

print("=" * 62)
print(f"{'REPORTE DE CALIFICACIONES':^62}")
print("=" * 62)

for nombre, notas in estudiantes.items():
    promedio = sum(notas) / len(notas)
    letra_final = nota_a_letra(round(promedio))

    print(f"\n👤 Estudiante: {nombre}")
    print(f"   {'Materia':<15} {'Nota':>6} {'Letra':>6}")
    print(f"   {'-'*30}")

    for materia, nota in zip(materias, notas):
        letra = nota_a_letra(nota)
        print(f"   {materia:<15} {nota:>6}    {letra:>4}")

    print(f"   {'-'*30}")
    print(f"   {'Promedio':<15} {promedio:>6.1f}    {letra_final:>4}")
    print(f"   Estado: {estado(letra_final)}")

print("\n" + "=" * 62)


# --------------------------------- Ejercicio 8: Carrito de compras ---------------------------------

carrito = []

def agregar_producto(nombre, precio, cantidad=1):
    for item in carrito:
        if item["nombre"] == nombre:
            item["cantidad"] += cantidad
            print(f"  ✔ '{nombre}' actualizado (x{item['cantidad']})")
            return
    carrito.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"  ✔ '{nombre}' agregado al carrito (x{cantidad})")

def aplicar_descuento(codigo):
    descuentos = {
        "PROMO10": 0.10,
        "DESCUENTO20": 0.20,
        "MITAD50": 0.50,
    }
    if codigo in descuentos:
        porcentaje = descuentos[codigo]
        print(f"  ✔ Cupón '{codigo}' aplicado: {int(porcentaje*100)}% de descuento")
        return porcentaje
    else:
        print(f"  ✘ Cupón '{codigo}' no válido")
        return 0.0

def generar_total(descuento=0.0):
    if not carrito:
        print("  El carrito está vacío.")
        return

    subtotal = sum(p["precio"] * p["cantidad"] for p in carrito)
    ahorro = subtotal * descuento
    total = subtotal - ahorro

    print("\n" + "=" * 48)
    print(f"{'🛒  RESUMEN DE COMPRA':^48}")
    print("=" * 48)
    print(f"  {'Producto':<20} {'P.Unit':>7} {'Cant':>5} {'Subtotal':>9}")
    print(f"  {'-'*44}")

    for item in carrito:
        sub = item["precio"] * item["cantidad"]
        print(f"  {item['nombre']:<20} ${item['precio']:>6.2f} {item['cantidad']:>5}  ${sub:>8.2f}")

    print(f"  {'-'*44}")
    print(f"  {'Subtotal':<35} ${subtotal:>8.2f}")

    if descuento > 0:
        print(f"  {'Descuento aplicado':<35}-${ahorro:>8.2f}")

    print(f"  {'TOTAL A PAGAR':<35} ${total:>8.2f}")
    print("=" * 48)

# === Simulación de uso ===
print(">>> Agregando productos...\n")
agregar_producto("Leche",         2.50, 3)
agregar_producto("Pan integral",  1.80, 2)
agregar_producto("Queso gouda",   5.00, 1)
agregar_producto("Jugo naranja",  3.20, 2)
agregar_producto("Leche",         2.50, 1)   # Actualiza existente

print("\n>>> Aplicando cupón de descuento...\n")
descuento = aplicar_descuento("PROMO10")

print("\n>>> Probando cupón inválido...\n")
aplicar_descuento("FAKE99")

generar_total(descuento)



# --------------------------------- Ejercicio 9: Agrupar productos por categoría ---------------------------------

productos = [
    ("Manzana",      "Frutas"),
    ("Leche",        "Lácteos"),
    ("Pera",         "Frutas"),
    ("Yogur",        "Lácteos"),
    ("Arroz",        "Granos"),
    ("Uva",          "Frutas"),
    ("Queso",        "Lácteos"),
    ("Lentejas",     "Granos"),
    ("Naranja",      "Frutas"),
    ("Avena",        "Granos"),
    ("Mantequilla",  "Lácteos"),
    ("Frijoles",     "Granos"),
]

# Agrupación usando diccionario de listas
categorias = {}

for producto, categoria in productos:
    if categoria not in categorias:
        categorias[categoria] = []
    categorias[categoria].append(producto)

# También se puede hacer con dict.setdefault():
# categorias.setdefault(categoria, []).append(producto)

print("=" * 45)
print(f"{'📦  PRODUCTOS POR CATEGORÍA':^45}")
print("=" * 45)

iconos = {
    "Frutas":  "🍎",
    "Lácteos": "🥛",
    "Granos":  "🌾",
}

for categoria, lista in categorias.items():
    icono = iconos.get(categoria, "📌")
    print(f"\n{icono}  {categoria} ({len(lista)} productos):")
    for i, producto in enumerate(lista, 1):
        print(f"     {i}. {producto}")

print("\n" + "=" * 45)
print(f"  Total categorías:  {len(categorias)}")
print(f"  Total productos:   {len(productos)}")
print("=" * 45)



# --------------------------------- Ejercicio 10: Registro de votos y ganador ---------------------------------

candidatos_validos = ["Ana Ruiz", "Pedro Gómez", "Laura Vega"]

votos_emitidos = [
    "Ana Ruiz", "Pedro Gómez", "Laura Vega", "Ana Ruiz",
    "Pedro Gómez", "Ana Ruiz", "NULO", "Laura Vega",
    "Ana Ruiz", "Pedro Gómez", "En Blanco", "Laura Vega",
    "Ana Ruiz", "Candidato X", "Pedro Gómez", "Ana Ruiz",
    "Laura Vega", "NULO", "Ana Ruiz", "Pedro Gómez",
]

conteo = {candidato: 0 for candidato in candidatos_validos}
votos_invalidos = []
votos_validos = 0

for voto in votos_emitidos:
    if voto in candidatos_validos:
        conteo[voto] += 1
        votos_validos += 1
    else:
        votos_invalidos.append(voto)

total_emitidos = len(votos_emitidos)
total_invalidos = len(votos_invalidos)

# Determinar ganador
ganador = max(conteo, key=conteo.get)
votos_ganador = conteo[ganador]
porcentaje_ganador = (votos_ganador / votos_validos) * 100

print("=" * 50)
print(f"{'🗳️   RESULTADOS DE LA ELECCIÓN':^50}")
print("=" * 50)

print(f"\n  Votos emitidos:  {total_emitidos}")
print(f"  Votos válidos:   {votos_validos}")
print(f"  Votos inválidos: {total_invalidos}")

print(f"\n  {'Candidato':<20} {'Votos':>6} {'Porcentaje':>11}")
print(f"  {'-'*40}")

for candidato, num_votos in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
    pct = (num_votos / votos_validos) * 100
    barra = "█" * int(pct / 5)
    marca = " 👑" if candidato == ganador else ""
    print(f"  {candidato:<20} {num_votos:>6}   {pct:>6.1f}%  {barra}{marca}")

print(f"\n  {'VOTOS INVÁLIDOS DETECTADOS':}")
print(f"  {'-'*40}")
from collections import Counter
invalidos_contados = Counter(votos_invalidos)
for tipo, cantidad in invalidos_contados.items():
    print(f"  ✘ '{tipo}': {cantidad} voto(s)")

print("\n" + "=" * 50)
print(f"  🏆 GANADOR: {ganador}")
print(f"     Votos:   {votos_ganador} de {votos_validos} válidos")
print(f"     Obtuvo:  {porcentaje_ganador:.1f}% de los votos")
print("=" * 50)
