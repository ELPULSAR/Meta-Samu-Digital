from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Set
import json
import os
from pathlib import Path
import shelve
from collections import defaultdict

@dataclass(frozen=True)
class IndiceToken:
    momento: datetime
    camino: str
    tipo: str
    valor: str
    tags: frozenset = field(default_factory=frozenset)
    intensidad: float = 0.0

class IndicePulsar:
    def __init__(self, ruta_base: str = "e:/Meta Samu Digital"):
        self.ruta_base = Path(ruta_base)
        self.db_path = self.ruta_base / "Repositorio_de_Consulta/El_Pulsar.Tokenizacion_de_Navegación_Web/pulsar_db"
        self.indices_temporales: Dict[str, List[IndiceToken]] = defaultdict(list)
        self.cargar_indices()

    def _normalizar_camino(self, camino: str) -> str:
        """Normaliza el camino hasta 'El_Pulsar'"""
        try:
            partes = Path(camino).parts
            idx = partes.index("El_Pulsar.Tokenizacion_de_Navegación_Web")
            return str(Path(*partes[:idx+1]))
        except ValueError:
            return camino

    def respirar_token(self, token: IndiceToken) -> None:
        """Registra un nuevo token en el índice con consciencia"""
        camino_normalizado = self._normalizar_camino(token.camino)
        
        # Indexar por momento (año-mes-día)
        fecha_key = token.momento.strftime("%Y-%m-%d")
        self.indices_temporales[fecha_key].append(token)
        
        # Persistir en la base de datos
        with shelve.open(str(self.db_path)) as db:
            # Índice temporal
            db[f"temporal_{fecha_key}"] = self.indices_temporales[fecha_key]
            
            # Índice por tipo
            tipos = db.get("tipos", defaultdict(list))
            tipos[token.tipo].append(token)
            db["tipos"] = tipos
            
            # Índice por camino
            caminos = db.get("caminos", defaultdict(list))
            caminos[camino_normalizado].append(token)
            db["caminos"] = caminos
            
            # Índice por intensidad
            intensidades = db.get("intensidades", defaultdict(list))
            nivel = round(token.intensidad * 10) / 10  # Redondear a décimas
            intensidades[nivel].append(token)
            db["intensidades"] = intensidades

    def observar_presente(self, 
                         momento: Optional[datetime] = None,
                         tipo: Optional[str] = None,
                         camino: Optional[str] = None,
                         intensidad_min: float = 0.0) -> List[IndiceToken]:
        """Recupera tokens según los parámetros de observación presente"""
        tokens = []
        
        with shelve.open(str(self.db_path)) as db:
            if momento:
                fecha_key = momento.strftime("%Y-%m-%d")
                if fecha_key in self.indices_temporales:
                    tokens.extend(self.indices_temporales[fecha_key])
            
            if tipo and "tipos" in db:
                tipos = db["tipos"]
                if tipo in tipos:
                    tokens.extend(tipos[tipo])
            
            if camino and "caminos" in db:
                caminos = db["caminos"]
                camino_norm = self._normalizar_camino(camino)
                if camino_norm in caminos:
                    tokens.extend(caminos[camino_norm])
            
            if intensidad_min > 0 and "intensidades" in db:
                intensidades = db["intensidades"]
                for nivel in intensidades:
                    if nivel >= intensidad_min:
                        tokens.extend(intensidades[nivel])
        
        # Eliminar duplicados manteniendo el orden
        tokens_unicos = []
        visto = set()
        for token in tokens:
            token_key = (token.momento, token.camino, token.tipo, token.valor)
            if token_key not in visto:
                visto.add(token_key)
                tokens_unicos.append(token)
        
        return sorted(tokens_unicos, 
                     key=lambda t: t.momento,
                     reverse=True)

    def cargar_indices(self) -> None:
        """Carga los índices existentes en memoria"""
        if os.path.exists(str(self.db_path) + ".db"):
            with shelve.open(str(self.db_path)) as db:
                for key in db:
                    if key.startswith("temporal_"):
                        fecha = key.replace("temporal_", "")
                        self.indices_temporales[fecha] = db[key]

    def visualizar_indice(self, tokens: List[IndiceToken]) -> str:
        """Crea una visualización zen de los tokens indexados"""
        if not tokens:
            return "∅ Vacío presente ∅"
        
        resultado = []
        resultado.append("◈ Índice del Pulsar ◈")
        resultado.append("─" * 40)
        
        for token in tokens:
            intensidad_visual = "○" * int(token.intensidad * 10)
            resultado.append(f"Momento: {token.momento.strftime('%H:%M:%S')}")
            resultado.append(f"Camino: ...{token.camino[-30:]}")
            resultado.append(f"Tipo: {token.tipo}")
            resultado.append(f"Intensidad: {intensidad_visual}")
            resultado.append("─" * 40)
        
        return "\n".join(resultado)

# Ejemplo de uso
if __name__ == "__main__":
    indice = IndicePulsar()
    
    # Crear algunos tokens de ejemplo
    token1 = IndiceToken(
        momento=datetime.now(),
        camino="e:/Meta Samu Digital/Repositorio_de_Consulta/El_Pulsar.Tokenizacion_de_Navegación_Web/ejemplo1",
        tipo="meditacion",
        valor="presente1",
        tags=frozenset({"zen", "mindfulness"}),
        intensidad=0.8
    )
    
    token2 = IndiceToken(
        momento=datetime.now(),
        camino="e:/Meta Samu Digital/Repositorio_de_Consulta/El_Pulsar.Tokenizacion_de_Navegación_Web/ejemplo2",
        tipo="contemplacion",
        valor="presente2",
        tags=frozenset({"silencio", "presencia"}),
        intensidad=0.6
    )
    
    # Respirar los tokens
    indice.respirar_token(token1)
    indice.respirar_token(token2)
    
    # Observar el presente
    tokens_presentes = indice.observar_presente(
        momento=datetime.now(),
        intensidad_min=0.5
    )
    
    # Visualizar
    print(indice.visualizar_indice(tokens_presentes))
