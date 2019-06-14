from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = 360, 500

Builder.load_file('calculatorkivy.kv')

class Frame(BoxLayout):
    prev = None
    funct = None

    def add(self, *args):
        getter = self.ids['display']
        self.prev = getter.text
        getter.text = ''
        self.funct = '+'

    def subtract(self, *args):
        getter = self.ids['display']
        self.prev = getter.text
        getter.text = ''
        self.funct = '-'

    def divide(self, *args):
        getter = self.ids['display']
        self.prev = getter.text
        getter.text = ''
        self.funct = '/'

    def multiply(self, *args):
        getter = self.ids['display']
        self.prev = getter.text
        getter.text = ''
        self.funct = '*'

    def power(self, *args):
        getter = self.ids['display']
        self.prev = getter.text
        getter.text = ''
        self.funct = '**'

    def AC(self, *args):
        getter = self.ids['display']
        getter.text = ''
        getter.color = 0, 0, 0, 1

    def error(self,*args):
        getter = self.ids['display']
        getter.color = 1, 0, 0, 1
        getter.text = 'Error'

    def calc(self, *args):
        ans = 0
        old = self.prev
        oldrn = ''
        if str(old).count(',') > 0:
            for figure in str(old):
                if figure != ',':
                    oldrn += figure
                else:
                    pass
            old = oldrn
        getter = self.ids['display']
        new = getter.text
        work = self.funct

        try:
            if work == '+':
                ans = float(old) + float(new)
                ans = '{:,}'.format(ans)
                getter.text = str(ans)

            elif work == '-':
                ans = float(old) - float(new)
                ans = '{:,}'.format(ans)
                getter.text = str(ans)

            elif work == '*':
                ans = float(old) * float(new)
                ans = '{:,}'.format(ans)
                getter.text = str(ans)

            elif work == '/':
                ans = float(old) / float(new)
                ans = '{:,}'.format(ans)
                getter.text = str(ans)

            elif work == '**':
                ans = float(old) ** float(new)
                ans = '{:,}'.format(ans)
                getter.text = str(ans)

            elif work == 'AC':
                getter.text = ' '
                getter.color = 0, 0, 0, 1
                
        except Exception as e:
            Clock.schedule_once(self.error, 0.0000000000000000000000001)
            Clock.schedule_once(self.AC, 1/2)


        old = ans
        new = None
        self.funct = None

class calculator(App):
    def build(self):
        return Frame()

if __name__ == '__main__':
    calculator().run()
