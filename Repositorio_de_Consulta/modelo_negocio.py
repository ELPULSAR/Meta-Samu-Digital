from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Dict
from enum import Enum

class ModeloNegocio:
    def __init__(self):
        self.servicios = {
            "Tokenización Empresarial": {
                "valor": "Optimización de procesos y recursos",
                "precio": "Por volumen de tokens procesados",
                "beneficio": "Reducción de costos operativos"
            },
            "Certificación Digital": {
                "valor": "Autenticidad y trazabilidad",
                "precio": "Por certificado emitido",
                "beneficio": "Confianza y transparencia"
            },
            "Consultoría Mindful": {
                "valor": "Integración consciencia-negocio",
                "precio": "Por hora de consultoría",
                "beneficio": "Desarrollo sostenible"
            },
            "Sistemas de Tokens": {
                "valor": "Infraestructura tokenizada",
                "precio": "Licencia + mantenimiento",
                "beneficio": "Escalabilidad consciente"
            }
        }
    
    def presentar_modelo(self) -> None:
        print("\n=== Modelo de Negocio Consciente ===\n")
        time.sleep(2)
        
        print("Balance entre valor y sustento:")
        print("El camino del medio en la práctica empresarial")
        time.sleep(2)
        
        for servicio, detalles in self.servicios.items():
            print(f"\n⚖ {servicio}")
            print(f"  Valor: {detalles['valor']}")
            print(f"  Precio: {detalles['precio']}")
            print(f"  Beneficio: {detalles['beneficio']}")
            print("  " + "─" * 40)
            time.sleep(2)
        
        print("\nPrincipios del modelo:")
        print("1. Valor justo por servicio prestado")
        print("2. Beneficio mutuo y sostenible")
        print("3. Consciencia en la práctica comercial")
        print("4. Equilibrio entre dar y recibir")
        
        print("\n" + "⚖" * 40)

if __name__ == "__main__":
    modelo = ModeloNegocio()
    modelo.presentar_modelo()
