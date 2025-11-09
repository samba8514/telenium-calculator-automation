from telenium import install
install()

# Calc Application with Kivy - Telenium Automation Example
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CalcApplicationWidget(BoxLayout):
    """Calculator widget - UI defined in calcapplication.kv"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Calculator state
        self.display_text = '0'
        self.current_num = ''
        self.first_num = None
        self.operation = None

    def update_display(self, text):
        """Update calculator display"""
        self.display_text = str(text)
        self.ids.display.text = self.display_text

    def on_button(self, instance):
        """Handle button presses - called from KV file"""
        btn_text = instance.text

        if btn_text.isdigit():  # Numbers 0-9
            self.current_num += btn_text
            self.update_display(self.current_num)

        elif btn_text == 'Add':
            self.set_operation('+')
        elif btn_text == 'Sub':
            self.set_operation('-')
        elif btn_text == 'Mul':
            self.set_operation('*')
        elif btn_text == 'Div':
            self.set_operation('/')

        elif btn_text == 'Eq':
            self.calculate()

        elif btn_text in ['C', 'CE', 'Clear']:
            self.clear_all()

        elif btn_text == 'Back':
            self.backspace()

        elif btn_text == 'Dot':
            if '.' not in self.current_num:
                self.current_num += '.'
                self.update_display(self.current_num)

    def set_operation(self, op):
        """Set the operation"""
        if self.current_num:
            if self.first_num is not None and self.operation:
                self.calculate()
            else:
                self.first_num = float(self.current_num)
            self.operation = op
            self.current_num = ''

    def calculate(self):
        """Perform calculation"""
        if self.current_num and self.first_num is not None and self.operation:
            second_num = float(self.current_num)

            if self.operation == '+':
                result = self.first_num + second_num
            elif self.operation == '-':
                result = self.first_num - second_num
            elif self.operation == '*':
                result = self.first_num * second_num
            elif self.operation == '/':
                if second_num != 0:
                    result = self.first_num / second_num
                else:
                    self.update_display('Error')
                    return

            # Format result
            if result.is_integer():
                result = int(result)

            self.update_display(result)
            self.first_num = result
            self.current_num = ''
            self.operation = None

    def clear_all(self):
        """Clear everything"""
        self.current_num = ''
        self.first_num = None
        self.operation = None
        self.update_display('0')

    def backspace(self):
        """Remove last character"""
        if self.current_num:
            self.current_num = self.current_num[:-1]
            self.update_display(self.current_num if self.current_num else '0')


class CalcApplication(App):
    """
    Main Calc Application class for Telenium automation example

    Kivy automatically loads calcapplication.kv file based on class name
    """

    def build(self):
        from kivy.core.window import Window

        # Set window size to match the desired calculator size
        Window.size = (400, 600)
        Window.minimum_width = 350
        Window.minimum_height = 500

        self.title = 'Calc Application - Telenium Example'
        # KV file defines the UI, just return the root widget
        return CalcApplicationWidget()


if __name__ == '__main__':
    CalcApplication().run()