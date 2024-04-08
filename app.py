import tkinter as tk
from tkinter import ttk, messagebox
from read import get_questions

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("400x200")

        self.category_label = tk.Label(root, text="Select a category:")
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(root, textvariable=self.category_var, values=["geography", "history", "accounting", "math", "programming"])
        self.category_combobox.pack()

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        category = self.category_var.get()
        if not category:
            messagebox.showerror("Error", "Please select a category.")
            return

        self.root.destroy()

        quiz_window = tk.Tk()
        quiz_window.title("Quiz")
        quiz_window.geometry("600x400")

        questions = get_questions(category)
        self.create_question_widgets(quiz_window, questions)

    def create_question_widgets(self, window, questions):
        feedback_labels = []
        for i, question_data in enumerate(questions):
            question_label = tk.Label(window, text=f"Question {i+1}: {question_data[1]}")
            question_label.pack()

            choices = [question_data[2], question_data[3], question_data[4], question_data[5]]
            answer = question_data[6]

            choice_var = tk.StringVar()
            choice_combobox = ttk.Combobox(window, textvariable=choice_var, values=choices)
            choice_combobox.pack()

            feedback_label = tk.Label(window, text="")
            feedback_label.pack()
            feedback_labels.append(feedback_label)

            submit_button = tk.Button(window, text="Submit", command=lambda ans=answer, choice=choice_var, fb=feedback_label: self.check_answer(ans, choice, fb))
            submit_button.pack()

    def check_answer(self, answer, choice, feedback_label):
        if choice.get() == answer:
            feedback_label.config(text="Correct!", fg="green")
        else:
            feedback_label.config(text="Incorrect!", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()