from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Optional
import math
import random
import json

@dataclass
class TokenPulsar:
    momento: datetime
    tipo: str
    valor: str
    intensidad: float
    frecuencia: float
    silencio: float

class PulsarTokenWeb:
    def __init__(self):
        self.tokens: List[TokenPulsar] = []
        self.simbolos_web = {
            'inicio': '◎',
            'navegacion': '➢',
            'interaccion': '⚡',
            'datos': '◈',
            'conexion': '∞',
            'silencio': '·',
            'espera': '○',
            'completado': '●',
            'error': '✗',
            'exito': '✓'
        }
        self.estado_red = 1.0
        
    def pulsar_web(self, url: str, tipo_interaccion: str) -> TokenPulsar:
        """Generar un token pulsar para una interacción web"""
        intensidad = random.random() * self.estado_red
        frecuencia = 0.5 + random.random() * 0.5
        silencio = 0.2 + random.random() * 0.3
        
        token = TokenPulsar(
            momento=datetime.now(),
            tipo=tipo_interaccion,
            valor=url,
            intensidad=intensidad,
            frecuencia=frecuencia,
            silencio=silencio
        )
        
        self.tokens.append(token)
        return token
    
    def visualizar_pulso_web(self, token: TokenPulsar) -> str:
        """Crear una visualización del pulso web"""
        ancho = 50
        altura = 3
        matriz = []
        
        # Patrón base del pulso
        for y in range(altura):
            linea = []
            for x in range(ancho):
                # Crear patrón ondulatorio basado en la URL
                valor = math.sin(x/4 + hash(token.valor) % 10) * \
                       math.cos(y/2 + token.frecuencia)
                valor = valor * token.intensidad
                
                if random.random() < token.silencio:
                    linea.append(self.simbolos_web['silencio'])
                else:
                    if abs(valor) < 0.3:
                        linea.append(self.simbolos_web['espera'])
                    elif abs(valor) < 0.6:
                        linea.append(self.simbolos_web[token.tipo])
                    else:
                        linea.append(self.simbolos_web['datos'])
            
            matriz.append(''.join(linea))
        
        # Agregar información del token
        info = f"{self.simbolos_web['inicio']} {token.tipo} | {token.valor[:30]}..."
        
        return (f"{info}\n" + 
                "\n".join(matriz) + 
                f"\n{self.simbolos_web['conexion'] * (ancho//2)}")
    
    def navegar_con_consciencia(self, url: str) -> Dict:
        """Realizar una navegación web consciente"""
        token = self.pulsar_web(url, 'navegacion')
        visualizacion = self.visualizar_pulso_web(token)
        
        return {
            'token': {
                'momento': token.momento.isoformat(),
                'tipo': token.tipo,
                'intensidad': token.intensidad,
                'frecuencia': token.frecuencia
            },
            'visualizacion': visualizacion
        }
    
    def interactuar_con_presencia(self, url: str, accion: str) -> Dict:
        """Realizar una interacción web con presencia plena"""
        token = self.pulsar_web(url, 'interaccion')
        token.valor = f"{url}#{accion}"
        visualizacion = self.visualizar_pulso_web(token)
        
        return {
            'token': {
                'momento': token.momento.isoformat(),
                'tipo': token.tipo,
                'accion': accion,
                'intensidad': token.intensidad
            },
            'visualizacion': visualizacion
        }

    def obtener_historial_pulsos(self) -> List[Dict]:
        """Obtener el historial de pulsos web"""
        return [
            {
                'momento': t.momento.isoformat(),
                'tipo': t.tipo,
                'valor': t.valor,
                'intensidad': t.intensidad
            }
            for t in self.tokens
        ]

# Ejemplo de uso
if __name__ == "__main__":
    pulsar_web = PulsarTokenWeb()
    
    print("=== Navegación Web Consciente ===\n")
    
    # Ejemplo de navegación
    resultado = pulsar_web.navegar_con_consciencia("https://ejemplo.com/zen")
    print(resultado['visualizacion'])
    print("\n" + "░" * 50 + "\n")
    
    # Ejemplo de interacción
    resultado = pulsar_web.interactuar_con_presencia(
        "https://ejemplo.com/zen",
        "meditar"
    )
    print(resultado['visualizacion'])
    print("\n" + "░" * 50 + "\n")
    
    # Mostrar historial
    print("=== Historial de Pulsos ===")
    print(json.dumps(pulsar_web.obtener_historial_pulsos(), indent=2))
