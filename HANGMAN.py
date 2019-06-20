import turtle
poly=turtle.Turtle()
poly.speed(50)
poly.hideturtle()

#making gallows
poly.left(90)
poly.penup()
poly.forward(90)
poly.pendown()
poly.forward(10)
poly.left(90)
poly.forward(30)
poly.left(90)
poly.forward(100)
poly.right(90)
poly.forward(30)
poly.backward(60)
poly.left(180)

#the users word and list
word=str(input("Please enter a word")).lower()
listerino=list(word)

#making correct lines
poly.pensize(.5)
poly.penup()
poly.setpos(-110,-31)
poly.write("Correct:")
poly.forward(40)
poly.pendown()
for i in range(len(word)):
  poly.forward(10)
  poly.penup()
  poly.forward(5)
  poly.pendown()

#making incorrect lines
poly.penup()
poly.setpos(-110, 129)
poly.write("Incorrect:")
poly.forward(50)
poly.pendown()
for i in range(6):
  poly.forward(10)
  poly.penup()
  poly.forward(5)
  poly.pendown()
poly.pensize(1)

# the huge function
def hangman():
  wrong=0
  right=0
  for i in range(26):
    guess=str(input("Guess a letter"))
    poly.setheading(0)
    if guess in listerino:
      poly.penup()
      poly.setpos(-110,-30)
      poly.forward(40)
      poly.forward((listerino.index(guess))*15)
      poly.write(guess)
      poly.forward((listerino.index(guess))*15)
      guess1=guess
      guess2=guess1
      guess3=guess2
      guess4=guess3
      listerino[listerino.index(guess)]=str("ANSWERED")
      right=right+1
      if right==len(word):
        print("Congratulations")
        break
      if guess1 in listerino:
        poly.penup()
        poly.setpos(-110,-30)
        poly.forward(40)
        poly.forward((listerino.index(guess1))*15)
        poly.write(guess)
        poly.forward((listerino.index(guess1))*15)
        listerino[listerino.index(guess1)]=str("ANSWERED")
        right=right+1
        if right==len(word):
          print("Congratulations")
          break 
      if guess2 in listerino:
        poly.penup()
        poly.setpos(-110,-30)
        poly.forward(40)
        poly.forward((listerino.index(guess2))*15)
        poly.write(guess)
        poly.forward((listerino.index(guess2))*15)
        listerino[listerino.index(guess2)]=str("ANSWERED")
        right=right+1
        if right==len(word):
          print("Congratulations")
          break 
      if guess3 in listerino:
        poly.penup()
        poly.setpos(-110,-30)
        poly.forward(40)
        poly.forward((listerino.index(guess3))*15)
        poly.write(guess)
        poly.forward((listerino.index(guess3))*15)
        listerino[listerino.index(guess3)]=str("ANSWERED")
        right=right+1
        if right==len(word):
          print("Congratulations")
          break
      if guess4 in listerino:
        poly.penup()
        poly.setpos(-110,-30)
        poly.forward(40)
        poly.forward((listerino.index(guess4))*15)
        poly.write(guess)
        poly.forward((listerino.index(guess4))*15)
        listerino[listerino.index(guess4)]=str("ANSWERED")
        right=right+1
        if right==len(word):
          print("Congratulations")
          break 
    else:
      poly.penup()
      poly.setpos(-60,130)
      poly.setheading(0)
      poly.forward(15*(wrong))
      poly.write(guess)
      poly.forward(10*(wrong))
      poly.pendown()
      if (wrong==0):
        poly.penup()
        poly.setpos(0,75)
        poly.pendown()
        for i in range(30):
          poly.forward(1)
          poly.left(12)
      if (wrong==1):
        poly.penup()
        poly.setpos(5,75)
        poly.pendown()
        poly.right(90)
        poly.forward(30)
        poly.backward(30)
      if (wrong==2):
        poly.penup()
        poly.setpos(5,75)
        poly.pendown()
        poly.right(300)
        poly.backward(20)
        poly.forward(20)
        poly.left(300)
      if (wrong==3):
        poly.penup()
        poly.setpos(5,75)
        poly.pendown()
        poly.left(100)
        poly.backward(20)
        poly.forward(20)
        poly.right(100)
      if (wrong==4):
        poly.penup()
        poly.setpos(5,45)
        poly.pendown()
        poly.right(280)
        poly.backward(20)
        poly.forward(20)
        poly.left(280)
      if (wrong==5):
        poly.penup()
        poly.setpos(5,45)
        poly.pendown()
        poly.left(100)
        poly.backward(20)
        poly.forward(20)
        poly.right(100)
        print("You lose")
        break
      wrong=wrong+1
hangman()




