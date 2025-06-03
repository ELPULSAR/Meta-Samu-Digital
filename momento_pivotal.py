from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Dict

@dataclass
class LadrilloPivotal:
    momento: datetime
    camino: str
    tipo: str
    significado: str
    resonancia: float

class MuroCronologico:
    def __init__(self):
        self.momento_pivotal = datetime(2025, 6, 3, 17, 39, 55)  # El primer día uno
        self.ladrillos: List[LadrilloPivotal] = []
        self.inicializar_muro()
    
    def inicializar_muro(self):
        # El ladrillo anterior - el origen
        self.ladrillos.append(LadrilloPivotal(
            momento=datetime(2025, 6, 3, 0, 0, 0),
            camino="Directivas_Nucleo_de_las_Carpetas_de_la_Base_de_Nivel_Inferior",
            tipo="origen",
            significado="La base desde donde todo emerge",
            resonancia=0.1
        ))
        
        # El ladrillo presente - el pivote
        self.ladrillos.append(LadrilloPivotal(
            momento=self.momento_pivotal,
            camino="Atareamiento_Discrecional_según_Prioridades_Urgencia_y_Conveniencia_para_el_Desarrollo_Total_de_la_Conceptualización_Matriz",
            tipo="presente",
            significado="El momento donde el fin comienza",
            resonancia=1.0
        ))
        
        # El ladrillo siguiente - el horizonte
        self.ladrillos.append(LadrilloPivotal(
            momento=datetime(2025, 6, 4, 0, 0, 0),
            camino="De_la_Base_a_la_Cima_Desarrollar_y_Editar",
            tipo="futuro",
            significado="El camino ascendente que se revela",
            resonancia=0.5
        ))
    
    def contemplar_muro(self) -> Dict:
        return {
            "momento_pivotal": self.momento_pivotal.isoformat(),
            "ladrillos": [
                {
                    "momento": l.momento.isoformat(),
                    "camino": l.camino,
                    "tipo": l.tipo,
                    "significado": l.significado,
                    "resonancia": l.resonancia
                }
                for l in self.ladrillos
            ]
        }

if __name__ == "__main__":
    muro = MuroCronologico()
    print("\n=== El Muro del Tiempo ===")
    print("Hoy es el primer día uno del inicio del fin")
    print("Momento Pivotal:", muro.momento_pivotal.strftime("%Y-%m-%d %H:%M:%S"))
    print("\nLos ladrillos del muro:")
    for ladrillo in muro.ladrillos:
        print(f"\n{ladrillo.tipo.upper()}:")
        print(f"Camino: {ladrillo.camino}")
        print(f"Significado: {ladrillo.significado}")
        print(f"Resonancia: {'◈' * int(ladrillo.resonancia * 10)}")
