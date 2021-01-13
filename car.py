import turtle as t
import random

class myCar:
        name='car'
        def __init__(self,name):
                self.name = name
                print("운전을 시작하겠습니다.")
                t.seth(random.randint(0,180))
        def foward(self):
                print(self.name,"(이)가 전진합니다.")
                t.fd(10)
        def left(self):
                print(self.name,"(이)가 좌회전합니다.")
                t.left(5)
        def right(self):
                print(self.name,"(이)가 우회전합니다.")
                t.right(5)
        def automode(self):
                print(self.name,"(이)가 *자율주행*을 시작합니다.")
                while True:
                    auto = random.choice(['foward','left','right'])
                    if auto == 'foward':
                        self.foward()
                    elif auto == 'right':
                        self.right()
                    else:
                        self.left()
                    pass
my_car = myCar('진준엽의 차')

t.listen()

t.onkeypress(my_car.foward,"Up")
t.onkeypress(my_car.left, "Left")
t.onkeypress(my_car.right, "Right")
t.onkeypress(my_car.automode,'r')
