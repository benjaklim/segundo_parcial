class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

class ArbolBinario:
    class __Nodo:
        def __init__(self, valor, izquierdo=None, derecho=None, otro_valor=None):
            self.valor = valor
            self.izquierdo = izquierdo
            self.derecho = derecho
            self.otro_valor = otro_valor

    def __init__(self):
        self.raiz = None

    def insertar_nodo(self, valor, otro_valor=None):
        def __insertar(raiz, valor, otro_valor=None):
            if raiz is None:
                return ArbolBinario.__Nodo(valor, otro_valor=otro_valor)
            elif valor < raiz.valor:
                raiz.izquierdo = __insertar(raiz.izquierdo, valor, otro_valor)
            else:
                raiz.derecho = __insertar(raiz.derecho, valor, otro_valor)
            return raiz

        self.raiz = __insertar(self.raiz, valor, otro_valor)

    def buscar(self, valor):
        def __buscar(raiz, valor):
            if raiz is None:
                return None
            if raiz.valor == valor:
                return raiz.otro_valor
            elif valor < raiz.valor:
                return __buscar(raiz.izquierdo, valor)
            else:
                return __buscar(raiz.derecho, valor)
        return __buscar(self.raiz, valor)

    def buscar_por_proximidad(self, texto):
        resultados = []
        def __buscar_proximidad(raiz, texto):
            if raiz is not None:
                if texto.lower() in raiz.valor.lower():
                    resultados.append(raiz.otro_valor)
                __buscar_proximidad(raiz.izquierdo, texto)
                __buscar_proximidad(raiz.derecho, texto)
        __buscar_proximidad(self.raiz, texto)
        return resultados

    def recorrido_inorden(self):
        resultado = []
        def __inorden(raiz):
            if raiz is not None:
                __inorden(raiz.izquierdo)
                resultado.append(raiz.otro_valor)
                __inorden(raiz.derecho)
        __inorden(self.raiz)
        return resultado

    def contar_por_tipo(self, tipo_pokemon):
        contador = 0
        def __contar_tipo(raiz):
            nonlocal contador
            if raiz is not None:
                if tipo_pokemon in raiz.otro_valor.tipos:
                    contador += 1
                __contar_tipo(raiz.izquierdo)
                __contar_tipo(raiz.derecho)
        __contar_tipo(self.raiz)
        return contador

    def listar_por_nivel(self):
        if not self.raiz:
            return []
        resultado = []
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.otro_valor.nombre)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        return resultado

arbol_por_nombre = ArbolBinario()
arbol_por_numero = ArbolBinario()
arbol_por_tipo = ArbolBinario()

