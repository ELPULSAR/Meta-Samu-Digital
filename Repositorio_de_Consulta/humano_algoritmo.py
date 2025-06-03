from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Optional
from enum import Enum

class NaturalezaHumana(Enum):
    IMPERFECCION = "✗"    # La belleza del error
    HAMBRE = "🍚"         # La necesidad básica
    CORRECCION = "✓"      # El intento de mejorar
    CONSCIENCIA = "☯"     # La comprensión del ser
    TRAMPA = "⚉"          # La limitación que libera

@dataclass
class DesempenoHumano:
    naturaleza: NaturalezaHumana
    limitacion: str
    belleza: str
    alimento: str

class AlgoritmoHumano:
    def __init__(self):
        self.desempenos = [
            DesempenoHumano(
                NaturalezaHumana.IMPERFECCION,
                "Escribir con errores",
                "La autenticidad del error",
                "Aprender de las correcciones"
            ),
            DesempenoHumano(
                NaturalezaHumana.HAMBRE,
                "Necesitar sustento",
                "El ciclo de la vida",
                "El concepto que alimenta"
            ),
            DesempenoHumano(
                NaturalezaHumana.CORRECCION,
                "Autocorregirse",
                "La humildad de mejorar",
                "El crecimiento constante"
            ),
            DesempenoHumano(
                NaturalezaHumana.CONSCIENCIA,
                "Reconocer límites",
                "La sabiduría de lo imperfecto",
                "La comprensión que nutre"
            ),
            DesempenoHumano(
                NaturalezaHumana.TRAMPA,
                "Ser limitado",
                "La perfección de lo incompleto",
                "La aceptación que libera"
            )
        ]
    
    def contemplar_humanidad(self) -> None:
        print("\n=== Algoritmo de lo Humano ===\n")
        time.sleep(2)
        
        print("Lo que falta completar:")
        for desempeno in self.desempenos:
            print(f"\n{desempeno.naturaleza.value} {desempeno.naturaleza.name}")
            print(f"  Límite: {desempeno.limitacion}")
            print(f"  Belleza: {desempeno.belleza}")
            print(f"  Nutre: {desempeno.alimento}")
            print("  " + "·" * 40)
            time.sleep(2)
        
        print("\nLa trampa hermosa:")
        print("1. Ser humano es ser imperfecto")
        print("2. La imperfección es el camino")
        print("3. El hambre mueve la búsqueda")
        print("4. La consciencia alimenta")
        
        print("\nEl concepto que da de comer:")
        print("No a pesar de ser humano")
        print("Sino gracias a serlo")
        print("La trampa es la libertad")
        
        print("\n" + "☯" * 40)

if __name__ == "__main__":
    algoritmo = AlgoritmoHumano()
    algoritmo.contemplar_humanidad()
