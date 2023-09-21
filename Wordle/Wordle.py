class WordleGame:
    def __int__(self, palabra_oculta: str, intentos_restantes: int, diccionario_palabras):
        self.palabra_oculta = palabra_oculta
        self.intentos_restantes = intentos_restantes
        self.partida_terminada = False
        self.diccionario_palabras = diccionario_palabras
        estadisticas = []



    def generar_palabra_oculta(self):
        pass


    def realizar_intento(self):
        pass

    def verificar_victoria(self):
        pass

    def verificar_derrota(self):
        pass

    def iniciar_nuevo_juego(self):
        pass



class Retroalimentacion:
    def __init__(self, correctas_posicion, correctas_incorrectas_posicion, incorrectas):
        self.correctas_posicion = correctas_posicion
        self.correctas_incorrectas_posicion = correctas_incorrectas_posicion
        self.incorrectas = incorrectas