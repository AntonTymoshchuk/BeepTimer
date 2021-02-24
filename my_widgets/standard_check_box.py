from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty


class StandardCheckBox(CheckBox):
    time_unit = StringProperty()

    def on_touch_down(self, touch):
        if not self.active:
            CheckBox.on_touch_down(self, touch)


__all__ = ['StandardCheckBox']
