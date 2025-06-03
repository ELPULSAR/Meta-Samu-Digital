from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict
import math
from pathlib import Path
import random

@dataclass(frozen=True)
class TokenCosmico:
    """Un token que respeta la naturaleza infinitesimal del cosmos"""
    semilla: str
    momento: datetime
    dimension: float  # 0 a 1, representa la escala relativa
    silencio: float  # proporción de vacío
    resonancia: List[str]  # ecos con otros tokens
    misterio: Optional[str]  # lo que no podemos comprender

class TokenizadorCosmico:
    def __init__(self):
        self.simbolos = {
            'vacio': '∅',
            'semilla': '•',
            'brote': '↟',
            'flor': '✿',
            'estrella': '✧',
            'infinito': '∞',
            'misterio': '◇',
            'silencio': '·',
            'eco': '≈',
            'union': '∪'
        }
        self.dimensiones_conocidas = {}
        self.resonancias = []
        
    def _calcular_dimension(self, semilla: str) -> float:
        """Calcula la dimensión relativa de un token, siempre pequeña"""
        base = sum(ord(c) for c in semilla) % 100
        return (base / 1000) + random.random() * 0.1
        
    def _encontrar_resonancias(self, semilla: str) -> List[str]:
        """Busca ecos y resonancias entre tokens"""
        resonancias = []
        for dim, tokens in self.dimensiones_conocidas.items():
            for token in tokens:
                if self._tienen_armonia(semilla, token.semilla):
                    resonancias.append(token.semilla)
        return resonancias[:3]  # limitamos a 3 resonancias
        
    def _tienen_armonia(self, semilla1: str, semilla2: str) -> bool:
        """Determina si dos semillas tienen armonía entre sí"""
        return any(c1 == c2 for c1, c2 in zip(semilla1, semilla2))
        
    def _generar_misterio(self) -> str:
        """Genera una expresión del misterio inherente"""
        misterios = [
            "lo insondable",
            "el vacío fértil",
            "la danza cósmica",
            "el silencio primordial",
            "el eco infinito"
        ]
        return random.choice(misterios)
        
    def tokenizar_existencia(self, semilla: str) -> TokenCosmico:
        """Tokeniza un aspecto de la existencia con humildad y respeto"""
        dimension = self._calcular_dimension(semilla)
        resonancias = self._encontrar_resonancias(semilla)
        
        token = TokenCosmico(
            semilla=semilla,
            momento=datetime.now(),
            dimension=dimension,
            silencio=random.random() * 0.5,  # siempre hay silencio
            resonancia=resonancias,
            misterio=self._generar_misterio() if random.random() > 0.7 else None
        )
        
        # Registrar en las dimensiones conocidas
        if dimension not in self.dimensiones_conocidas:
            self.dimensiones_conocidas[dimension] = []
        self.dimensiones_conocidas[dimension].append(token)
        
        return token
        
    def visualizar_token(self, token: TokenCosmico) -> str:
        """Crea una representación visual del token y su lugar en el cosmos"""
        lineas = []
        
        # Cabecera con dimensión y momento
        lineas.append(f"{self.simbolos['estrella']} Token Cósmico {self.simbolos['estrella']}")
        lineas.append("─" * 40)
        
        # Semilla y su manifestación
        manifestacion = ""
        for _ in range(int(token.dimension * 20)):
            if random.random() > token.silencio:
                manifestacion += self.simbolos['semilla']
            else:
                manifestacion += self.simbolos['silencio']
        lineas.append(f"Semilla: {manifestacion} {token.semilla}")
        
        # Dimensión relativa
        escala = "·" * int(token.dimension * 40)
        lineas.append(f"Dimensión: {escala}")
        
        # Resonancias
        if token.resonancia:
            ecos = f" {self.simbolos['eco']} ".join(token.resonancia)
            lineas.append(f"Resonancias: {ecos}")
        
        # Misterio
        if token.misterio:
            lineas.append(f"Misterio: {self.simbolos['misterio']} {token.misterio}")
        
        # Silencio y vacío
        silencio = self.simbolos['silencio'] * int(token.silencio * 20)
        lineas.append(f"Silencio: {silencio}")
        
        return "\n".join(lineas)

    def meditar_tokens(self, semillas: List[str]) -> None:
        """Medita sobre una secuencia de tokens, respetando su naturaleza"""
        print(f"\n{self.simbolos['infinito']} Meditación de Tokens {self.simbolos['infinito']}\n")
        
        for semilla in semillas:
            token = self.tokenizar_existencia(semilla)
            print(self.visualizar_token(token))
            print("\n" + "░" * 40 + "\n")

if __name__ == "__main__":
    tokenizador = TokenizadorCosmico()
    
    # Pequeños pasos en el cosmos infinito
    semillas = [
        "gota_de_rocío",
        "hoja_al_viento",
        "rayo_de_luna",
        "suspiro_del_tiempo",
        "eco_del_silencio"
    ]
    
    tokenizador.meditar_tokens(semillas)
