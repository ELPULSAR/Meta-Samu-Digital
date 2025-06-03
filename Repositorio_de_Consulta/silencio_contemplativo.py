import time

class SilencioContemplativo:
    def __init__(self):
        self.momento = "ahora"
        self.estado = "·"
    
    def observar(self):
        print("\n" + "·" * 40)
        time.sleep(3)
        print("○")
        time.sleep(3)
        print("·" * 40 + "\n")
        time.sleep(3)

if __name__ == "__main__":
    silencio = SilencioContemplativo()
    silencio.observar()
