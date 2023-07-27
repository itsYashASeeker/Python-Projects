class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        your_ans = input(f"Q.{self.question_number} {current_question.text} (True/False)? ").lower().capitalize()
        print(f"Your answer:- {your_ans}")
        print(f"Correct answer:- {current_question.answer}")
        self.check_answer(your_ans, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans==correct_ans:
            self.score+=1
            print("You got it Right!!")
            print(f"Your score:- {self.score}/{self.question_number}")
        else:
            print('You got it wrong.')
            print(f"Your score:- {self.score}/{self.question_number}")




