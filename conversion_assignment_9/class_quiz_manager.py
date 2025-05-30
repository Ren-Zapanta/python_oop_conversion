import os

class QuizManager:
    def __init__(self, file_path):
        self.quiz_data = {
            "question": "",
            "choices": {"A": "", "B": "", "C": "", "D": ""},
            "answer": ""
        }
        self.input_stage = "question"
        self.file_path = file_path

    def process_input(self, user_input):
        if self.input_stage == "question":
            self.quiz_data["question"] = user_input
            self.input_stage = "choice_A"
            return "Enter choice A: "
        elif self.input_stage == "choice_A":
            self.quiz_data["choices"]["A"] = user_input
            self.input_stage = "choice_B"
            return "Enter choice B: "
        elif self.input_stage == "choice_B":
            self.quiz_data["choices"]["B"] = user_input
            self.input_stage = "choice_C"
            return "Enter choice C: "
        elif self.input_stage == "choice_C":
            self.quiz_data["choices"]["C"] = user_input
            self.input_stage = "choice_D"
            return "Enter choice D: "
        elif self.input_stage == "choice_D":
            self.quiz_data["choices"]["D"] = user_input
            self.input_stage = "answer"
            return "Enter the correct answer (A, B, C, or D): "
        elif self.input_stage == "answer":
            self.quiz_data["answer"] = user_input.upper()
            self.save_to_file()
            self.input_stage = "confirm_continue"
            return "Do you want to input another question? (Y/N): "
        elif self.input_stage == "confirm_continue":
            if user_input.lower() == "y":
                self.quiz_data = {
                    "question": "",
                    "choices": {"A": "", "B": "", "C": "", "D": ""},
                    "answer": ""
                }
                self.input_stage = "question"
                return "Please enter a question: "
            elif user_input.lower() == "n":
                return "exit"
            else:
                return "Invalid input. Please type Y or N:"

    def save_to_file(self):
        with open(self.file_path, "a") as file:
            file.write("Question: " + self.quiz_data["question"] + "\n")
            for key in ["A", "B", "C", "D"]:
                file.write(f"{key}. {self.quiz_data['choices'][key]}\n")
            file.write("Answer: " + self.quiz_data["answer"] + "\n\n")