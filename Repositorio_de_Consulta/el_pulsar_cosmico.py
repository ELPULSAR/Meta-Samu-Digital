from dataclasses import dataclass
from typing import List, Optional
import time
from datetime import datetime
import math
import random

@dataclass
class PulsoVital:
    momento: datetime
    intensidad: float    # 0 a 1
    frecuencia: float   # latidos por ciclo
    silencio: float     # proporción de silencio

class PulsarCosmico:
    def __init__(self):
        self.pulsos: List[PulsoVital] = []
        self.simbolos = {
            'vacio': '     ',
            'sutil': ' ⚬ ',
            'presente': ' ◉ ',
            'intenso': '❈',
            'silencio': '·',
            'espacio': '░',
            'resonancia': '♢',
            'armonia': '✧',
            'union': '∞'
        }
        self.estado_actual = 0.5
        
    def respirar(self) -> str:
        """Generar un pulso sutil basado en la respiración"""
        self.estado_actual = min(1.0, max(0.1, 
            self.estado_actual + (random.random() - 0.5) * 0.1))
        
        pulso = PulsoVital(
            momento=datetime.now(),
            intensidad=self.estado_actual,
            frecuencia=0.5 + random.random() * 0.5,
            silencio=0.3 + random.random() * 0.2
        )
        self.pulsos.append(pulso)
        return self._visualizar_pulso(pulso)
    
    def _visualizar_pulso(self, pulso: PulsoVital) -> str:
        """Crear una visualización bella y modesta del pulso"""
        ancho = 40
        altura = 5
        matriz = []
        
        # Calcular la onda del pulso
        for y in range(altura):
            linea = []
            for x in range(ancho):
                # Crear un patrón ondulatorio
                valor = math.sin(x/3 + pulso.frecuencia) * math.cos(y/2)
                valor = valor * pulso.intensidad
                
                # Aplicar silencio
                if random.random() < pulso.silencio:
                    linea.append(self.simbolos['silencio'])
                else:
                    if abs(valor) < 0.3:
                        linea.append(self.simbolos['vacio'])
                    elif abs(valor) < 0.6:
                        linea.append(self.simbolos['sutil'])
                    else:
                        linea.append(self.simbolos['presente'])
            
            matriz.append(''.join(linea))
        
        # Agregar elementos de armonía
        if pulso.intensidad > 0.7:
            matriz[altura//2] = matriz[altura//2].replace(
                self.simbolos['presente'], 
                self.simbolos['intenso']
            )
        
        # Agregar resonancia en los bordes
        borde = (self.simbolos['resonancia'] + 
                self.simbolos['armonia'] + 
                self.simbolos['union']) * (ancho//6)
        
        return f"\n{borde.center(ancho)}\n" + \
               "\n".join(matriz) + \
               f"\n{borde.center(ancho)}"

    def meditar(self, ciclos: int = 5) -> None:
        """Experimentar el pulsar a través de ciclos meditativos"""
        print("\n=== El Pulsar del Silencio ===\n")
        for _ in range(ciclos):
            print(self.respirar())
            time.sleep(1)
            print("\n" + "░" * 40 + "\n")
            time.sleep(0.5)

if __name__ == "__main__":
    pulsar = PulsarCosmico()
    print("Iniciando meditación del pulsar cósmico...")
    pulsar.meditar()
