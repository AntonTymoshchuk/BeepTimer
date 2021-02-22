from kivy.uix.gridlayout import GridLayout

from my_widgets.standard_check_box import StandardCheckBox


class SignalLayout(GridLayout):
    def __init__(self, num, **kwargs):
        GridLayout.__init__(self, **kwargs)
        for child in self.children:
            if isinstance(child, StandardCheckBox):
                child.group = 'time_unit_{0}'.format(str(num))
            self.set_time_unit_to_children(child, num)

    def set_time_unit_to_children(self, parent, num):
        for child in parent.children:
            if isinstance(child, StandardCheckBox):
                child.group = 'time_unit_{0}'.format(str(num))
            self.set_time_unit_to_children(child, num)


__all__ = ['SignalLayout']
