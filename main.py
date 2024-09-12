from gettext import textdomain

import generate_verse
import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class CreateScreen(GridLayout):

    def __init__(self, **kwargs):
        super(CreateScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Colour:'))
        self.colour = TextInput(multiline=False)
        self.add_widget(self.colour)
        self.add_widget(Label(text='Size:'))
        self.canvas_size = TextInput(multiline=False)
        self.add_widget(self.canvas_size)




class MultiSlug(App):
    def build(self):
        return CreateScreen()


if __name__ == '__main__':
    MultiSlug().run()