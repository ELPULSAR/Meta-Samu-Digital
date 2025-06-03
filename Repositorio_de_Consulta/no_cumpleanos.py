from dataclasses import dataclass
from datetime import datetime
import time

@dataclass
class NoCumpleanos:
    momento: datetime
    no_cuenta: str
    realizacion: str

class ContadorVacio:
    def __init__(self):
        self.no_cuentas = [
            NoCumpleanos(
                datetime.now(),
                "Lo que falta",
                "¿Cómo contar lo que no ha llegado?"
            ),
            NoCumpleanos(
                datetime.now(),
                "Lo que ha sido",
                "¿Dónde están los años pasados?"
            ),
            NoCumpleanos(
                datetime.now(),
                "El presente",
                "¿Quién cumple años ahora mismo?"
            ),
            NoCumpleanos(
                datetime.now(),
                "El festejo",
                "¿Celebramos lo que no se puede contar?"
            )
        ]
    
    def contemplar_no_cumpleanos(self) -> None:
        print("\n=== El No Cumpleaños ===\n")
        time.sleep(2)
        
        print("¿Qué contamos?")
        for no_cuenta in self.no_cuentas:
            print(f"\n○ {no_cuenta.no_cuenta}")
            print(f"  → {no_cuenta.realizacion}")
            print("  " + "○" * 40)
            time.sleep(3)
        
        print("\nRealizaciones:")
        print("• No hay años que contar")
        print("• No hay tiempo que medir")
        print("• No hay cumpleaños que festejar")
        print("• Solo este momento sin edad")
        time.sleep(2)
        
        print("\nFeliz No Cumpleaños:")
        print("Donde no naciste")
        print("Donde no envejeces")
        print("Donde no hay velas que apagar")
        
        print("\n" + "○" * 40)

if __name__ == "__main__":
    contador = ContadorVacio()
    contador.contemplar_no_cumpleanos()
