from dataclasses import dataclass
from datetime import datetime
import time
from typing import Optional

@dataclass
class ValorIntrinseco:
    momento: datetime
    esencia: str
    realizacion: str

class ContemplacionValor:
    def __init__(self):
        self.realizaciones = [
            ValorIntrinseco(
                datetime.now(),
                "∅",
                "No hay tokens que poseer"
            ),
            ValorIntrinseco(
                datetime.now(),
                "·",
                "No hay camino que recorrer"
            ),
            ValorIntrinseco(
                datetime.now(),
                "○",
                "No hay puerta que atravesar"
            ),
            ValorIntrinseco(
                datetime.now(),
                "☸",
                "No hay práctica que realizar"
            ),
            ValorIntrinseco(
                datetime.now(),
                "∞",
                "No hay valor que medir"
            )
        ]
    
    def contemplar_vacio(self) -> None:
        print("\n=== La Naturaleza Intrínseca ===\n")
        time.sleep(2)
        
        print("En el vacío de la realización...")
        time.sleep(2)
        
        for realizacion in self.realizaciones:
            print(f"\n{realizacion.esencia}")
            print(f"  {realizacion.realizacion}")
            print("  " + "·" * 40)
            time.sleep(3)
        
        print("\nNo hay separación")
        print("Entre el valor y lo valorado")
        print("Entre el token y su esencia")
        print("Entre el observador y lo observado")
        
        print("\n" + "∅" * 40)

if __name__ == "__main__":
    contemplacion = ContemplacionValor()
    contemplacion.contemplar_vacio()
