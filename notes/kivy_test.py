from kivy.app import App
from kivy.lang import Builder

class HelloWorldApp(App):
    def build(self):
        return Builder.load_file("main.kv")


HelloWorldApp().run()

# Orientation tells what direction the box should be
# Label displays text on screen, Always required
# Button creates a clickable button with customizable appearence and behavior
# TextInput is where user inputs text
# You can make checkboxes