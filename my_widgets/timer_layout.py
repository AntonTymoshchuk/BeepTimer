from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty


class TimerLayout(BoxLayout):
    started = BooleanProperty(False)


__all__ = ['TimerLayout']
