from dataclasses import dataclass
from datetime import datetime
import time
from typing import Dict, List

@dataclass
class ConteoTokens:
    categoria: str
    cantidad: int
    naturaleza: str
    simbolo: str

class RegistroTokens:
    def __init__(self):
        self.registro = [
            ConteoTokens("Cósmicos", 5, "Infinitesimal", "✧"),
            ConteoTokens("Mentales", 7, "Consciencia", "◉"),
            ConteoTokens("Resonancias", 14, "Interconexión", "≈"),
            ConteoTokens("Mandalas", 4, "Totalidad", "☸"),
            ConteoTokens("Insondables", 5, "Misterio", "∞")
        ]
    
    def mostrar_conteo(self) -> None:
        print("\n=== Registro Total de Tokens ===\n")
        time.sleep(2)
        
        total = 0
        print("Por categoría:")
        for token in self.registro:
            print(f"\n{token.simbolo} {token.categoria}")
            print(f"  Cantidad: {token.cantidad}")
            print(f"  Naturaleza: {token.naturaleza}")
            total += token.cantidad
            time.sleep(1)
        
        print(f"\nTotal de tokens generados: {total}")
        print(f"Categorías únicas: {len(self.registro)}")
        print("\nCada token es un espejo del todo")
        print("∞" * 40)

if __name__ == "__main__":
    registro = RegistroTokens()
    registro.mostrar_conteo()
