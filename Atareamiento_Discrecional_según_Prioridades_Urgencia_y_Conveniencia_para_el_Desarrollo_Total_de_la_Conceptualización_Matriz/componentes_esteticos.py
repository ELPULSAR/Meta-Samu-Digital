from dataclasses import dataclass
from typing import List, Dict, Optional
import math
import time
from datetime import datetime

class ComponenteZen:
    def __init__(self, ancho: int = 40):
        self.ancho = ancho
        self.simbolos_zen = {
            'circulo': '○',
            'circulo_lleno': '●',
            'flor': '✿',
            'hoja': '❧',
            'onda': '∿',
            'punto_zen': '・',
            'rama': '⎯',
            'espacio': '  ',
            # Nuevos símbolos para el pulsar
            'pulso': '◈',
            'pulso_lleno': '◆',
            'pulso_suave': '◇',
            'estrella': '✧',
            'estrella_llena': '✦',
            'espiral': '§',
            'infinito': '∞',
            'onda_pulso': '≈',
            'latido': '♥',
            'latido_vacio': '♡'
        }

    def pulso_cosmico(self, intensidad: float) -> str:
        """Crear una visualización del pulso cósmico"""
        ancho = self.ancho // 2
        pulsos = math.floor(intensidad * ancho)
        lineas = []
        
        # Primera línea: pulsos fuertes
        linea1 = ''.join([
            self.simbolos_zen['pulso_lleno'] if i < pulsos
            else self.simbolos_zen['pulso_suave']
            for i in range(ancho)
        ])
        
        # Segunda línea: estrellas y espirales
        linea2 = ''.join([
            self.simbolos_zen['estrella_llena'] if i % 3 == 0
            else self.simbolos_zen['espiral'] if i % 3 == 1
            else self.simbolos_zen['infinito']
            for i in range(ancho)
        ])
        
        # Tercera línea: latidos
        linea3 = ''.join([
            self.simbolos_zen['latido'] if i < pulsos
            else self.simbolos_zen['latido_vacio']
            for i in range(ancho)
        ])
        
        return '\n'.join([linea1.center(self.ancho),
                         linea2.center(self.ancho),
                         linea3.center(self.ancho)])

    def jardin_zen(self, nivel: float) -> str:
        """Crear un jardín zen visual basado en el nivel de mindfulness"""
        piedras = math.floor(nivel * 5)
        arena = self.ancho - piedras
        
        jardin = [
            self.simbolos_zen['onda'] * self.ancho,
            ''.join([
                self.simbolos_zen['circulo_lleno'] if i < piedras 
                else self.simbolos_zen['punto_zen']
                for i in range(self.ancho)
            ]),
            self.simbolos_zen['onda'] * self.ancho
        ]
        
        return '\n'.join(jardin)

    def mandala_energia(self, energia: float) -> str:
        """Crear un mandala que representa el nivel de energía"""
        niveles = math.floor(energia * 4)
        mandala = []
        
        for i in range(4):
            if i < niveles:
                linea = f"{self.simbolos_zen['flor']} {self.simbolos_zen['rama'] * 3} {self.simbolos_zen['flor']}"
            else:
                linea = f"{self.simbolos_zen['punto_zen']} {self.simbolos_zen['rama'] * 3} {self.simbolos_zen['punto_zen']}"
            mandala.append(linea.center(self.ancho))
            
        return '\n'.join(mandala)

    def barra_progreso_zen(self, valor: float, etiqueta: str) -> str:
        """Crear una barra de progreso con estética zen"""
        longitud = self.ancho - len(etiqueta) - 4
        progreso = math.floor(valor * longitud)
        
        barra = f"{etiqueta} [{self.simbolos_zen['hoja'] * progreso}"
        barra += f"{self.simbolos_zen['punto_zen'] * (longitud - progreso)}]"
        
        return barra

    def marco_zen(self, contenido: List[str]) -> str:
        """Crear un marco decorativo para el contenido"""
        ancho_max = max(len(linea) for linea in contenido)
        marco = []
        
        # Borde superior
        marco.append(f"╭{'─' * (ancho_max + 2)}╮")
        
        # Contenido
        for linea in contenido:
            marco.append(f"│ {linea.ljust(ancho_max)} │")
            
        # Borde inferior
        marco.append(f"╰{'─' * (ancho_max + 2)}╯")
        
        return '\n'.join(marco)

class VisualizadorTareas:
    def __init__(self):
        self.componente = ComponenteZen()
        
    def mostrar_estado_sistema(self, energia: float, mindfulness: float, tareas_pendientes: int) -> str:
        """Crear una visualización bella del estado del sistema con pulso cósmico"""
        # Pulso cósmico que representa la energía vital
        pulso = self.componente.pulso_cosmico(energia)
        """Crear una visualización bella del estado del sistema"""
        # Jardín Zen que representa el mindfulness
        jardin = self.componente.jardin_zen(mindfulness)
        
        # Mandala de energía
        mandala = self.componente.mandala_energia(energia)
        
        # Barras de progreso
        barra_energia = self.componente.barra_progreso_zen(energia, "Energía")
        barra_mind = self.componente.barra_progreso_zen(mindfulness, "Mindful")
        
        # Información de tareas
        info_tareas = f"Tareas pendientes: {tareas_pendientes}"
        
        # Unir todo en un marco zen
        visualizacion = [
            "Estado del Sistema",
            "─" * 20,
            "",
            pulso,
            "",
            jardin,
            "",
            mandala,
            "",
            barra_energia,
            barra_mind,
            "",
            info_tareas
        ]
        
        return self.componente.marco_zen(visualizacion)

def demostrar_componentes():
    """Demostración de los componentes estéticos"""
    visualizador = VisualizadorTareas()
    
    # Simular cambios en el sistema
    for i in range(5):
        energia = (i + 1) / 5
        mindfulness = min(1.0, (i + 2) / 5)
        tareas = 5 - i
        
        print("\033[2J\033[H")  # Limpiar pantalla
        print(visualizador.mostrar_estado_sistema(energia, mindfulness, tareas))
        time.sleep(2)  # Pausa para apreciar la visualización

if __name__ == "__main__":
    print("=== Demostración de Componentes Estéticos Zen ===")
    demostrar_componentes()
