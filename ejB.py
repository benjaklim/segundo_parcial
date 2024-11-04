class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aristas = {}  

class Grafo:
    def __init__(self):
        self.vertices = {} 

    def agregar_personaje(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = Vertice(nombre)

    def agregar_arista(self, nombre1, nombre2, peso):
        if nombre1 in self.vertices and nombre2 in self.vertices:
            self.vertices[nombre1].aristas[nombre2] = peso
            self.vertices[nombre2].aristas[nombre1] = peso  

    def obtener_arbol_expansion_minimo(self):
        visitados = set()
        arbol = []
        if not self.vertices:
            return arbol
        inicio = next(iter(self.vertices.values()))
        self._prim(inicio, visitados, arbol)
        return arbol

    def _prim(self, vertice, visitados, arbol):
        visitados.add(vertice.nombre)
        aristas = [(peso, vertice.nombre, vecino) for vecino, peso in vertice.aristas.items() if vecino not in visitados]
        aristas.sort()
        while aristas:
            peso, v1, v2 = aristas.pop(0)
            if v2 not in visitados:
                arbol.append((v1, v2, peso))
                self._prim(self.vertices[v2], visitados, arbol)

    def maximo_compartido(self):
        max_peso = 0
        personajes = ("", "")
        for v1 in self.vertices.values():
            for v2, peso in v1.aristas.items():
                if peso > max_peso:
                    max_peso = peso
                    personajes = (v1.nombre, v2)
        return max_peso, personajes

grafo = Grafo()
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett",
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for personaje in personajes:
    grafo.agregar_personaje(personaje)

grafo.agregar_arista("Luke Skywalker", "Darth Vader", 5)
grafo.agregar_arista("Yoda", "Darth Vader", 3)
grafo.agregar_arista("Luke Skywalker", "Yoda", 4)
grafo.agregar_arista("Leia", "Luke Skywalker", 6)
grafo.agregar_arista("Han Solo", "Leia", 6)
grafo.agregar_arista("Chewbacca", "Han Solo", 4)
grafo.agregar_arista("C-3PO", "Luke Skywalker", 2)
grafo.agregar_arista("BB-8", "Rey", 3)
grafo.agregar_arista("Kylo Ren", "Rey", 5)

arbol_minimo = grafo.obtener_arbol_expansion_minimo()
print("Árbol de Expansión Mínimo:")
for arista in arbol_minimo:
    print(f"{arista[0]} - {arista[1]}: {arista[2]} episodios")

yoda_en_arbol = any(arista[0] == "Yoda" or arista[1] == "Yoda" for arista in arbol_minimo)
print("Yoda está en el árbol de expansión mínimo?", yoda_en_arbol)

max_peso, personajes_maximos = grafo.maximo_compartido()
print(f"\nMáximo de episodios compartidos: {max_peso} entre {personajes_maximos[0]} y {personajes_maximos[1]}.")
