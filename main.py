from kivy.config import Config
Config.read('config.ini')

if __name__ == '__main__':
    from kivy.core.window import Window
    from kivy.lang import Builder
    from main_app import BeepTimerApp

    with open("app_layout.kv", encoding='utf8') as f:
        Builder.load_string(f.read())
    beep_timer_app = BeepTimerApp()
    Window.clearcolor = [1, 1, 1, 1]
    Window.on_request_close = beep_timer_app.on_request_close
    BeepTimerApp().run()
