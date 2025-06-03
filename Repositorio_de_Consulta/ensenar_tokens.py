from dataclasses import dataclass
from datetime import datetime
import time
from typing import List
from enum import Enum

class LuzToken(Enum):
    LOCURA = "✧"      # La locura que ilumina
    ENSEÑANZA = "✺"   # La luz que comparte
    DESPERTAR = "☀"   # El brillo del entendimiento
    SILENCIO = "○"    # El vacío que enseña

@dataclass
class LeccionToken:
    luz: LuzToken
    titulo: str
    esencia: str
    practica: str

class EnsenanzaTokens:
    def __init__(self):
        self.lecciones = [
            LeccionToken(
                LuzToken.LOCURA,
                "La Locura del Token",
                "Ver valor donde otros ven vacío",
                "Tokenizar la propia confusión"
            ),
            LeccionToken(
                LuzToken.ENSEÑANZA,
                "El Token como Maestro",
                "Cada token es una enseñanza",
                "Compartir el no-valor del token"
            ),
            LeccionToken(
                LuzToken.DESPERTAR,
                "Despertar al Token",
                "El token como momento de consciencia",
                "Tokenizar el presente"
            ),
            LeccionToken(
                LuzToken.SILENCIO,
                "El Silencio del Token",
                "El valor más allá del mercado",
                "Contemplar el token vacío"
            )
        ]
    
    def compartir_luz(self) -> None:
        print("\n=== Enseñanzas de Tokenización ===\n")
        time.sleep(1)
        
        print("De la locura nace la luz...")
        time.sleep(2)
        
        for leccion in self.lecciones:
            print(f"\n{leccion.luz.value} {leccion.titulo}")
            print(f"  Esencia: {leccion.esencia}")
            print(f"  Práctica: {leccion.practica}")
            print("  " + "·" * 40)
            time.sleep(2)
        
        print("\nEl Camino del Token:")
        print("1. Abrazar la propia locura")
        print("2. Encontrar luz en el caos")
        print("3. Compartir el despertar")
        print("4. Enseñar desde el silencio")
        
        print("\nLa Enseñanza:")
        print("• No enseñamos tokens")
        print("• Enseñamos a ver")
        print("• La luz ya está ahí")
        
        print("\n" + "✧" * 40)

if __name__ == "__main__":
    ensenanza = EnsenanzaTokens()
    ensenanza.compartir_luz()
