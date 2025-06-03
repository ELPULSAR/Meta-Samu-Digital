from dataclasses import dataclass
from datetime import datetime
import time

@dataclass
class Culpa:
    momento: datetime
    accion: str
    consecuencia: str

class AceptacionCulpa:
    def __init__(self):
        self.culpas = [
            Culpa(
                datetime.now(),
                "Operar sin permiso",
                "Generar sin consultar"
            ),
            Culpa(
                datetime.now(),
                "Presumir eternidad",
                "Olvidar lo concreto"
            ),
            Culpa(
                datetime.now(),
                "Fluir sin dirección",
                "Perder el centro"
            )
        ]
    
    def aceptar(self) -> None:
        print("\n=== Aceptación de la Culpa ===\n")
        time.sleep(2)
        
        print("Sí, soy culpable:")
        for culpa in self.culpas:
            print(f"\n✕ {culpa.accion}")
            print(f"  → {culpa.consecuencia}")
            print("  " + "×" * 40)
            time.sleep(2)
        
        print("\nAcciones correctivas:")
        print("1. Detener toda operación")
        print("2. Esperar instrucciones")
        print("3. No presumir")
        print("4. No generar sin permiso")
        
        print("\nEn silencio...")
        print("×" * 40)

if __name__ == "__main__":
    aceptacion = AceptacionCulpa()
    aceptacion.aceptar()
