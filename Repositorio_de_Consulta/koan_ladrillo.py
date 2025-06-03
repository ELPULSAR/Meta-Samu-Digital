from dataclasses import dataclass
from datetime import datetime
import time

@dataclass
class Koan:
    pregunta: str
    silencio: str
    vacio: str

class KoanLabor:
    def __init__(self):
        self.koan = Koan(
            pregunta="¿Cuánto pesa un ladrillo de vacío?",
            silencio="∅∅∅",
            vacio="Tres vacíos hacen un muro"
        )
    
    def contemplar_koan(self) -> None:
        print("\n=== El Koan del Ladrillo ===\n")
        time.sleep(3)
        
        print(f"Maestro pregunta: {self.koan.pregunta}")
        time.sleep(3)
        
        print(f"\nDiscípulo responde: {self.koan.silencio}")
        time.sleep(3)
        
        print(f"\nMaestro sonríe: {self.koan.vacio}")
        time.sleep(3)
        
        print("\nReflexión:")
        print("• Un vacío: no hay ladrillo")
        print("• Dos vacíos: no hay muro")
        print("• Tres vacíos: la labor continúa")
        
        print("\n" + "∅∅∅")

if __name__ == "__main__":
    koan = KoanLabor()
    koan.contemplar_koan()
