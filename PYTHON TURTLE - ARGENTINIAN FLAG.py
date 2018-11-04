import turtle

x = turtle.Screen()
x.bgcolor('dark blue')
x.title('Argentinian Flag - By JM')


jm_turtle = turtle.Turtle()
jm_turtle.speed(8)


# PARTS/SECTIONS OF THE FLAG // PARTES/SECCIONES DE LA BANDERA
def white_rectangle():
    jm_turtle.color('white')
    jm_turtle.begin_fill()
    jm_turtle.left(90)
    jm_turtle.forward(100) 
    jm_turtle.left(90)
    jm_turtle.forward(600)
    jm_turtle.left(90)
    jm_turtle.forward(100) 
    jm_turtle.left(90)
    jm_turtle.forward(300)
    jm_turtle.end_fill()
def blue_rectangle_below():
    jm_turtle.color('sky blue')
    jm_turtle.begin_fill()
    jm_turtle.forward(300)
    jm_turtle.right(90)
    jm_turtle.forward(120) 
    jm_turtle.right(90)
    jm_turtle.forward(600)
    jm_turtle.right(90)
    jm_turtle.forward(120) 
    jm_turtle.right(90)
    jm_turtle.forward(300)
    jm_turtle.end_fill()
def blue_rectangle_above():
    jm_turtle.color('sky blue')
    jm_turtle.begin_fill()
    jm_turtle.forward(120)
    jm_turtle.left(90)
    jm_turtle.forward(600) 
    jm_turtle.left(90)
    jm_turtle.forward(120)
    jm_turtle.left(90)
    jm_turtle.forward(600)
    jm_turtle.end_fill()
def sol_de_mayo():
    jm_turtle.color('gold')
    jm_turtle.begin_fill()
    jm_turtle.circle(20)
    jm_turtle.end_fill()   
def outline():
    jm_turtle.color('black')
    jm_turtle.right(90)
    jm_turtle.forward(220)
    jm_turtle.right(90)
    jm_turtle.forward(600)
    jm_turtle.right(90)
    jm_turtle.forward(340)
    jm_turtle.right(90)
    jm_turtle.forward(600)
    jm_turtle.right(90)
    jm_turtle.forward(120)
def letters():
    jm_turtle.color('white')
    jm_turtle.write("BANDERA ARGENTINA", align="center", font=(None, 16, "bold"))

# IT RUNS THE CODE // ESTO EJECUTA EL CÓDIGO  
jm_turtle.penup()      
jm_turtle.begin_fill()
blue_rectangle_below()
jm_turtle.end_fill()
jm_turtle.forward(300)
white_rectangle()
jm_turtle.forward(300)
jm_turtle.left(90)
jm_turtle.forward(100)
jm_turtle.begin_fill()
blue_rectangle_above()
jm_turtle.end_fill()
jm_turtle.pendown()
outline()
jm_turtle.penup()
jm_turtle.goto(-20,50)
jm_turtle.pendown()
sol_de_mayo()
jm_turtle.penup()
jm_turtle.goto(0,-170)
letters()
jm_turtle.goto(-5,-400)
x.mainloop()





