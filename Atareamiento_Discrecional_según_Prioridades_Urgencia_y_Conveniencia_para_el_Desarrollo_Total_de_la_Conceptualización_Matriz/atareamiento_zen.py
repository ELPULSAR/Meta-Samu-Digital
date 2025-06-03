from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import json

class Prioridad(Enum):
    URGENTE = 4
    ALTA = 3
    MEDIA = 2
    BAJA = 1
    NO_URGENTE = 0

@dataclass
class Tarea:
    nombre: str
    descripcion: str
    prioridad: Prioridad
    energia_requerida: float  # 0 a 1
    tiempo_estimado: int     # minutos
    estado_mindful: float    # 0 a 1, nivel de atención requerido
    fecha_creacion: datetime
    completada: bool = False
    
class AtareamientoMindful:
    def __init__(self):
        self.tareas: List[Tarea] = []
        self.energia_actual: float = 1.0
        self.nivel_mindfulness: float = 0.5
        self.historial_completadas: List[Dict] = []
        
    def agregar_tarea(self, 
                     nombre: str, 
                     descripcion: str, 
                     prioridad: Prioridad,
                     energia: float,
                     tiempo: int,
                     mindfulness: float) -> Tarea:
        """Agregar nueva tarea con consciencia plena"""
        tarea = Tarea(
            nombre=nombre,
            descripcion=descripcion,
            prioridad=prioridad,
            energia_requerida=min(1.0, max(0.0, energia)),
            tiempo_estimado=tiempo,
            estado_mindful=min(1.0, max(0.0, mindfulness)),
            fecha_creacion=datetime.now()
        )
        self.tareas.append(tarea)
        return tarea
    
    def evaluar_momento_presente(self) -> List[Tarea]:
        """
        Evaluar tareas según el estado presente (Shikantaza - 只管打坐)
        Considera energía actual y nivel de mindfulness
        """
        tareas_posibles = []
        for tarea in self.tareas:
            if not tarea.completada:
                if (tarea.energia_requerida <= self.energia_actual and 
                    tarea.estado_mindful <= self.nivel_mindfulness):
                    tareas_posibles.append(tarea)
        
        return sorted(
            tareas_posibles,
            key=lambda t: (t.prioridad.value, -t.energia_requerida),
            reverse=True
        )
    
    def completar_tarea(self, nombre_tarea: str) -> Dict:
        """Completar tarea con atención plena"""
        for tarea in self.tareas:
            if tarea.nombre == nombre_tarea and not tarea.completada:
                tarea.completada = True
                self.energia_actual = max(0.1, self.energia_actual - tarea.energia_requerida * 0.5)
                self.nivel_mindfulness = min(1.0, self.nivel_mindfulness + 0.1)
                
                registro = {
                    'tarea': tarea.nombre,
                    'momento': datetime.now().isoformat(),
                    'energia_restante': self.energia_actual,
                    'mindfulness': self.nivel_mindfulness
                }
                self.historial_completadas.append(registro)
                return registro
        return {'error': 'Tarea no encontrada o ya completada'}
    
    def meditar(self, minutos: int) -> Dict:
        """
        Práctica de meditación para restaurar energía y mindfulness
        Basado en Zazen (坐禅)
        """
        energia_recuperada = min(0.2, minutos / 60)
        mindful_incremento = min(0.15, minutos / 45)
        
        self.energia_actual = min(1.0, self.energia_actual + energia_recuperada)
        self.nivel_mindfulness = min(1.0, self.nivel_mindfulness + mindful_incremento)
        
        return {
            'minutos_meditados': minutos,
            'energia_actual': self.energia_actual,
            'mindfulness_actual': self.nivel_mindfulness
        }
    
    def obtener_estado_actual(self) -> Dict:
        """Observar el estado presente del sistema"""
        tareas_pendientes = [t for t in self.tareas if not t.completada]
        tareas_completadas = [t for t in self.tareas if t.completada]
        
        return {
            'energia_actual': self.energia_actual,
            'nivel_mindfulness': self.nivel_mindfulness,
            'tareas_pendientes': len(tareas_pendientes),
            'tareas_completadas': len(tareas_completadas),
            'proxima_sugerida': self.evaluar_momento_presente()[0].nombre if self.evaluar_momento_presente() else None
        }

# Ejemplo de uso
if __name__ == "__main__":
    sistema = AtareamientoMindful()
    
    # Agregar algunas tareas
    sistema.agregar_tarea(
        "Meditación matutina",
        "Práctica de zazen",
        Prioridad.ALTA,
        energia=0.3,
        tiempo=30,
        mindfulness=0.7
    )
    
    sistema.agregar_tarea(
        "Revisión de código",
        "Con atención plena",
        Prioridad.MEDIA,
        energia=0.5,
        tiempo=45,
        mindfulness=0.8
    )
    
    # Estado inicial
    print("=== Estado Inicial ===")
    print(json.dumps(sistema.obtener_estado_actual(), indent=2))
    
    # Meditar para prepararse
    print("\n=== Después de Meditar ===")
    print(json.dumps(sistema.meditar(30), indent=2))
    
    # Completar una tarea
    print("\n=== Completar Tarea ===")
    print(json.dumps(sistema.completar_tarea("Meditación matutina"), indent=2))
    
    # Estado final
    print("\n=== Estado Final ===")
    print(json.dumps(sistema.obtener_estado_actual(), indent=2))
