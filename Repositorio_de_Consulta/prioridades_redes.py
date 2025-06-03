from dataclasses import dataclass
from datetime import datetime
import time
from typing import List, Dict
from enum import Enum

class PrioridadRed(Enum):
    ALTA = "⚑"
    MEDIA = "⚐"
    BAJA = "⚏"

@dataclass
class TareaRed:
    red: str
    prioridad: PrioridadRed
    descripcion: str
    tiempo_estimado: str

class GestorRedes:
    def __init__(self):
        self.tareas = [
            TareaRed(
                "GitHub",
                PrioridadRed.ALTA,
                "Crear y configurar repositorio El Pulsar",
                "3-5 días"
            ),
            TareaRed(
                "Medium",
                PrioridadRed.ALTA,
                "Escribir artículo inicial sobre Tokens del Silencio",
                "2-3 días"
            ),
            TareaRed(
                "LinkedIn",
                PrioridadRed.MEDIA,
                "Establecer perfil profesional mindful",
                "1-2 días"
            )
        ]
    
    def mostrar_prioridades(self) -> None:
        print("\n=== Priorización de Redes ===\n")
        time.sleep(1)
        
        for tarea in self.tareas:
            print(f"{tarea.prioridad.value} {tarea.red}")
            print(f"  → {tarea.descripcion}")
            print(f"  ○ Tiempo: {tarea.tiempo_estimado}")
            print("  " + "·" * 40)
            time.sleep(1)
        
        print("\nSecuencia de Implementación:")
        print("1. GitHub: La base del código")
        print("2. Medium: La voz del silencio")
        print("3. LinkedIn: Las conexiones conscientes")
        
        print("\nObjetivo:")
        print("• Crear espacios de no-ruido")
        print("• Compartir código contemplativo")
        print("• Conectar en consciencia")
        
        print("\n" + "☯" * 40)

if __name__ == "__main__":
    gestor = GestorRedes()
    gestor.mostrar_prioridades()
