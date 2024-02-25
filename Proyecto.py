from kivy.app import App
from kivy.clock import mainthread, Clock  
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from tkinter import filedialog
import os
import datetime
import pygame

class AlarmaApp(App):
    def build(self):
        self.activa = False
        self.hora_alarma = None
        self.ruta_sonido = None
        
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        self.hora_label = Label(text="Hora actual:") 
        layout.add_widget(self.hora_label)

        self.hora_input = TextInput(hint_text="HH:MM")
        layout.add_widget(self.hora_input)
        
        self.file_chooser = FileChooserListView(path='.')
        layout.add_widget(self.file_chooser)
        
        btn_alarma = Button(text="Establecer alarma")
        btn_alarma.bind(on_press=self.establecer_alarma)
        layout.add_widget(btn_alarma)
        
        return layout

    def establecer_alarma(self, instance):
        texto_hora = self.hora_input.text
        self.ruta_sonido = self._seleccionar_sonido()
        
        if texto_hora:
            self.hora_alarma = self.__obtener_datetime(texto_hora)
            self.hora_label.text = f"Hora de alarma: {texto_hora}"
            
            self.__schedule_alarma()
                
            # Activa alarma 
            self.activa = True

    def _seleccionar_sonido(self):
        pass
        
    def __obtener_datetime(self, texto):
        pass
        
    def __schedule_alarma(self):
        if self.hora_alarma:
            Clock.schedule_once(self.reproducir_alarma, self.hora_alarma)
            
    @mainthread        
    def reproducir_alarma(self, dt):
        if self.activa:
            print("Reproduciendo sonido")
            
            self.activa = False

if __name__ == "__main__":
    AlarmaApp().run()
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
            