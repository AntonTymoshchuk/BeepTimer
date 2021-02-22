from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from my_widgets.add_signal_button import AddSignalButton
from my_widgets.add_timer_button import AddTimerButton
from my_widgets.frequency_text_input import FrequencyTextInput
from my_widgets.milliseconds_text_input import MillisecondsTextInput
from my_widgets.minutes_text_input import MinutesTextInput
from my_widgets.seconds_text_input import SecondsTextInput
from my_widgets.signal_layout import SignalLayout
from my_widgets.time_unit_label import TimeUnitLabel
from my_widgets.timer_layout import TimerLayout


class BeepTimerLayout(BoxLayout):
    pass


class BeepTimerApp(App):
    def __init__(self, **kwargs):
        App.__init__(self, **kwargs)
        self.ids = None
        self.num = 0

    def build(self):
        layout = BeepTimerLayout()
        self.ids = layout.ids
        return layout

    def add_signal(self, sender):
        signals_container = sender.parent
        pos = 0
        while True:
            button_tbr = signals_container.children[pos]
            if isinstance(button_tbr, AddSignalButton):
                break
            pos += 1
        self.num += 1
        signals_container.remove_widget(button_tbr)
        signals_container.add_widget(SignalLayout(self.num))
        signals_container.add_widget(AddSignalButton())
        timer_layout = signals_container.parent
        timer_layout.height += dp(100)
        self.ids.main_container.height += dp(100)

    def remove_signal(self, sender):
        signal_layout_tbr = sender.parent
        signals_container = signal_layout_tbr.parent
        signals_container.remove_widget(signal_layout_tbr)
        timer_layout = signals_container.parent
        timer_layout.height -= dp(100)
        self.ids.main_container.height -= dp(100)

    def add_timer(self, sender):
        timers_container = sender.parent
        pos = 0
        while True:
            button_tbr = timers_container.children[pos]
            if isinstance(button_tbr, AddTimerButton):
                break
            pos += 1
        timers_container.remove_widget(button_tbr)
        timers_container.add_widget(TimerLayout())
        timers_container.add_widget(AddTimerButton())
        self.ids.main_container.height += dp(130)

    def remove_timer(self, sender):
        timer_layout_tbr = sender.parent.parent.parent
        layout_height = timer_layout_tbr.height
        self.ids.main_container.remove_widget(timer_layout_tbr)
        self.ids.main_container.height -= layout_height

    def increase_seconds_value(self, sender):
        container = sender.parent.parent
        pos = 0
        while True:
            input_tbe = container.children[pos]
            if isinstance(input_tbe, SecondsTextInput):
                break
            pos += 1
        if input_tbe.text == '':
            value = 0
        else:
            value = int(input_tbe.text)
        if value < 9999:
            value += 1
        input_tbe.text = str(value)

    def reduce_seconds_value(self, sender):
        container = sender.parent.parent
        pos = 0
        while True:
            input_tbe = container.children[pos]
            if isinstance(input_tbe, SecondsTextInput):
                break
            pos += 1
        if input_tbe.text == '':
            value = 0
        else:
            value = int(input_tbe.text)
        if value > 0:
            value -= 1
        input_tbe.text = str(value)

    def increase_milliseconds_value(self, sender):
        container = sender.parent.parent
        pos = 0
        while True:
            input_tbe = container.children[pos]
            if isinstance(input_tbe, MillisecondsTextInput):
                break
            pos += 1
        if input_tbe.text == '':
            value = 0
        else:
            value = int(input_tbe.text)
        if value < 9999:
            value += 1
        input_tbe.text = str(value)

    def reduce_milliseconds_value(self, sender):
        container = sender.parent.parent
        pos = 0
        while True:
            input_tbe = container.children[pos]
            if isinstance(input_tbe, MillisecondsTextInput):
                break
            pos += 1
        if input_tbe.text == '':
            value = 0
        else:
            value = int(input_tbe.text)
        if value > 0:
            value -= 1
        input_tbe.text = str(value)

    def increase_frequency_value(self, sender):
        container = sender.parent.parent
        pos = 0
        while True:
            input_tbe = container.children[pos]
            if isinstance(input_tbe, FrequencyTextInput):
                break
            pos += 1
        if input_tbe.text == '':
            value = 0
        else:
            value = int(input_tbe.text)
        if value < 9999:
            value += 1
        input_tbe.text = str(value)

    def reduce_frequency_value(self, sender):
        container = sender.parent.parent
        pos = 0
        while True:
            input_tbe = container.children[pos]
            if isinstance(input_tbe, FrequencyTextInput):
                break
            pos += 1
        if input_tbe.text == '':
            value = 0
        else:
            value = int(input_tbe.text)
        if value > 0:
            value -= 1
        input_tbe.text = str(value)

    def increase_minutes_value(self, sender):
        container = sender.parent
        pos = 0
        while True:
            input_tbe = container.children[pos]
            if isinstance(input_tbe, MinutesTextInput):
                break
            pos += 1
        if input_tbe.text == '':
            value = 0
        else:
            value = int(input_tbe.text)
        if value < 9999:
            value += 1
        input_tbe.text = str(value)

    def reduce_minutes_value(self, sender):
        container = sender.parent
        pos = 0
        while True:
            input_tbe = container.children[pos]
            if isinstance(input_tbe, MinutesTextInput):
                break
            pos += 1
        if input_tbe.text == '':
            value = 0
        else:
            value = int(input_tbe.text)
        if value > 0:
            value -= 1
        input_tbe.text = str(value)

    def set_second_time_unit(self, sender):
        container = sender.parent
        pos = 0
        while True:
            label_tbe = container.children[pos]
            if isinstance(label_tbe, TimeUnitLabel):
                break
            pos += 1
        label_tbe.text = ' сек '

    def set_minute_time_unit(self, sender):
        container = sender.parent
        pos = 0
        while True:
            label_tbe = container.children[pos]
            if isinstance(label_tbe, TimeUnitLabel):
                break
            pos += 1
        label_tbe.text = ' мин '


if __name__ == '__main__':
    with open("app_layout.kv", encoding='utf8') as f:
        Builder.load_string(f.read())
    Window.clearcolor = [1, 1, 1, 1]
    BeepTimerApp().run()
