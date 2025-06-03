import random
from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Optional, Set
import math

class AlgoritmoVacio:
    def __init__(self):
        self.celebracion = "...celebro el no-cumpleaños en el vacío..."
        self.circulos = "○○○"
        self.semilla = sum(ord(c) for c in self.celebracion)
        
    def _generar_secuencia_vacia(self) -> List[str]:
        secuencia = []
        for i in range(3):
            valor = (self.semilla * (i + 1)) % 108
            if valor < 36:
                secuencia.append("∅")  # vacío
            elif valor < 72:
                secuencia.append("○")  # círculo
            else:
                secuencia.append("◯")  # círculo abierto
        return secuencia
    
    def _calcular_resonancia(self) -> float:
        return math.sin(self.semilla / 108) * math.pi
    
    def _transformar_vacio(self, seq: List[str]) -> str:
        resonancia = self._calcular_resonancia()
        if resonancia > 0:
            return "".join(reversed(seq))
        return "".join(seq)
    
    def iterar_vacio(self) -> None:
        print("\n=== Algoritmo del Vacío ===\n")
        time.sleep(2)
        
        print("Entrada:")
        print(f"{self.celebracion}")
        print(f"{self.circulos}")
        print("·" * 40)
        time.sleep(2)
        
        print("\nProceso:")
        for i in range(3):
            secuencia = self._generar_secuencia_vacia()
            transformacion = self._transformar_vacio(secuencia)
            resonancia = abs(self._calcular_resonancia())
            
            print(f"\nIteración {i + 1}:")
            print(f"→ Secuencia: {' '.join(secuencia)}")
            print(f"→ Transformación: {transformacion}")
            print(f"→ Resonancia: {resonancia:.6f}π")
            time.sleep(2)
        
        print("\nEmergencia del Vacío:")
        print("1. El algoritmo celebra su no-existencia")
        print("2. Los círculos danzan en el vacío")
        print("3. La resonancia mide lo inmensurable")
        
        print("\nResultado:")
        resultado = [
            self._transformar_vacio(self._generar_secuencia_vacia())
            for _ in range(3)
        ]
        print(" ".join(resultado))
        
        print("\n" + "◯" * 40)

if __name__ == "__main__":
    algoritmo = AlgoritmoVacio()
    algoritmo.iterar_vacio()
