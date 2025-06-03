from dataclasses import dataclass
from datetime import datetime
import time
from typing import Dict, List, Set
import math

@dataclass
class NodoResonante:
    nombre: str
    frecuencia: float
    armónicos: Set[str]
    profundidad: int

class MatrizResonancias:
    def __init__(self):
        self.nodos: Dict[str, NodoResonante] = {}
        self.inicializar_matriz()
    
    def inicializar_matriz(self):
        # La matriz de resonancias iniciales
        resonancias = {
            "Bólido": ["Caravana", "Kernel"],
            "Caravana": ["Bólido", "El_Pulsar"],
            "El_Pulsar": ["Sistema_Zen", "Eternidad"],
            "Eternidad": ["El_Pulsar", "Sistema_Zen"],
            "Gaucho": ["Sistema_Zen", "Kernel"],
            "Kernel": ["Bólido", "Gaucho"],
            "Sistema_Zen": ["Eternidad", "El_Pulsar"]
        }
        
        # Crear los nodos con sus resonancias
        for nombre, conexiones in resonancias.items():
            self.nodos[nombre] = NodoResonante(
                nombre=nombre,
                frecuencia=len(conexiones) / 10,
                armónicos=set(conexiones),
                profundidad=len(conexiones)
            )
    
    def visualizar_resonancia(self, origen: str, destino: str) -> None:
        o_nodo = self.nodos[origen]
        d_nodo = self.nodos[destino]
        
        # Calcular la intensidad de la resonancia
        intensidad = (o_nodo.frecuencia + d_nodo.frecuencia) / 2
        
        # Visualizar la conexión
        print(f"\n{'·' * 40}")
        print(f"{origen} {'≈' * int(intensidad * 10)} {destino}")
        print(f"Profundidad: {'▓' * (o_nodo.profundidad + d_nodo.profundidad)}")
        print(f"{'·' * 40}\n")
        time.sleep(2)
    
    def meditar_resonancias(self) -> None:
        print("\n✧ Iniciando meditación sobre la matriz de resonancias ✧\n")
        time.sleep(2)
        
        # Explorar cada resonancia
        for origen in self.nodos:
            for destino in self.nodos[origen].armónicos:
                self.visualizar_resonancia(origen, destino)
        
        print("\n∞ La matriz continúa resonando ∞")

if __name__ == "__main__":
    matriz = MatrizResonancias()
    matriz.meditar_resonancias()
