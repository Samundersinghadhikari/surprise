from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout

class MainApp(MDApp):
    def build(self):
        # Create a BoxLayout to hold the label and button
        layout = BoxLayout(orientation='vertical', spacing=100, padding=10)
        
        # Create a label with initial text
        self.label = MDLabel(text="Click to get suprise!", halign="center")
        
        # Create a button with the callback to change the label text
        button = MDRaisedButton(text="Click Me!")
        button.bind(on_release=self.say_hello)
        
        # Add the label and button to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)
        
        return layout
    
    def say_hello(self, instance):
        # Change the label text when the button is clicked
        self.label.text = "Why are you Gay?"

MainApp().run()
