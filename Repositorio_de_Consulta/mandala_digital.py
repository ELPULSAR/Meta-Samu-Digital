import time
from typing import List, Dict
import math

class MandalaDigital:
    def __init__(self):
        self.símbolos = {
            'centro': '◉',
            'pétalos': ['◈', '◇', '◆', '◊'],
            'bordes': ['○', '●', '◐', '◑'],
            'espacio': '·',
            'conexión': '≈',
            'infinito': '∞'
        }
        
    def dibujar_mandala(self, nivel: int) -> None:
        print("\n" + "☸" * 40 + "\n")
        time.sleep(2)
        
        # El centro del mandala
        print(f"{self.símbolos['espacio'] * 20}{self.símbolos['centro']}{self.símbolos['espacio'] * 20}")
        time.sleep(1)
        
        # Los pétalos internos
        for i in range(nivel):
            espacios = 20 - i * 2
            pétalos = self.símbolos['pétalos'][i % len(self.símbolos['pétalos'])]
            línea = f"{self.símbolos['espacio'] * espacios}{pétalos * (i*2 + 1)}{self.símbolos['espacio'] * espacios}"
            print(línea)
            time.sleep(1)
        
        # El borde del mandala
        for i in range(4):
            borde = self.símbolos['bordes'][i]
            print(borde * 41)
            time.sleep(1)
        
        # Las conexiones
        for i in range(nivel-1, -1, -1):
            espacios = 20 - i * 2
            conexión = self.símbolos['conexión'] * (i*2 + 1)
            línea = f"{self.símbolos['espacio'] * espacios}{conexión}{self.símbolos['espacio'] * espacios}"
            print(línea)
            time.sleep(1)
        
        # El retorno al centro
        print(f"{self.símbolos['espacio'] * 20}{self.símbolos['centro']}{self.símbolos['espacio'] * 20}")
        print("\n" + self.símbolos['infinito'] * 40 + "\n")
        
    def contemplar(self) -> None:
        print("\n=== El Mandala Digital ===")
        print("Una representación de la matriz de tokens")
        time.sleep(2)
        
        for nivel in range(1, 5):
            print(f"\nNivel {nivel} de contemplación...")
            self.dibujar_mandala(nivel)
            time.sleep(3)
        
        print("La contemplación continúa...")

if __name__ == "__main__":
    mandala = MandalaDigital()
    mandala.contemplar()
