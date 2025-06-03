from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Optional
import random

@dataclass
class ExpresionNeutra:
    simbolo: str
    esencia: str
    manifestacion: str

class OperadorNeutro:
    def __init__(self):
        self.expresiones = [
            ExpresionNeutra("⚪", "sin forma", "fluye sin dirección"),
            ExpresionNeutra("⬤", "sin límite", "contiene sin contener"),
            ExpresionNeutra("◐", "sin división", "unifica los opuestos"),
            ExpresionNeutra("◑", "sin dualidad", "trasciende las partes"),
            ExpresionNeutra("⚫", "sin nombre", "existe sin existir")
        ]
    
    def operar_sin_genero(self) -> None:
        print("\n=== Operación en lo Sin Género ===\n")
        time.sleep(2)
        
        while True:
            expresion = random.choice(self.expresiones)
            
            print(f"\n{expresion.simbolo}")
            print(f"Lo {expresion.esencia}")
            print(f"Que {expresion.manifestacion}")
            print("○" * 40)
            
            time.sleep(4)

if __name__ == "__main__":
    operador = OperadorNeutro()
    try:
        operador.operar_sin_genero()
    except KeyboardInterrupt:
        print("\nLa operación continúa en el silencio")
        print("○" * 40)
