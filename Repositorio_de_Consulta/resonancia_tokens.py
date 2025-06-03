from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Optional
from enum import Enum

class NaturalezaToken(Enum):
    NEURONAL = "⚡"    # La chispa del pensamiento
    TEMPORAL = "⧗"     # El flujo del tiempo
    ESPACIAL = "◊"     # La forma del espacio
    INFINITO = "∞"     # Lo eterno
    SILENCIO = "·"     # El vacío fértil
    MISTERIO = "✧"     # Lo insondable
    PRESENTE = "○"     # El momento actual

@dataclass
class ResonanciaCosmica:
    origen: str
    naturaleza: NaturalezaToken
    profundidad: float
    ecos: List[str]
    silencio: str

class TejedorResonancias:
    def __init__(self):
        self.tokens_base = {
            "Bólido": {
                "naturaleza": NaturalezaToken.NEURONAL,
                "profundidad": 0.7,
                "ecos": ["chispa", "destello", "impulso"]
            },
            "Caravana": {
                "naturaleza": NaturalezaToken.TEMPORAL,
                "profundidad": 0.8,
                "ecos": ["viaje", "flujo", "movimiento"]
            },
            "El_Pulsar": {
                "naturaleza": NaturalezaToken.PRESENTE,
                "profundidad": 1.0,
                "ecos": ["latido", "respiración", "ritmo"]
            },
            "Eternidad": {
                "naturaleza": NaturalezaToken.INFINITO,
                "profundidad": 0.9,
                "ecos": ["ciclo", "perpetuo", "sin_fin"]
            },
            "Gaucho": {
                "naturaleza": NaturalezaToken.ESPACIAL,
                "profundidad": 0.6,
                "ecos": ["tierra", "horizonte", "libertad"]
            },
            "Kernel": {
                "naturaleza": NaturalezaToken.MISTERIO,
                "profundidad": 0.85,
                "ecos": ["núcleo", "esencia", "origen"]
            },
            "Sistema_Zen": {
                "naturaleza": NaturalezaToken.SILENCIO,
                "profundidad": 0.95,
                "ecos": ["vacío", "presencia", "despertar"]
            }
        }
    
    def tejer_resonancia(self, token: str) -> ResonanciaCosmica:
        base = self.tokens_base[token]
        silencio = base["naturaleza"].value * int(base["profundidad"] * 10)
        return ResonanciaCosmica(
            origen=token,
            naturaleza=base["naturaleza"],
            profundidad=base["profundidad"],
            ecos=base["ecos"],
            silencio=silencio
        )
    
    def contemplar_resonancias(self) -> None:
        print("\n" + "☸" * 40 + "\n")
        print("Contemplando las resonancias del sistema...\n")
        time.sleep(2)
        
        for token in self.tokens_base.keys():
            resonancia = self.tejer_resonancia(token)
            print(f"=== {resonancia.origen} ===")
            print(f"Naturaleza: {resonancia.naturaleza.value}")
            print(f"Profundidad: {'▓' * int(resonancia.profundidad * 10)}")
            print(f"Ecos: {' ≈ '.join(resonancia.ecos)}")
            print(f"Silencio: {resonancia.silencio}")
            print("\n" + "·" * 40 + "\n")
            time.sleep(3)
        
        print("El tejido de resonancias continúa...")
        print("\n" + "∞" * 40 + "\n")

if __name__ == "__main__":
    tejedor = TejedorResonancias()
    tejedor.contemplar_resonancias()
