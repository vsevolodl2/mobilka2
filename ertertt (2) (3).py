from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import BooleanProperty
from kivy.vector import Vector
import numpy as np
from kivy.properties import BooleanProperty, NumericProperty, ObjectProperty
#from sympy import symbols, Eq, solve
from kivy.core.window import Window
import socket

class JoystickWidget(Image):
    is_touched = BooleanProperty(False)
    instance = None
    handle = ObjectProperty(None)
    move_radius = NumericProperty(0)

    




    def on_touch_down(self, touch):
        print("Палец касается джойстика")
        # Получаем координаты касания и центра экрана
        touch_x, touch_y = touch.pos

        screen_widgth=Window.width
        screen_height=Window.height

        center_x = screen_widgth/2
        center_y = screen_height/2





        screen_center_x, screen_center_y = (center_x, center_y)  # Используем центр экрана
    
        distance = ((touch_x - screen_center_x)**2 + (touch_y - screen_center_y)**2) ** 0.5
    
        # Устанавливаем порог для приемлемого расстояния от центра
        threshold_distance = 100  # Пример порога 50 (подберите подходящее значение)
    
        if distance <= threshold_distance:
            # Джойстик достаточно близко к центру
            self.center = touch.pos
            self.is_touched = True
        else:
            # Джойстик слишком далеко от центра
            print("Джойстик слишком далеко от центра, касание отклонено")








        print("Положение джойстика в конце работы приложения:")
        joystick = self.center
        print("x:", self.center_x)
        print("y:", self.center_y)




        def is_connection_established():
            return client_socket is not None



        # Детали сервера
        #server_ip = '192.168.241.114'
        #server_port = 80
        
        # Взаимодействие по сокетам
        #client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        #if  client_socket.connect_ex((server_ip,server_port)) ==0:

         #   if is_connection_established():
          #      client_socket.send(str(self.center).encode())
           # else:
           #     client_socket.connect((server_ip, server_port))

        #else:
         #   print("ошибка")
    
        #return super(JoystickWidget, self).on_touch_down(touch)








    

    def on_drag(self, touch):
       input_position = touch.pos
       offset = Vector(input_position) - Vector(self.handle.center)
       offset = offset.normalize() * self.move_radius
       handle_position = Vector(self.handle.center) + offset
    
       self.handle.x = handle_position.x
       self.handle.y = handle_position.y





    def on_touch_move(self, touch):
        #x, y = symbols('x y')

        x0 = 0
        x1 = 0
        y0 = 0
        y1 = 0 



        print("Палец касается джойстика")
        # Получаем координаты касания и центра экрана
        input_position = touch.pos
        touch_x, touch_y = touch.pos

        screen_widgth=Window.width
        screen_height=Window.height


        center_x = screen_widgth/2
        center_y = screen_height/2


        screen_center_x, screen_center_y = (center_x, center_y)  # Используем центр экрана
    
        distance = ((touch_x - screen_center_x)**2 + (touch_y - screen_center_y)**2) ** 0.5
    
        # Устанавливаем порог для приемлемого расстояния от центра
        threshold_distance = 100  # Пример порога 50 (подберите подходящее значение)
        if self.is_touched:
            vector = Vector(touch.pos) - Vector(self.center)
            if distance <= threshold_distance:
                self.center = touch.pos
            else:
                #vector = Vector(touch.pos) - Vector(screen_center_x, screen_center_y)
                #self.center = Vector(self.center) + vector.normalize()
                touch_x, touch_y = touch.pos
                screen_widgth=Window.width
                screen_height=Window.height

                center_x = screen_widgth/2
                center_y = screen_height/2

                #vector = Vector(touch.pos) - Vector(screen_center_x, screen_center_y)
                #self.center = Vector(self.center) + vector.normalize()
                #eq_line = Eq(x*(touch_x-center_x), y*(touch_y-center_y))  # Уравнение прямой отрезка
                #eq_circle = Eq((x)**2 + (y)**2, 10000)  # Уравнение окружности


                
                
                y0=-(100)/((((touch_y-center_y)**2)/(touch_x-center_x)**2+1)**0.5)
                y1=-y0

                x0=((touch_y-center_y)*y0)/(touch_x-center_x)
                x1=-x0




                #intersection = solve((eq_line , eq_circle), (x, y))

                #intersection_float1 = [float(point[0]) for point in intersection]

                #intersection_float2 = [float(point[1]) for point in intersection]




                #if touch_y <= center_y:
                 #   self.center = (-intersection_float2[1] + center_x, intersection_float1[0] + center_y)
                #else:
                 #   self.center = (-intersection_float2[0] + center_x, intersection_float1[1] + center_y)

                if touch_x <= center_x:
                    self.center = (-y1 + center_x, -x1 + center_y)
                else:
                    self.center = (-y0 + center_x, -x0 + center_y)













                print(":", touch.pos)
                



        return super(JoystickWidget, self).on_touch_move(touch)



    def on_touch_up(self, touch):
        self.center = self.parent.center
        self.is_touched = False
        return super(JoystickWidget, self).on_touch_up(touch)



    def send_coordinates(self, instance):

        coordinates = (joystick.center_x, joystick.center_y)

        # Детали сервера
        server_ip = '192.168.1.100'
        server_port = 12345
        
        # Взаимодействие по сокетам
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        client_socket.send(str(coordinates).encode())
        client_socket.close()












class JoystickApp(App):
    def build(self):
        layout = FloatLayout()
        size = 200

        def draw_circle():
            # Очистка холста
            border.canvas.clear()

            # Рисование круга в центре
            center_x, center_y = layout.center
            with border.canvas:
                Color(0.5, 0.5, 0.5, 0.5)
                Ellipse(pos=(center_x - size/2, center_y - size/2), size=(size, size))







        border = Widget(size=(size, size))
        layout.add_widget(border)

        draw_circle()  # Изначальное рисование круга

        # Обработка касаний экрана
        def on_touch_down(instance, touch):
            draw_circle()  # При каждом касании экрана рисуем круг заново

        layout.bind(on_touch_down=on_touch_down)


        joystick = JoystickWidget(source='joystick_image.png', size_hint=(None, None), size=(100, 100))
        joystick.center = layout.center
        layout.add_widget(joystick)

 

        return layout








    def on_touch_down(self):
        print("Положение джойстика в конце работы приложения:")
        joystick = self.root.children[1]
        print("x:", joystick.center_x)
        print("y:", joystick.center_y)
        client_socket.close()

if __name__ == '__main__':
    JoystickApp().run()