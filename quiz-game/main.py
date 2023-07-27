from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_q = QuizBrain(question_bank)
while quiz_q.still_has_questions():
    quiz_q.next_question()
print(f"You completed the Quiz!\nYour Final Score:- {quiz_q.score}/{quiz_q.question_number}")
