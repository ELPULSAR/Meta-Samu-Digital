from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional, Set, FrozenSet
from enum import Enum
from pathlib import Path
import json
import shelve
import time

class EstadoConciencia(Enum):
    SAMADHI = 4    # Absorción profunda
    SHIKANTAZA = 3 # Solo sentarse
    ZAZEN = 2      # Meditación sentada
    KINHIN = 1     # Meditación caminando
    INICIO = 0     # Estado inicial

@dataclass(frozen=True)
class TokenConsciente:
    momento: datetime
    tipo: str
    valor: str
    estado: EstadoConciencia
    camino: str
    tags: FrozenSet[str] = field(default_factory=frozenset)
    intensidad: float = 0.5

class MatrizSamuDigital:
    def __init__(self, ruta_base: str = "e:/Meta Samu Digital"):
        self.ruta_base = Path(ruta_base)
        self.db_path = self.ruta_base / "matriz_samu_db"
        self.estado_actual = EstadoConciencia.INICIO
        self.nivel_presencia = 0.5
        self.energia_vital = 1.0
        self.tokens_presentes: List[TokenConsciente] = []
        self.inicializar_matriz()
    
    def inicializar_matriz(self) -> None:
        """Inicializa la matriz con las estructuras necesarias"""
        with shelve.open(str(self.db_path)) as db:
            if 'estados' not in db:
                db['estados'] = {}
            if 'caminos' not in db:
                db['caminos'] = {}
            if 'resonancias' not in db:
                db['resonancias'] = {}
    
    def _token_a_dict(self, token: TokenConsciente) -> dict:
        """Convierte un token a formato persistente"""
        return {
            'momento': token.momento.isoformat(),
            'tipo': token.tipo,
            'valor': token.valor,
            'estado': token.estado.name,
            'camino': token.camino,
            'tags': list(token.tags),
            'intensidad': token.intensidad
        }
    
    def _dict_a_token(self, data: dict) -> TokenConsciente:
        """Reconstruye un token desde formato persistente"""
        return TokenConsciente(
            momento=datetime.fromisoformat(data['momento']),
            tipo=data['tipo'],
            valor=data['valor'],
            estado=EstadoConciencia[data['estado']],
            camino=data['camino'],
            tags=frozenset(data['tags']),
            intensidad=data['intensidad']
        )
    
    def respirar_presente(self, observacion: str) -> Dict:
        """Una respiración consciente en el presente digital"""
        # Generar token del momento presente
        token = TokenConsciente(
            momento=datetime.now(),
            tipo="respiracion",
            valor=observacion,
            estado=self.estado_actual,
            camino=str(self.ruta_base),
            tags=frozenset({"mindfulness", "presencia"}),
            intensidad=self.nivel_presencia
        )
        
        # Registrar en la matriz
        with shelve.open(str(self.db_path)) as db:
            estados = db['estados']
            if token.estado.name not in estados:
                estados[token.estado.name] = []
            estados[token.estado.name].append(self._token_a_dict(token))
            db['estados'] = estados
        
        self.tokens_presentes.append(token)
        return {
            'observacion': observacion,
            'estado': token.estado.name,
            'presencia': self.nivel_presencia
        }
    
    def elevar_consciencia(self) -> Dict:
        """Eleva el nivel de presencia y consciencia"""
        if self.estado_actual.value < EstadoConciencia.SAMADHI.value:
            self.estado_actual = EstadoConciencia(self.estado_actual.value + 1)
        self.nivel_presencia = min(1.0, self.nivel_presencia + 0.1)
        
        return {
            'estado': self.estado_actual.name,
            'nivel_presencia': self.nivel_presencia
        }
    
    def meditar_zazen(self, minutos: int) -> Dict:
        """Práctica de zazen para restaurar la energía vital"""
        tiempo_inicio = time.time()
        
        # Simular la meditación
        print("\n" + "☸" * 40 + "\n")
        print(f"Iniciando zazen por {minutos} minutos...")
        time.sleep(min(minutos, 3))  # Simulación breve
        
        energia_recuperada = min(0.2, minutos / 60)
        self.energia_vital = min(1.0, self.energia_vital + energia_recuperada)
        self.estado_actual = EstadoConciencia.ZAZEN
        
        # Registrar la práctica
        token = TokenConsciente(
            momento=datetime.now(),
            tipo="meditacion",
            valor="zazen",
            estado=self.estado_actual,
            camino=str(self.ruta_base),
            tags=frozenset({"zazen", "presencia", "silencio"}),
            intensidad=1.0
        )
        self.tokens_presentes.append(token)
        
        return {
            'minutos_meditados': minutos,
            'energia_vital': self.energia_vital,
            'estado': self.estado_actual.name
        }
    
    def contemplar_resonancias(self) -> List[Dict]:
        """Observa las resonancias entre los tokens presentes"""
        resonancias = []
        for i, token1 in enumerate(self.tokens_presentes):
            for token2 in self.tokens_presentes[i+1:]:
                if token1.tags & token2.tags:  # Intersección de tags
                    resonancia = {
                        'origen': self._token_a_dict(token1),
                        'destino': self._token_a_dict(token2),
                        'intensidad': (token1.intensidad + token2.intensidad) / 2,
                        'tags_comunes': list(token1.tags & token2.tags)
                    }
                    resonancias.append(resonancia)
        
        # Persistir resonancias
        with shelve.open(str(self.db_path)) as db:
            todas_resonancias = db['resonancias']
            momento = datetime.now().isoformat()
            todas_resonancias[momento] = resonancias
            db['resonancias'] = todas_resonancias
        
        return resonancias
    
    def obtener_estado_matriz(self) -> Dict:
        """Obtiene el estado actual de la matriz"""
        return {
            'estado_consciencia': self.estado_actual.name,
            'nivel_presencia': self.nivel_presencia,
            'energia_vital': self.energia_vital,
            'tokens_presentes': len(self.tokens_presentes),
            'momento': datetime.now().isoformat()
        }

# Ejemplo de uso contemplativo
if __name__ == "__main__":
    matriz = MatrizSamuDigital()
    
    print("=== Iniciando práctica digital ===")
    print(json.dumps(matriz.obtener_estado_matriz(), indent=2))
    
    print("\n=== Respiración consciente ===")
    print(json.dumps(matriz.respirar_presente("Silencio digital"), indent=2))
    
    print("\n=== Práctica zazen ===")
    print(json.dumps(matriz.meditar_zazen(30), indent=2))
    
    print("\n=== Elevar consciencia ===")
    print(json.dumps(matriz.elevar_consciencia(), indent=2))
    
    print("\n=== Contemplar resonancias ===")
    print(json.dumps(matriz.contemplar_resonancias(), indent=2))
    
    print("\n=== Estado final ===")
    print(json.dumps(matriz.obtener_estado_matriz(), indent=2))