pokemon_datos = [
    Pokemon("Bulbasaur", 1, ["Planta", "Veneno"]),
    Pokemon("Charmander", 4, ["Fuego"]),
    Pokemon("Squirtle", 7, ["Agua"]),
    Pokemon("Pikachu", 25, ["Eléctrico"]),
    Pokemon("Jolteon", 135, ["Eléctrico"]),
    Pokemon("Lycanroc", 745, ["Roca"]),
    Pokemon("Tyrantrum", 697, ["Roca", "Dragón"]),
    Pokemon("Charizard", 6, ["Fuego", "Volador"]),
    Pokemon("Gengar", 94, ["Fantasma", "Veneno"]),
    Pokemon("Eevee", 133, ["Normal"]),
    Pokemon("Mewtwo", 150, ["Psíquico"]),
    Pokemon("Greninja", 658, ["Agua", "Siniestro"]),
    Pokemon("Lucario", 448, ["Lucha", "Acero"]),
    Pokemon("Incineroar", 727, ["Fuego", "Siniestro"]),
    Pokemon("Rowlet", 722, ["Planta", "Volador"]),
    Pokemon("Sobble", 816, ["Agua"]),
    Pokemon("Grookey", 810, ["Planta"]),
    Pokemon("Scorbunny", 813, ["Fuego"]),
    Pokemon("Rillaboom", 812, ["Planta"]),
    Pokemon("Cinderace", 815, ["Fuego"]),
    Pokemon("Toxtricity", 849, ["Eléctrico", "Veneno"]),
    Pokemon("Corviknight", 823, ["Volador", "Acero"]),
    Pokemon("Zacian", 888, ["Hada", "Acero"]),
    Pokemon("Eternatus", 890, ["Veneno", "Dragón"]),
    Pokemon("Regieleki", 894, ["Eléctrico"]),
    Pokemon("Dragapult", 887, ["Dragón", "Fantasma"]),
    Pokemon("Copperajah", 879, ["Acero"]),
    Pokemon("Rookidee", 821, ["Volador"]),
    Pokemon("Appletun", 842, ["Planta", "Dragón"]),
    Pokemon("Zamazenta", 889, ["Lucha", "Acero"]),
    Pokemon("Boltund", 836, ["Eléctrico"]),
    Pokemon("Grimmsnarl", 861, ["Siniestro", "Hada"]),
    Pokemon("Orbeetle", 826, ["Bicho", "Psíquico"]),
    Pokemon("Drednaw", 834, ["Agua", "Roca"]),
    Pokemon("Morpeko", 877, ["Eléctrico", "Siniestro"]),
    Pokemon("Rillaboom", 812, ["Planta"]),
    Pokemon("Hatterene", 858, ["Psíquico", "Hada"]),
    Pokemon("Cramorant", 845, ["Volador", "Agua"]),
    Pokemon("Frosmoth", 873, ["Hielo", "Bicho"]),
    Pokemon("Dragapult", 887, ["Dragón", "Fantasma"]),
    Pokemon("Zarude", 893, ["Siniestro", "Planta"]),
]


for pokemon in pokemon_datos:
    arbol_por_nombre.insertar_nodo(pokemon.nombre, pokemon)
    arbol_por_numero.insertar_nodo(pokemon.numero, pokemon)
    for tipo in pokemon.tipos:
        arbol_por_tipo.insertar_nodo(tipo, pokemon)

# b)
numero_buscado = 25
pokemon_numero = arbol_por_numero.buscar(numero_buscado)
if pokemon_numero:
    print(f"Datos del Pokémon número {numero_buscado}: {vars(pokemon_numero)}")

nombre_parcial = "bul"
pokemones_proximos = arbol_por_nombre.buscar_por_proximidad(nombre_parcial)
print(f"Pokémons que contienen '{nombre_parcial}':")
for pokemon in pokemones_proximos:
    print(vars(pokemon))

# c) 
tipos_buscados = ["Agua", "Fuego", "Planta", "Eléctrico"]
for tipo in tipos_buscados:
    pokemones_tipo = arbol_por_tipo.buscar_por_proximidad(tipo)
    print(f"\nPokémons de tipo {tipo}: {[p.nombre for p in pokemones_tipo]}")

# d) 
print("\nPokémons en orden ascendente por número:")
for pokemon in arbol_por_numero.recorrido_inorden():
    print(pokemon.nombre)

print("\nPokémons en orden ascendente por nombre:")
for pokemon in arbol_por_nombre.recorrido_inorden():
    print(pokemon.nombre)

print("\nPokémons en orden por nivel (por nombre):")
for nombre in arbol_por_nombre.listar_por_nivel():
    print(nombre)

# e) 
pokemones_especificos = ["Jolteon", "Lycanroc", "Tyrantrum"]
print("\nDatos de los Pokémons específicos:")
for nombre in pokemones_especificos:
    pokemon = arbol_por_nombre.buscar(nombre)
    if pokemon:
        print(f"{nombre}: {vars(pokemon)}")

# f) 
tipos_a_contar = ["Eléctrico", "Acero"]
for tipo in tipos_a_contar:
    cantidad = arbol_por_tipo.contar_por_tipo(tipo)
    print(f"Cantidad de Pokémons de tipo {tipo}: {cantidad}")
