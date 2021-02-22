from threading import Thread
from datetime import datetime
from time import sleep

import winsound


class BeepThread(Thread):
    def __init__(self, app):
        Thread.__init__(self)
        self.app = app

    def run(self):
        # (((текущая минута в секундах + текущая секунда) +
        # (время до сигнала в секундах + длительность сигнала в секундах))
        # в минутах) % время таймера == 0.
        while True:
            for timer_info in self.app.timers_info:
                for signal_info in timer_info['signals']:
                    # текущая минута в секундах
                    current_time = datetime.now()
                    current_minute_in_seconds = current_time.minute * 60

                    # текущая секунда
                    current_second = current_time.second

                    # текущая минута в секундах + текущая секунда
                    current_global_second = current_minute_in_seconds + current_second

                    # время до сигнала в секундах
                    time_to_signal_in_seconds = signal_info['time_to_signal']
                    if signal_info['time_unit'] == 'minute':
                        time_to_signal_in_seconds *= 60

                    # длительность сигнала в секундах
                    signal_duration_in_seconds = int(signal_info['duration'] / 1000)

                    # время до сигнала в секундах + длительность сигнала в секундах
                    global_time_to_signal = time_to_signal_in_seconds + signal_duration_in_seconds

                    # сума глобальных значений.
                    global_time_target = current_global_second + global_time_to_signal

                    # сума глобальных значений в минутах
                    global_time_target_in_minutes = global_time_target / 60

                    # время таймера
                    timer_time = timer_info['timer_time']

                    print(global_time_target_in_minutes)

                    # проверка совпадения
                    if global_time_target_in_minutes % timer_time == 0:
                        frequency = signal_info['frequency']
                        duration = signal_info['duration']
                        winsound.Beep(frequency, duration)
            sleep(0.001)
