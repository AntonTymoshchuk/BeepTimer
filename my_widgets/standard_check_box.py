from kivy.uix.checkbox import CheckBox


class StandardCheckBox(CheckBox):
    def on_touch_down(self, touch):
        if not self.active:
            CheckBox.on_touch_down(self, touch)


__all__ = ['StandardCheckBox']
