from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
from ui import Ui_tkinter
from tkinter import *
from tkinter import simpledialog, messagebox, colorchooser
import requests
#-----------------------------filling the data with the help of an API-------------------------------

#collect number of questions in data
no_of_ques = simpledialog.askinteger(title="Hellllo!", prompt="Enter The No. of questions you want to play quiz on! 10 Questions are default, if no entries are recieved. Every Game New Questions are refreshed, But max to max the no. of questions can be 50 :(((") 
print(no_of_ques)
if no_of_ques == 0 or no_of_ques == None:
    no_of_ques = 10
elif no_of_ques > 50:
    no_of_ques = 50    
parameter={
    "amount":no_of_ques,
    "type":"boolean"
}
print(parameter)

#-----------Get the color for GUI-------------
selected_color = colorchooser.askcolor()
print(selected_color)
if selected_color == (None, None):
    selected_color = ("rgb(55,83,98)", "#375362")

#getting the data from api
response = requests.get(url="https://opentdb.com/api.php", params=parameter)
new_data = response.json()
question_data = new_data["results"]
print(question_data)
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# quiz = QuizBrain(question_bank)
quiz = Ui_tkinter(question_bank, no_of_ques, selected_color[1])
quiz.create_ui()


