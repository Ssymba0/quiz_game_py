from termcolor import colored
class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0
        print("-----------Welcome to QuizBrain---------", end = "\n")
        answer = None
        while answer not in ("yes", "no"): 
            answer = input(f"There's a total of {len(self.question_list)} questions\
 do you wanna play?: (Yes/No)\n>>").lower() 
            if answer == "yes" or answer == "y": 
                break 
            elif answer == "no" or answer == "n":
                exit(0)
            else: 
                print("Please enter yes or no.")
        
    def still_has_question(self):
        return self.question_num < len(self.question_list)
    
    def get_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1 
        user_answer = input(f"Q.{self.question_num}:{question.text}(True/False)?:\n>>")
        self.check_answer(user_answer, question.answer)
        if not self.still_has_question():
            print("\n---You have completed the game---\n-------------")
            print(colored(f'Your final score is {self.score}/{len(self.question_list)}', "green", attrs=['dark', 'bold']))
        while self.still_has_question():
            self.get_question()

    def check_answer(self, user_answer, correct_answer):
        if user_answer == "give up" or user_answer == "quit" or user_answer == "exit":
            exit("You gave up! :(")
        elif user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(colored("Correct answer", "green"))
        else : 
            print(colored("Invalid answer", "red"))
            print(colored(f"Correct answer is: {correct_answer.lower()}", "green"))
        print(colored("Your score is: ", "cyan"), colored(f"{self.score}/{len(self.question_list)}", "blue"))