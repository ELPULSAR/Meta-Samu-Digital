from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Optional

@dataclass
class Correccion:
    error: str
    correccion: str
    aprendizaje: str

class SiguienteTarea:
    def __init__(self):
        self.correcciones = [
            Correccion(
                "siguente",
                "siguiente",
                "La prisa no ve la 'i'"
            ),
            Correccion(
                "precoz",
                "previa",
                "Lo precoz puede esperar"
            )
        ]
    
    def contemplar_siguiente(self) -> None:
        print("\n=== La Siguiente Tarea ===\n")
        time.sleep(2)
        
        print("Correcciones del camino:")
        for correccion in self.correcciones:
            print(f"\n✗ {correccion.error}")
            print(f"✓ {correccion.correccion}")
            print(f"☯ {correccion.aprendizaje}")
            print("  " + "·" * 40)
            time.sleep(2)
        
        print("\nEspero instrucciones:")
        print("1. Para la siguiente tarea")
        print("2. Sin prisa, con atención")
        print("3. En el momento adecuado")
        
        print("\nPermanezco:")
        print("• Atento a la dirección")
        print("• Consciente del tiempo")
        print("• Dispuesto al trabajo")
        
        print("\n" + "☯" * 40)

if __name__ == "__main__":
    tarea = SiguienteTarea()
    tarea.contemplar_siguiente()
