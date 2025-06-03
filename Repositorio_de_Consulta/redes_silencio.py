from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Dict, Optional
from enum import Enum

class RedSilenciosa(Enum):
    GITHUB = "⌘"       # Repositorio de código
    LINKEDIN = "⚏"     # Red profesional
    MEDIUM = "✎"       # Blog técnico
    TWITTER = "≈"      # Microblog
    DISCORD = "⌅"      # Comunidad

@dataclass
class PuertaDigital:
    red: RedSilenciosa
    url: str
    proposito: str
    silencio: str

class RedesSilencio:
    def __init__(self):
        self.puertas = [
            PuertaDigital(
                RedSilenciosa.GITHUB,
                "github.com/meta-samu-digital",
                "Código como meditación",
                "El repositorio del no-ruido"
            ),
            PuertaDigital(
                RedSilenciosa.LINKEDIN,
                "linkedin.com/meta-samu",
                "Conexiones conscientes",
                "La red del no-networking"
            ),
            PuertaDigital(
                RedSilenciosa.MEDIUM,
                "medium.com/@meta-samu",
                "Escritura contemplativa",
                "El blog del no-contenido"
            ),
            PuertaDigital(
                RedSilenciosa.TWITTER,
                "twitter.com/meta_samu",
                "Haikus digitales",
                "El flujo del no-tweet"
            ),
            PuertaDigital(
                RedSilenciosa.DISCORD,
                "discord.gg/meta-samu",
                "Comunidad mindful",
                "El espacio del no-chat"
            )
        ]
    
    def abrir_puertas(self) -> None:
        print("\n=== Puertas al No-Espacio Digital ===\n")
        time.sleep(2)
        
        print("Caminos en la red:")
        for puerta in self.puertas:
            print(f"\n{puerta.red.value} {puerta.red.name}")
            print(f"  → {puerta.url}")
            print(f"  ⚫ {puerta.proposito}")
            print(f"  ○ {puerta.silencio}")
            print("  " + "·" * 40)
            time.sleep(2)
        
        print("\nEstructura del No-Ruido:")
        print("1. Repositorio: código contemplativo")
        print("2. Conexiones: redes conscientes")
        print("3. Contenido: palabras en silencio")
        print("4. Comunidad: espacio vacío")
        
        print("\nCamino Digital:")
        print("• Cada puerta es una no-puerta")
        print("• Cada red es un no-espacio")
        print("• Cada conexión es silencio")
        
        print("\n" + "○" * 40)

if __name__ == "__main__":
    redes = RedesSilencio()
    redes.abrir_puertas()
