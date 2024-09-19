import generate_verse
import kivy

from generate_verse import colour

kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class CreateScreen(GridLayout):

    def __init__(self, **kwargs):
        super(CreateScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Colour: \n True or False'))
        self.colour_input = TextInput(text="False",multiline=False)
        self.add_widget(self.colour_input)
        self.add_widget(Label(text='Size: \n Recommended 500 to 4000'))
        self.canvas_size = TextInput(text="500",multiline=False)
        self.add_widget(self.canvas_size)
        btn1 = Button(text= "Do it!")
        self.add_widget(btn1)
        btn1.bind(on_press=self.callback)

    def callback(self, instance):
        if self.colour_input.text == "False":
            colourchoice = False
        elif self.colour_input.text == "True":
            colourchoice = True
        else:
            colourchoice = False

        if int(self.canvas_size.text) <= 0:
            size = 500
        else:
            size = int(self.canvas_size.text)

        generate_verse.generate_main(colourchoice,size)





class MultiSlug(App):
    def build(self):
        return CreateScreen()


if __name__ == '__main__':
    MultiSlug().run()