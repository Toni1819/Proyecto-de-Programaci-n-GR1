#1.

#2.
# Importar las librerías necesarias
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView

class AlarmaApp(App):
    def build(self):
        # Crear la interfaz gráfica
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Etiqueta para mostrar la hora actual
        self.hora_label = Label(text="Hora actual: ")
        layout.add_widget(self.hora_label)

        # Campo de entrada para la hora de la alarma
        self.hora_input = TextInput(hint_text="Ingrese la hora (HH:MM)")
        layout.add_widget(self.hora_input)

        # Selector de archivos para el sonido
        self.file_chooser = FileChooserListView(path='.')
        layout.add_widget(self.file_chooser)

        # Botón para establecer la alarma
        self.establecer_alarma_btn = Button(text="Establecer Alarma")
        self.establecer_alarma_btn.bind(on_press=self.establecer_alarma)
        layout.add_widget(self.establecer_alarma_btn)

        return layout

    def establecer_alarma(self, instance):
        # Obtener la hora ingresada por el usuario
        hora_ingresada = self.hora_input.text

        # Obtener la ruta del archivo de sonido seleccionado
        ruta_sonido = self.file_chooser.selection[0] if self.file_chooser.selection else None

        # Aquí puedes agregar la lógica para verificar la hora y reproducir el sonido de la alarma
        # Por ahora, simplemente actualizaremos la etiqueta con la hora y la ruta del sonido
        self.hora_label.text = f"Hora de la alarma: {hora_ingresada}"
        if ruta_sonido:
            print(f"Sonido seleccionado: {ruta_sonido}")
        else:
            print("No se ha seleccionado ningún sonido.")

if __name__ == '__main__':
    AlarmaApp().run()
 

#3.
def obtener_hora_alarma():
    try:
        # Obtener la hora ingresada por el usuario (formato HH:MM)
        hora_ingresada = input("Ingrese la hora de la alarma (HH:MM): ")

        # Convertir la hora ingresada a un objeto time
        hora, minutos = map(int, hora_ingresada.split(":"))
        hora_alarma = datetime.time(hour=hora, minute=minutos)

        print(f"Alarma establecida para las {hora_alarma.strftime('%H:%M')}")
        return hora_alarma
    except EOFError:
        print("No se ingresó ninguna hora. Inténtalo nuevamente.")
        return None

# Ejemplo de uso
hora_alarma_seleccionada = obtener_hora_alarma()

# Ahora puedes utilizar 'hora_alarma_seleccionada' en tu lógica para activar la alarma.

#4.
import tkinter as tk
from tkinter import filedialog

def seleccionar_sonido():
    ruta_sonido = filedialog.askopenfilename(
        initialdir="/storage/emulated/0/Sounds",  # Directorio inicial donde tienes tus sonidos
        title="Selecciona un archivo de sonido",
        filetypes=(("Archivos de audio", "*.wav *.mp3"), ("Todos los archivos", "*.*"))
    )
    if ruta_sonido:
        print(f"Sonido seleccionado: {ruta_sonido}")
        # Aquí puedes guardar la ruta del sonido en una variable o en tu lógica de alarma

root = tk.Tk()
root.title("Seleccionar Sonido")

boton_seleccionar = tk.Button(root, text="Seleccionar Sonido", command=seleccionar_sonido)
boton_seleccionar.pack(pady=10)

root.mainloop()


#5
import datetime
import time
import pygame

# Inicializar Pygame y el mixer
pygame.init()
pygame.mixer.init()

# Cargar el sonido de la alarma (reemplaza 'fondo.wav' con la ruta de tu archivo de sonido)
sonido_alarma = pygame.mixer.Sound("fondo.wav")

# Obtener la hora de la alarma (reemplaza esto con la lógica para obtener la hora ingresada por el usuario)
hora_alarma = datetime.time(hour=8, minute=30)  
# Ejemplo: alarma a las 8:30 AM

while True:
    hora_actual = datetime.datetime.now().time()

    if hora_actual.hour == hora_alarma.hour and hora_actual.minute == hora_alarma.minute:
        print("¡Es hora de la alarma!")
        sonido_alarma.play()  # Reproducir el sonido de la alarma

    # Esperar un segundo antes de verificar nuevamente
    time.sleep(1)
    
#6.
import datetime
import time
import pygame

# Inicializar Pygame y el mixer
pygame.init()
pygame.mixer.init()

# Cargar el sonido de la alarma (reemplaza 'fondo.wav' con la ruta de tu archivo de sonido)
sonido_alarma = pygame.mixer.Sound("fondo.wav")

# Obtener la hora de la alarma (reemplaza esto con la lógica para obtener la hora ingresada por el usuario)
hora_alarma = datetime.time(hour=8, minute=30)  # Ejemplo: alarma a las 8:30 AM

while True:
    hora_actual = datetime.datetime.now().time()

    if hora_actual.hour == hora_alarma.hour and hora_actual.minute == hora_alarma.minute:
        print("¡Es hora de la alarma!")
        sonido_alarma.play()  # Reproducir el sonido de la alarma

    # Esperar un segundo antes de verificar nuevamente
    time.sleep(1)
   
#7.
if hora_actual == hora_alarma:

  sonido_alarma.play()
  
  time.sleep(20) # Suena por 20 segundos
  
  sonido_alarma.stop()

  alarma_activa = False # Desactivar alarma
  
#8.
import android
from android.droid import batterystats

# Obtener estado del modo silencioso  
audio_manager = android.Android().getContext().getSystemService(android.Android().AUDIO_SERVICE)
modo_silencioso = audio_manager.ringer_mode != android.Android().RINGER_MODE_NORMAL

# Obtener nivel de batería
nivel_bateria = batterystats.BatteryStats().getStatistics()['percentage'] 

if hora_actual == hora_alarma:

  # Revisar modo silencioso
  if modo_silencioso:
    # Mostrar notificación en lugar de sonido
    pass

  # Revisar batería baja   
  if nivel_bateria < 20:
    # No reproducir sonido
    pass

  # Tu código para reproducir el sonido
  sonido_alarma.play()
  
  # Tu código para desactivar la alarma
    
#9.
import json

# Datos a almacenar
preferencias = {
   "hora_alarma": "22:46",
   "ruta_sonido": "/sdcard/alarma.mp3",
   "volumen": 80
}

# Guardar en archivo 
with open("preferencias_alarma.txt", "w") as archivo:
    json.dump(preferencias, archivo)

# Cargar preferencias
with open("preferencias_alarma.txt") as archivo:
    preferencias = json.load(archivo)

hora_alarma = preferencias["hora_alarma"]
ruta_sonido = preferencias["ruta_sonido"]
volumen = preferencias["volumen"]

import pygame

class AlarmaApp(App):

    def reproducir_alarma(self, dt):
        if self.activa:
            # Inicializa pygame
            pygame.init() 
            
            # Carga sonido
            pygame.mixer.music.load(self.ruta_sonido)
            
            # Reproduce
            pygame.mixer.music.play()
            
            self.activa = False