import random
x=input('Do you want to start?: yes or no ')
while x=="yes":
    Name=input('What is your name? ')
    question=input("What is your question? ")
    answer=''
    random_number=random.randint(1,9)
    if random_number == 1:
      answer="Yes-definitely"
    elif random_number ==2:
      answer="It is decidedly so"
    elif random_number ==3:
      answer="Without a doubt"
    elif random_number ==4:
       answer="Reply hazy, try again"
    elif random_number ==5:
       answer="Ask again later"
    elif random_number ==6:
       answer="Better not tell you now"
    elif random_number ==7:
       answer="My sources say no"
    elif random_number ==8:
       answer="Outlook not so good"
    elif random_number ==9:
      answer="Very doubtful"
    else:
      answer="Error"
    print(Name,"asks:",question,"?")
    print("The magic 8-balls answer is",answer)
    x=input('Do you want to start again yes or no ')
else:
    print("Thank you for using")

