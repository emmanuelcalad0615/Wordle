import enchant
from translate import Translator
import random

class Retroalimentacion:
    def __init__(self, palabra_oculta):
        self.palabra_oculta = palabra_oculta
        self.correctas_posicion = 0
        self.correctas_incorrectas_posicion = 0
        self.incorrectas = 0

    def calcular_retroalimentacion(self, palabra):
        for i in range(5):
            if palabra[i] == self.palabra_oculta[i]:
                self.correctas_posicion += 1
            elif palabra[i] in self.palabra_oculta:
                self.correctas_incorrectas_posicion += 1
            else:
                self.incorrectas += 1

class WordleGame:
    def __init__(self):
        self.palabra_oculta = None
        self.intentos_restantes = 6
        self.historial_intentos = []
        self.partida_terminada = False

    def generar_palabra_oculta(self):
        corrector_ingles = enchant.Dict("en_US")

        def obtener_palabra_ingles():
            palabra = ""
            while not palabra:
                palabra = "".join([chr(random.randint(97, 122)) for _ in range(5)])
                if not corrector_ingles.check(palabra):
                    palabra = ""
            return palabra

        def traducir_a_espanol(palabra_ingles):
            translator = Translator(to_lang="es")
            palabra_espanol = translator.translate(palabra_ingles)

            if palabra_espanol != palabra_ingles and len(palabra_espanol.split()) == 1 and len(palabra_espanol) == 5:
                return palabra_espanol
            else:
                return traducir_a_espanol(obtener_palabra_ingles())

        self.palabra_oculta = traducir_a_espanol(obtener_palabra_ingles())
        return self.palabra_oculta

    def realizar_intento(self, palabra):
        if not self.partida_terminada:
            self.intentos_restantes -= 1
            retroalimentacion = Retroalimentacion(self.palabra_oculta)
            retroalimentacion.calcular_retroalimentacion(palabra)
            self.historial_intentos.append((palabra, retroalimentacion))
            if retroalimentacion.correctas_posicion == 5:
                self.partida_terminada = True
            elif self.intentos_restantes == 0:
                self.partida_terminada = True

    def verificar_victoria(self):
        return self.partida_terminada and self.historial_intentos[-1][1].correctas_posicion == 5

    def verificar_derrota(self):
        return self.partida_terminada and self.intentos_restantes == 0

    def iniciar_nueva_partida(self):
        self.palabra_oculta = self.generar_palabra_oculta()
        self.intentos_restantes = 6
        self.historial_intentos = []
        self.partida_terminada = False



if __name__ == "__main__":
    juego = WordleGame()
    juego.generar_palabra_oculta()
    while not juego.partida_terminada:
        palabra = input("Ingresa tu intento (una palabra de 5 letras): ").strip()
        if len(palabra) != 5:
            print("La palabra debe tener exactamente 5 letras.")
            continue
        juego.realizar_intento(palabra)
        retroalimentacion = juego.historial_intentos[-1][1]
        palabra_con_aciertos = []
        for i in range(5):
            if palabra[i] == juego.palabra_oculta[i]:
                palabra_con_aciertos.append(palabra[i])
            else:
                palabra_con_aciertos.append("-")
        palabra_con_aciertos = "".join(palabra_con_aciertos)
        print(f"Intento: {palabra} - Retroalimentación: {retroalimentacion.correctas_incorrectas_posicion} correctas en posición incorrecta, "
              f"{retroalimentacion.incorrectas} incorrectas. Palabra con aciertos: {palabra_con_aciertos}")
        if juego.verificar_victoria():
            print("¡Has ganado!")
        elif juego.verificar_derrota():
            print(f"Has perdido. La palabra oculta era: {juego.palabra_oculta}")
            break

