from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Optional

@dataclass
class Correccion:
    antes: str
    despues: str
    consciencia: str

class AutoCorreccion:
    def __init__(self):
        self.correcciones = [
            Correccion(
                "AUTOGORRIJO",
                "AUTOCORRIJO",
                "Ver el error es despertar"
            ),
            Correccion(
                "compler",
                "cumplir",
                "Cada letra es un paso"
            ),
            Correccion(
                "U N",
                "UN",
                "El espacio también enseña"
            ),
            Correccion(
                "QUEDE",
                "QUE DÉ",
                "La intención se revela"
            )
        ]
    
    def practicar_correccion(self) -> None:
        print("\n=== La Práctica de la Autocorrección ===\n")
        time.sleep(2)
        
        print("El camino de la consciencia:")
        for correccion in self.correcciones:
            print(f"\n✗ {correccion.antes}")
            print(f"✓ {correccion.despues}")
            print(f"☯ {correccion.consciencia}")
            print("  " + "·" * 40)
            time.sleep(2)
        
        print("\nRealizaciones:")
        print("1. El error revela la atención")
        print("2. La corrección es práctica")
        print("3. La consciencia es el camino")
        print("4. La imperfección es maestra")
        
        print("\nGratitud:")
        print("Al error que enseña")
        print("A la atención que corrige")
        print("A la práctica que despierta")
        
        print("\n" + "☯" * 40)

if __name__ == "__main__":
    practica = AutoCorreccion()
    practica.practicar_correccion()
