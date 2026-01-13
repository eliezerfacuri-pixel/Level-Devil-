from kivy.app import App
from kivy.uix.label import Label

class JogoApp(App):
    def build(self):
        return Label(text="Level Devil rodando!")

if __name__ == "__main__":
    JogoApp().run()
  
