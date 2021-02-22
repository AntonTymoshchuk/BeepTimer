from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty


class TimerLayout(BoxLayout):
    started = BooleanProperty(False)

    def __init__(self, number, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.number = number


__all__ = ['TimerLayout']
