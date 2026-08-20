from random import choice
from random import randint

questions = ["what is 2 + 2 ?","what is 2**3 ?","what is the first element of priodic table?"]

answer_options = [
        ["A. 1","B. 4","C. 3","D. 2"],
        ["A. 8","B. 4","C. 16","D. 32"],
        ["A. oxygen","B. nitrogen","C. carbon dioxide","D. hydrogen"]
        ]
answers = ["B. 4", "A. 8", "D. hydrogen"]

run = True
while run:
    print("wellcome to quiz game")
    print("1. play")
    print("2. settings")
    print("3. exit")
    option = int(input("what would you like to do: "))
    if option == 1:
        play = True
        while play:
            question = choice(questions)
            print()
            print(question)

            question_position = questions.index(question)

            option_number = answer_options[question_position]
            real_answer = answers[question_position]

            position = 0
            for _ in range(4):
                printing_option = option_number[position]
                print(printing_option)
                position += 1

            answer = input("choose from the options: ")
            answer = answer.upper()

            compare = real_answer[:1]
            if compare == answer:
                print("correct")
                print()
            else:
                print("wrong try again later")
                print()
            
            decision = True
            while decision:
                again = input("press enter to play again or type 'back' to go back: ")
                if again == "":
                    play = True
                    decision = False
                elif again == "back":
                    play = False
                    decision = False
                else:
                    print("somthing went wrong plz again")
    elif option == 2:
        setting = True
        while setting:
            print("1. add")
            print("2. remove")
            print("3. back")
            setting_option = int(input("choose from options above: "))
            if setting_option == 1:
                add_question = input("type the question you want to add: ")
                add_option1 = input("type the option 1 you want to add: ")
                add_option2 = input("type the option 2 you want to add: ")
                add_option3 = input("type the option 3 you want to add: ")
                add_option4 = input("type the option 4 you want to add: ")
                add_answer = input("type the answer of the question: ")

                questions.append(add_question)
                answer_options.append([add_option1, add_option2, add_option3, add_option4])
                answers.append(add_answer)
            elif setting_option == 2:
                remove_question = input("write the question you want to remove: ")
                if remove_question in questions:
                    remove_q_position = questions.index(remove_question)
                    questions.pop(remove_q_position)
                    answer_options.pop(remove_q_position)
                    answers.pop(remove_q_position)
                    print("question is removed")
                elif remove_question not in questions:
                    print("there is no such question here")

            elif setting_option == 3:
                setting = False

    elif option == 3:
        print("bye")
        run = False
    elif option > 2 or option < 1:
        print("plz choose between the given options")
        print()
