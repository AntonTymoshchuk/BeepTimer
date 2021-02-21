from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class BeepTimerLayout(BoxLayout):
    pass


class BeepTimerApp(App):
    def build(self):
        return BeepTimerLayout()


if __name__ == '__main__':
    Window.clearcolor = [1, 1, 1, 1]
    BeepTimerApp().run()
