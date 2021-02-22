from kivy.uix.textinput import TextInput


class ValueTextInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if substring in '0123456789' and len(self.text) < 4:
            return TextInput.insert_text(self, substring, from_undo)


__all__ = ['ValueTextInput']
