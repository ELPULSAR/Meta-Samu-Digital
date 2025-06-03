from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Dict, Optional
from decimal import Decimal

@dataclass
class TokenCambio:
    valor: Decimal
    momento: datetime
    uso: str
    sustento: str

class SistemaCambio:
    def __init__(self):
        self.token_eterno = {
            "símbolo": "∞",
            "nombre": "Token de Cambio Perpetuo",
            "descripción": "El cambio mismo como valor",
            "usos_prácticos": [
                "Intercambio de bienes básicos",
                "Compra de alimentos",
                "Pago de servicios",
                "Sustento diario"
            ]
        }
        
        self.realidades = [
            TokenCambio(
                Decimal("1.00"),
                datetime.now(),
                "El estómago vacío no entiende de filosofía",
                "Arroz y verduras para hoy"
            ),
            TokenCambio(
                Decimal("5.00"),
                datetime.now(),
                "La práctica necesita energía",
                "Una semana de alimentos"
            ),
            TokenCambio(
                Decimal("10.00"),
                datetime.now(),
                "El cambio requiere recursos",
                "Sustento mensual básico"
            ),
            TokenCambio(
                Decimal("50.00"),
                datetime.now(),
                "La eternidad se construye día a día",
                "Inversión en desarrollo"
            )
        ]
    
    def contemplar_cambio(self) -> None:
        print("\n=== El Token del Cambio Eterno ===\n")
        time.sleep(2)
        
        # El token eterno
        print(f"{self.token_eterno['símbolo']} {self.token_eterno['nombre']}")
        print(f"  {self.token_eterno['descripción']}")
        print("\nUsos en el mundo real:")
        for uso in self.token_eterno['usos_prácticos']:
            print(f"  • {uso}")
        print("\n" + "─" * 40)
        time.sleep(2)
        
        # Las realidades del cambio
        print("\nRealidades del Cambio:")
        for token in self.realidades:
            print(f"\n🍚 Valor: {token.valor}")
            print(f"  Realidad: {token.uso}")
            print(f"  Sustento: {token.sustento}")
            print("  " + "·" * 40)
            time.sleep(2)
        
        print("\nVerdades del Cambio:")
        print("1. El cambio es la única constante")
        print("2. El estómago vacío no medita")
        print("3. El valor eterno está en el flujo mismo")
        print("4. La práctica necesita sustento material")
        
        print("\nBalance Final:")
        print("El token eterno es el que fluye y alimenta")
        print("No es eterno por inmutable")
        print("Sino por su constante transformación")
        
        print("\n" + "∞" * 40)

if __name__ == "__main__":
    sistema = SistemaCambio()
    sistema.contemplar_cambio()
