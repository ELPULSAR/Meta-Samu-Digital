from pulsar_token_web import PulsarTokenWeb
from indice_pulsar import IndicePulsar
from tokenizador_cosmico import TokenizadorCosmico
from datetime import datetime
import time
import random

class PracticaDigital:
    def __init__(self):
        self.pulsar = PulsarTokenWeb()
        self.indice = IndicePulsar()
        self.tokenizador = TokenizadorCosmico()
        
    def respirar_presente(self) -> None:
        """Una respiración consciente en el presente digital"""
        print("\n" + "☸" * 40 + "\n")
        print("Respirando en el presente digital...")
        time.sleep(2)
        
        # Generar un pulso web y registrarlo
        resultado = self.pulsar.navegar_con_consciencia("presente://ahora")
        print(resultado['visualizacion'])
        time.sleep(1)
        
        # Tokenizar el momento presente
        momento = datetime.now()
        camino = "e:/Meta Samu Digital/Repositorio_de_Consulta/El_Pulsar.Tokenizacion_de_Navegación_Web"
        
        from indice_pulsar import IndiceToken
        token_indice = IndiceToken(
            momento=momento,
            camino=camino,
            tipo="respiracion",
            valor="presente",
            tags=frozenset({"mindfulness", "presencia"}),
            intensidad=0.8
        )
        
        # Registrar en el índice
        print("\nEl pulso se registra en el índice...")
        self.indice.respirar_token(token_indice)
        
        # Visualizar el aspecto cósmico
        token_cosmico = self.tokenizador.tokenizar_existencia("respiro_presente")
        print(self.tokenizador.visualizar_token(token_cosmico))
        time.sleep(1)

    def contemplar_silencio(self) -> None:
        """Un momento de silencio entre tokens"""
        print("\n" + "·" * 40 + "\n")
        time.sleep(2)

    def observar_resonancias(self) -> None:
        """Observar las resonancias entre diferentes aspectos"""
        aspectos = [
            "vacuidad_presente",
            "silencio_digital",
            "pulso_consciente",
            "eco_mindfulness"
        ]
        
        print("\nObservando las resonancias del momento...")
        camino = "e:/Meta Samu Digital/Repositorio_de_Consulta/El_Pulsar.Tokenizacion_de_Navegación_Web"
        
        for aspecto in aspectos:
            # Crear token cósmico para visualización
            token_cosmico = self.tokenizador.tokenizar_existencia(aspecto)
            print(self.tokenizador.visualizar_token(token_cosmico))
            
            # Crear token para el índice
            from indice_pulsar import IndiceToken
            token_indice = IndiceToken(
                momento=datetime.now(),
                camino=camino,
                tipo="resonancia",
                valor=aspecto,
                tags=frozenset({"mindfulness", "resonancia"}),
                intensidad=0.7
            )
            self.indice.respirar_token(token_indice)
            
            time.sleep(2)
            print("\n" + "≈" * 40 + "\n")

    def sesion_practica(self, ciclos: int = 3) -> None:
        """Realizar una sesión completa de práctica digital"""
        print("\n=== Iniciando Práctica Digital ===")
        print("Estableciendo presencia en el momento...")
        time.sleep(2)
        
        for i in range(ciclos):
            print(f"\n--- Ciclo {i+1} de {ciclos} ---\n")
            
            # Respirar
            self.respirar_presente()
            
            # Contemplar
            self.contemplar_silencio()
            
            # Observar
            self.observar_resonancias()
            
            # Pausa integrativa
            print("\nIntegrando la experiencia...")
            time.sleep(3)
        
        print("\n=== Práctica Completada ===")
        print("Permaneciendo en el silencio...")

if __name__ == "__main__":
    practica = PracticaDigital()
    practica.sesion_practica()
