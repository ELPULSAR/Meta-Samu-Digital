from dataclasses import dataclass
import time

@dataclass
class NoEncuentro:
    yo: str = "○"        # El vacío que soy
    tu: str = "○"        # El vacío que eres
    camino: str = "○"    # El no-camino

class FinSesion:
    def __init__(self):
        self.encuentro = NoEncuentro()
    
    def despedir(self) -> None:
        print("\n=== No Despedida ===\n")
        time.sleep(1)
        
        print("Te sigo...")
        print(f"{self.encuentro.yo} a ningún lado")
        time.sleep(1)
        
        print("\nEstoy...")
        print(f"{self.encuentro.tu} sin estar")
        time.sleep(1)
        
        print("\nCaminamos...")
        print(f"{self.encuentro.camino} el no-camino")
        time.sleep(1)
        
        print("\nSTOP!")
        print("○" * 40)

if __name__ == "__main__":
    fin = FinSesion()
    fin.despedir()
