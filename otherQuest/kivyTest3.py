from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainApp(App):


    def __init__(self):
        super().__init__()


    def build(self):


        layout = BoxLayout(size_hint = (0.5, 0.5),
                           pos_hint = {'center_x': .5,
                           'center_y': .5},
                           padding = 0.5,
                           spacing = 10,
                           orientation = "vertical")

        layout2 = BoxLayout(orientation = 'horizontal')

        texto = Label(text='Deu certo?',
                      size_hint = (.10, .10),
                      pos_hint = {'center_x': .5, 'center_y': .5}

                      )

        button1 = Button(text='Sim',
                        size_hint = (.4, 0.5),
                        pos_hint = {'center_x': .5,
                                    'center_y': .5}
                        )

        button2 = Button(text='Não',
                         size_hint = (.4, 0.5),
                         pos_hint = {'center_x': .5,
                                     'center_y': .5}
                         )

        button1.bind(on_press = self.teste)
        button2.bind(on_press = self.on_press_button2)



        layout.add_widget(texto)
        layout2.add_widget(button1)
        layout2.add_widget(button2)
        layout.add_widget(layout2)
        return layout




    def on_press_button1(self, instance):
        print(':D')

    def on_press_button2(self, instance):
        print('>:O')

    def teste(self, instance):
        text = self.texto.text
        text = 'deu certo'

if __name__ == '__main__':
    app = MainApp()
    app.run()