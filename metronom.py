import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix import label


class TestApp(App):

    def build(self):
        # return a Button() as a root widget
        return Button(text='hello world', font_size=70)


if __name__ == '__main__':
    TestApp().run()
