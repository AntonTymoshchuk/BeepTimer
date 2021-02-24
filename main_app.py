import os

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
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
        self.working_timers_info = []
        beep_thread = BeepThread(self)
        beep_thread.daemon = True
        beep_thread.start()

    def build(self):
        layout = BeepTimerLayout()
        self.ids = layout.ids
        self.show_saved_timers()
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
        self.save_timers_info()

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
        self.save_timers_info()

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
        self.save_timers_info()

    def remove_timer(self, sender):
        timer_layout_tbr = sender.parent.parent.parent
        layout_height = timer_layout_tbr.height
        self.ids.main_container.remove_widget(timer_layout_tbr)
        self.ids.main_container.height -= layout_height
        self.save_timers_info()

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
        self.save_timers_info()

    def set_minute_time_unit(self, sender):
        container = sender.parent
        pos = 0
        while True:
            label_tbe = container.children[pos]
            if isinstance(label_tbe, TimeUnitLabel):
                break
            pos += 1
        label_tbe.text = ' мин '
        self.save_timers_info()

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
                    if child.text == '':
                        timer_value = 0
                    else:
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
            self.working_timers_info.append({'number': timer_layout.number,
                                             'timer_time': timer_value,
                                             'signals': signals_info})
            self.change_children_state(timer_layout, True)
        else:
            sender.text = 'Запустить таймер'
            timer_layout.started = False
            pos = 0
            while pos < len(self.working_timers_info):
                if self.working_timers_info[pos]['number'] == \
                        timer_layout.number:
                    self.working_timers_info.pop(pos)
                    break
                pos += 1
            self.change_children_state(timer_layout, False)

    def get_signal_container_info(self, parent, signal_info):
        for child in parent.children:
            if isinstance(child, SomeTimeTextInput):
                if child.text == '':
                    signal_info['time_to_signal'] = 0
                else:
                    signal_info['time_to_signal'] = int(child.text)
            elif isinstance(child, TimeUnitLabel):
                if child.text[1: -1] == 'сек':
                    time_unit = 'second'
                else:
                    time_unit = 'minute'
                signal_info['time_unit'] = time_unit
            elif isinstance(child, MillisecondsTextInput):
                if child.text == '':
                    signal_info['duration'] = 0
                else:
                    signal_info['duration'] = int(child.text)
            elif isinstance(child, FrequencyTextInput):
                if child.text == '':
                    signal_info['frequency'] = 0
                else:
                    signal_info['frequency'] = int(child.text)
            self.get_signal_container_info(child, signal_info)

    def get_timer_layout_info(self, timer, timer_info):
        header = None
        for child in timer.children:
            if isinstance(child, GridLayout):
                header = child
                break
        timer_value = None
        for child in header.children:
            if isinstance(child, MinutesTextInput):
                if child.text == '':
                    timer_value = 0
                else:
                    timer_value = int(child.text)
                break
        signals_layout = None
        for child in timer.children:
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
        timer_info['timer_time'] = timer_value
        timer_info['signals'] = signals_info

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

    def on_text_change(self):
        self.save_timers_info()

    def read_timers_info(self):
        local_timers_info = []
        timers_path = os.getcwd() + '/timers.ini'
        timers_file = open(timers_path, 'r')
        lines = timers_file.readlines()
        pos = 0
        while pos < len(lines):
            lines[pos] = lines[pos].split('\n')[0]
            pos += 1
        pos = 0
        while pos < len(lines):
            if lines[pos] == '[timer]':
                timer_info = {'timer_time': int(lines[pos + 1].split('=')[1])}
                signals_info = []
                pos += 2
                while pos < len(lines):
                    if lines[pos] == '[timer]':
                        pos -= 1
                        break
                    elif lines[pos] == '[signal]':
                        signal_info = {'time_to_signal': int(lines[pos + 1].split('=')[1]),
                                       'time_unit': lines[pos + 2].split('=')[1],
                                       'duration': int(lines[pos + 3].split('=')[1]),
                                       'frequency': int(lines[pos + 4].split('=')[1])}
                        signals_info.append(signal_info)
                        pos += 4
                    pos += 1
                timer_info['signals'] = signals_info
                local_timers_info.append(timer_info)
            pos += 1
        timers_file.close()
        return local_timers_info

    def show_saved_timers(self):
        local_timers_info = self.read_timers_info()
        timer_layouts = []
        for timer_info in local_timers_info:
            self.num += 1
            timer_layout = TimerLayout(self.num)
            timer_time = str(timer_info['timer_time'])
            self.set_minutes_text_input_value(timer_layout, timer_time)
            signal_layouts = []
            for signal_info in timer_info['signals']:
                self.num += 1
                signal_layout = SignalLayout(self.num)
                time_to_signal = str(signal_info['time_to_signal'])
                time_unit = None
                if signal_info['time_unit'] == 'second':
                    time_unit = ' сек '
                elif signal_info['time_unit'] == 'minute':
                    time_unit = ' мин '
                check_box_value = None
                if time_unit == ' сек ':
                    check_box_value = 'second'
                elif time_unit == ' мин ':
                    check_box_value = 'minute'
                duration = str(signal_info['duration'])
                frequency = str(signal_info['frequency'])
                self.set_some_time_text_input_value(signal_layout, time_to_signal)
                self.set_standard_check_box_value(signal_layout, check_box_value)
                self.set_time_unit_label_value(signal_layout, time_unit)
                self.set_milliseconds_text_input_value(signal_layout, duration)
                self.set_frequency_text_input_value(signal_layout, frequency)
                signal_layouts.append(signal_layout)
                timer_layout.height += dp(100)
                self.ids.main_container.height += dp(100)
            signals_container = None
            for child in timer_layout.children:
                if isinstance(child, BoxLayout):
                    signals_container = child
            pos = 0
            while True:
                button_tbr = signals_container.children[pos]
                if isinstance(button_tbr, AddSignalButton):
                    break
                pos += 1
            self.num += 1
            signals_container.remove_widget(button_tbr)
            for signal_layout in signal_layouts:
                signals_container.add_widget(signal_layout)
            signals_container.add_widget(AddSignalButton())
            if len(signal_layouts) > 0:
                pos = 0
                while True:
                    button_tbe = timer_layout.children[pos]
                    if isinstance(button_tbe, WideButton):
                        break
                    pos += 1
                button_tbe.disabled = False
            timer_layouts.append(timer_layout)
            self.ids.main_container.height += dp(130)
        pos = 0
        while True:
            button_tbr = self.ids.main_container.children[pos]
            if isinstance(button_tbr, AddTimerButton):
                break
            pos += 1
        self.ids.main_container.remove_widget(button_tbr)
        for timer_layout in timer_layouts:
            self.ids.main_container.add_widget(timer_layout)
        self.ids.main_container.add_widget(AddTimerButton())
        self.save_timers_info()

    def set_minutes_text_input_value(self, parent, value):
        for child in parent.children:
            if isinstance(child, MinutesTextInput):
                child.text = value
                break
            self.set_minutes_text_input_value(child, value)

    def set_some_time_text_input_value(self, parent, value):
        for child in parent.children:
            if isinstance(child, SomeTimeTextInput):
                child.text = value
                break
            self.set_some_time_text_input_value(child, value)

    def set_standard_check_box_value(self, parent, value):
        for child in parent.children:
            if isinstance(child, StandardCheckBox):
                if child.time_unit == 'second' and value == 'second':
                    child.active = True
                elif child.time_unit == 'minute' and value == 'minute':
                    child.active = True
            self.set_standard_check_box_value(child, value)

    def set_time_unit_label_value(self, parent, value):
        for child in parent.children:
            if isinstance(child, TimeUnitLabel):
                child.text = value
                break
            self.set_time_unit_label_value(child, value)

    def set_milliseconds_text_input_value(self, parent, value):
        for child in parent.children:
            if isinstance(child, MillisecondsTextInput):
                child.text = value
                break
            self.set_milliseconds_text_input_value(child, value)

    def set_frequency_text_input_value(self, parent, value):
        for child in parent.children:
            if isinstance(child, FrequencyTextInput):
                child.text = value
                break
            self.set_frequency_text_input_value(child, value)

    def save_timers_info(self):
        local_timers_info = []
        for child in self.ids.main_container.children:
            if isinstance(child, TimerLayout):
                timer_info = {}
                self.get_timer_layout_info(child, timer_info)
                local_timers_info.append(timer_info)
        local_timers_info.reverse()
        timers_path = os.getcwd() + '/timers.ini'
        timers_file = open(timers_path, 'w')
        for timer_info in local_timers_info:
            timers_file.write('[timer]\n')
            timers_file.write('timer_time={0}\n\n'.format(timer_info['timer_time']))
            for signal_info in timer_info['signals']:
                timers_file.write('[signal]\n')
                timers_file.write('time_to_signal={0}\n'.format(signal_info['time_to_signal']))
                timers_file.write('time_unit={0}\n'.format(signal_info['time_unit']))
                timers_file.write('duration={0}\n'.format(signal_info['duration']))
                timers_file.write('frequency={0}\n'.format(signal_info['frequency']))
                timers_file.write('\n')
            timers_file.write('\n')
        timers_file.close()

    def on_request_close(self, **kwargs):
        from kivy.core.window import Window
        from kivy.config import Config
        Config.set('graphics', 'left', Window.left)
        Config.set('graphics', 'top', Window.top)
        Config.set('graphics', 'width', Window.width)
        Config.set('graphics', 'height', Window.height)
        Config.write()
