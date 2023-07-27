from tkinter import *
from tkinter import messagebox
import html
class Ui_tkinter:
    def __init__(self, questions, no_of_ques_tk, color):
        self.THEME_COLOR = color
        self.window = Tk()
        self.window.config(padx=20, pady=20)
        self.window.config(bg=self.THEME_COLOR)
        self.window.minsize(width=260, height=300)
        self.window.resizable(width=False, height=False)
        self.question_list_tkinter = questions
        self.score = 0
        self.question_no = 0
        self.no_of_ques_tk = no_of_ques_tk 
        self.MULTIPLE_FOR_GRAPH = 360/no_of_ques_tk  
    def questions_left(self):
        if self.question_no == (self.no_of_ques_tk):
            return False 
        else:
            return True    
    def update_question(self, question_lists):
        self.question_no += 1
        if self.questions_left():
            current_question_tkinter = question_lists[self.question_no]
            question_text_tk = html.unescape(current_question_tkinter.text)
            self.canvas.itemconfig(self.question_text, text=f"Q{self.question_no+1}. {question_text_tk}")
        else:
            messagebox.showinfo(title="QuizGame", message=f"Thank you for Playing QuizBrain! Your Final Score is {self.score}/{self.no_of_ques_tk}")    
            self.window.quit()
    def false_response(self):
        self.correct_answer_check = self.question_list_tkinter[self.question_no].answer
        if self.correct_answer_check == "False":
            self.score += 1
            self.score_board.config(text=f"Score: {self.score}/{self.no_of_ques_tk}")
            self.graph_score(self.score)
        self.update_question(self.question_list_tkinter)
    def true_response(self):
        self.correct_answer_check = self.question_list_tkinter[self.question_no].answer
        if self.correct_answer_check == "True":
            self.score += 1 
            self.score_board.config(text=f"Score: {self.score}/{self.no_of_ques_tk}") 
            self.graph_score(self.score)
        self.update_question(self.question_list_tkinter)

    def graph_score(self, score_for_graph):
        #graph for score
        self.graph_canvas = Canvas(width=100, height=100, bg=self.THEME_COLOR, highlightthickness=0)
        coord = 0, 0, 100, 100
        arc = self.graph_canvas.create_oval(coord, fill="red")
        if score_for_graph == self.no_of_ques_tk:
            self.graph_canvas.itemconfig(arc, fill="green")
        elif score_for_graph > 0:
            arc2 = self.graph_canvas.create_arc(coord, start=0, extent=score_for_graph*self.MULTIPLE_FOR_GRAPH, fill="green")
        self.graph_canvas.grid(row=0, column=0)

    def create_ui(self):
        #graph for score
        self.graph_score(self.score)
        #score_board
        self.score_board = Label(bg=self.THEME_COLOR, text=f"Score: {self.score}/{self.no_of_ques_tk}", font=("Arial", 20, "normal"), fg="white")
        self.score_board.grid(row=0, column=1, sticky=E)
        #question
        first_question = self.question_list_tkinter[self.question_no]
        first_question_text_tk = html.unescape(first_question.text)
        #canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text=f"Q{self.question_no+1}. {first_question_text_tk}", 
                                                     fill=self.THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #cross_button
        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, command=self.false_response, highlightthickness=0, relief='ridge')
        self.false_btn.grid(row=2, column=0)

        #correct_button
        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, command=self.true_response, highlightthickness=0, relief='ridge')
        self.true_btn.grid(row=2, column=1)


        self.window.mainloop()


