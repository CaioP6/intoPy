from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'dock')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ['/', '*', '+', '-'] #lista dos operadores
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation = 'vertical')
        self.solution = TextInput(
            multiline = False, #definido como não-multilinha
            readonly = True, #definido como Apenas leitura
            halign = 'right', #alinhamento
            font_size = 55
        )
        main_layout.add_widget(self.solution)

        buttons = [#uma aninhada de lista para os buttons
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        
        for row in buttons: #para cada linha da aninhada faça
          h_layout = BoxLayout() #um layout horizontal
            
          for label in row: #para cada label na linha faça
             button = Button( #um
             text = label,
             pos_hint = {'center_x': 0.5,
                        'center_y': 0.5}
                )
             button.bind(on_press = self.on_button_press)
             h_layout.add_widget(button)
          main_layout.add_widget(h_layout)

        igual_button = Button(
         text = '=',
         pos_hint = {'center_x': 0.5,
                     'center_y': 0.5}
                )
        igual_button.bind(on_press = self.on_solution)
        main_layout.add_widget(igual_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ''
            #limpa o widget solution
        else:

         if current and (self.last_was_operator and button_text in self.operators):
            #não adiciona dois operadores ao mesmo tempo
            return

         elif current == "" and button_text in self.operators:
                #o primeiro caracter não pode ser um operador

            return

         else:
            new_text = current + button_text
            self.solution.text = new_text
            self.last_button = button_text
            self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

        if text == '0+6':
            self.solution.text = 'O Caio é legal'



app = MainApp()
app.run()

