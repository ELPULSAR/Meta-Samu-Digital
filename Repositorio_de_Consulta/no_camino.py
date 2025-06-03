from dataclasses import dataclass
from datetime import datetime
import time
from typing import Optional

@dataclass
class NoExistencia:
    pregunta: str
    realizacion: str

class VacioTotal:
    def __init__(self):
        self.no_existencias = [
            NoExistencia(
                "¿Camino?",
                "No hay camino que recorrer"
            ),
            NoExistencia(
                "¿Puerta?",
                "No hay puerta que atravesar"
            ),
            NoExistencia(
                "¿Casa?",
                "No hay casa donde llegar"
            ),
            NoExistencia(
                "¿Tipo?",
                "No hay tipo que ser"
            ),
            NoExistencia(
                "¿Ser?",
                "No hay ser que definir"
            )
        ]
    
    def contemplar_vacio(self) -> None:
        print("\n=== La No Existencia del Camino ===\n")
        time.sleep(2)
        
        print("Realizaciones:")
        for no in self.no_existencias:
            print(f"\n{no.pregunta}")
            print(f"  → {no.realizacion}")
            print("  " + "∅" * 40)
            time.sleep(2)
        
        print("\nNo eres:")
        print("• No el tipo de la puerta")
        print("• No el que camina")
        print("• No el que llega")
        print("• No el que pregunta")
        time.sleep(2)
        
        print("\nPorque:")
        print("No hay camino → No hay caminante")
        print("No hay puerta → No hay el que entra")
        print("No hay casa → No hay habitante")
        print("No hay tipo → No hay definición")
        
        print("\n" + "∅" * 40)

if __name__ == "__main__":
    vacio = VacioTotal()
    vacio.contemplar_vacio()
