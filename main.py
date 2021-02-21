from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class BeepTimerLayout(BoxLayout):
    pass


class BeepTimerApp(App):
    def build(self):
        return BeepTimerLayout()


if __name__ == '__main__':
    with open("app_layout.kv", encoding='utf8') as f:
        my = Builder.load_string(f.read())
    Window.clearcolor = [1, 1, 1, 1]
    BeepTimerApp().run()
