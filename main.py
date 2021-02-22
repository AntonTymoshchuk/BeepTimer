from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from my_widgets.add_signal_button import AddSignalButton
from my_widgets.add_timer_button import AddTimerButton
from my_widgets.delete_signal_button import DeleteSignalButton
from my_widgets.delete_timer_button import DeleteTimerButton
from my_widgets.frequency_text_input import FrequencyTextInput
from my_widgets.milliseconds_text_input import MillisecondsTextInput
from my_widgets.minus_button import MinusButton
from my_widgets.minutes_text_input import MinutesTextInput
from my_widgets.plus_button import PlusButton
from my_widgets.some_time_text_input import SomeTimeTextInput
from my_widgets.signal_layout import SignalLayout
from my_widgets.standard_check_box import StandardCheckBox
from my_widgets.time_unit_label import TimeUnitLabel
from my_widgets.timer_layout import TimerLayout

from beep_thread import BeepThread
from my_widgets.wide_button import WideButton


class BeepTimerLayout(BoxLayout):
    pass


class BeepTimerApp(App):
    def __init__(self, **kwargs):
        App.__init__(self, **kwargs)
        self.ids = None
        self.num = 0
        self.timers_info = []
        beep_thread = BeepThread(self)
        beep_thread.daemon = True
        beep_thread.start()

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
        pos = 0
        while True:
            button_tbe = timer_layout.children[pos]
            if isinstance(button_tbe, WideButton):
                break
            pos += 1
        button_tbe.disabled = False
        timer_layout.height += dp(100)
        self.ids.main_container.height += dp(100)

    def remove_signal(self, sender):
        signal_layout_tbr = sender.parent
        signals_container = signal_layout_tbr.parent
        signals_container.remove_widget(signal_layout_tbr)
        timer_layout = signals_container.parent
        if len(signals_container.children) == 1:
            pos = 0
            while True:
                button_tbe = timer_layout.children[pos]
                if isinstance(button_tbe, WideButton):
                    break
                pos += 1
            button_tbe.disabled = True
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
        self.num += 1
        timers_container.remove_widget(button_tbr)
        timers_container.add_widget(TimerLayout(self.num))
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
            if isinstance(input_tbe, SomeTimeTextInput):
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
            if isinstance(input_tbe, SomeTimeTextInput):
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

    def start_timer(self, sender):
        timer_layout = sender.parent
        if not timer_layout.started:
            sender.text = 'Остановить таймер'
            timer_layout.started = True
            header = None
            for child in timer_layout.children:
                if isinstance(child, GridLayout):
                    header = child
                    break
            timer_value = None
            for child in header.children:
                if isinstance(child, MinutesTextInput):
                    timer_value = int(child.text)
                    break
            signals_layout = None
            for child in timer_layout.children:
                if isinstance(child, BoxLayout):
                    signals_layout = child
                    break
            signal_containers = []
            for child in signals_layout.children:
                if isinstance(child, SignalLayout):
                    signal_containers.append(child)
            signals_info = []
            for child in signal_containers:
                signal_info = {}
                self.get_signal_container_info(child, signal_info)
                signals_info.append(signal_info)
            self.timers_info.append({'number': timer_layout.number,
                                     'timer_time': timer_value,
                                     'signals': signals_info})
            self.change_children_state(timer_layout, True)
        else:
            sender.text = 'Запустить таймер'
            timer_layout.started = False
            pos = 0
            while pos < len(self.timers_info):
                if self.timers_info[pos]['number'] == \
                        timer_layout.number:
                    self.timers_info.pop(pos)
                    break
                pos += 1
            self.change_children_state(timer_layout, False)

    def get_signal_container_info(self, parent, signal_info):
        for child in parent.children:
            if isinstance(child, SomeTimeTextInput):
                signal_info['time_to_signal'] = int(child.text)
            elif isinstance(child, TimeUnitLabel):
                if child.text[1: -1] == 'сек':
                    time_unit = 'second'
                else:
                    time_unit = 'minute'
                signal_info['time_unit'] = time_unit
            elif isinstance(child, MillisecondsTextInput):
                signal_info['duration'] = int(child.text)
            elif isinstance(child, FrequencyTextInput):
                signal_info['frequency'] = int(child.text)
            self.get_signal_container_info(child, signal_info)

    def change_children_state(self, parent, value):
        for child in parent.children:
            if isinstance(child, MinutesTextInput):
                child.disabled = value
            elif isinstance(child, SomeTimeTextInput):
                child.disabled = value
            elif isinstance(child, MillisecondsTextInput):
                child.disabled = value
            elif isinstance(child, FrequencyTextInput):
                child.disabled = value
            elif isinstance(child, StandardCheckBox):
                child.disabled = value
            elif isinstance(child, PlusButton):
                child.disabled = value
            elif isinstance(child, MinusButton):
                child.disabled = value
            elif isinstance(child, DeleteSignalButton):
                child.disabled = value
            elif isinstance(child, AddSignalButton):
                child.disabled = value
            elif isinstance(child, DeleteTimerButton):
                child.disabled = value
            self.change_children_state(child, value)


if __name__ == '__main__':
    with open("app_layout.kv", encoding='utf8') as f:
        Builder.load_string(f.read())
    Window.clearcolor = [1, 1, 1, 1]
    BeepTimerApp().run()
