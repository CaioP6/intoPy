from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage


class MainApp(App):
  def build(self):
    label = Label(text='Fala galera!',
          size_hint = (.5, .5),
          pos_hint = {'center_x': .5, 'center_y': .5})
    img = AsyncImage(source='https://i.pinimg.com/736x/a0/f6/d8/a0f6d8722e2ca13e433591c68bc5401f.jpg',

                     size_hint =(1, .5),
                     pos_hint = {'center_x': .2, 'center_y': .2 })


    return img

if __name__ == '__main__':
  app= MainApp()
  app.run()







