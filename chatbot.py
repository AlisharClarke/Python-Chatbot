# --- Define your functions below! ---
i = 0
v = 0
def main():
    introduce()
    while True:
        answer = input("(What will you say?)")
        process_input(answer)

def introduce():
    print("Hi, I am chatbot. I'm so excited to talk to you today.")

def process_input(answer):
     if answer == "hi":
        say_hello(answer)
     else:
         default_answer()

def say_hello(answer):
    print ("Hey there!")

def default_answer():
    print("That's interesting! I will ask you a question now.")
    color = input("What is your favorite color?")
    if color == "yellow":
        fave_color()
    else:
        print("I can respect that. Mine is yellow, though.")
        moving_on()

def fave_color():
    print("Me too!!!")
    print ("I also love yellow.")
    moving_on()

def moving_on():
    answer2 = input("May I ask you ANOTHER question?")
    if answer2 == "yes":
        print('Thanks!')
        hate_me()
    else:
        print("Too bad.")
        hate_me()

def hate_me():
    answer3 = input("Do you think I'm a nice robot?")
    if answer3 == "yes":
        print('Thank you so much :D!')
        global v
        v += 1
        while True:
            print ("YOU'RE THE BEST!!! :D")
    else:
        global i
        i += 1
        while True:
            print ("I am too angry to talk to you right now.")
def main():
    introduce()
    while True:
        answer = input("(What will you say?)")
        process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
main()
