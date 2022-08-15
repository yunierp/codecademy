import random
import math

name = input("Insert your name: ")
question = input("Ask your question: ")

if question == "":
  print("Please ask something.")
else:
  if name == "":
	  print("The question was: " + question)
  else:
    print(name + " asks: "+ question)
  random_number = random.randint(0,12)
  #print(random_number)

  if random_number == 0:
    answer = ("Error")

  elif random_number == 1:
    answer = ("Yes - definitely.")

  elif random_number == 2:
    answer = ("It is decidedly so.")

  elif random_number == 3:
    answer = ("Without a doubt.")

  elif random_number == 4:
    answer = ("Reply hazy, try again.")

  elif random_number == 5:
    answer = ("Ask again later.")

  elif random_number == 6:
    answer = ("Better not tell you now.")

  elif random_number == 7:
    answer = ("My sources say no.")

  elif random_number == 8:
    answer = ("Outlook not so good.")

  elif random_number == 9:
    answer = ("Very doubtful.")
  else:
    answer = ("Sorry, the random number generator generated a number above 9. I mean - I can't see it because the future lookes misty.")

  print("Magic 8-Ball's answer: " + answer)