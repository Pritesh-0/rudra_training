import turtle

window = turtle.Screen()
window.bgcolor('dark salmon')
window.tracer(0)


player = turtle.Turtle()
player.shape('turtle')
player.color('turquoise')
player.penup()


def turn_left():
  player.color('light green')
  player.left(10)
  
def turn_right():
  player.color('light blue')
  player.right(10)
  
def fwd():
  player.color('light green')
  player.forward(10)
  
def fwd():
  player.color('light green')
  player.backward(10)

window.onkeypress(turn_left, "Left")
window.onkeypress(turn_right, "Right")
window.listen()


while True:
  player.forward(0.0)
  window.update()
  

