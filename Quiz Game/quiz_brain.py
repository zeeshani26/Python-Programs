class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.q_number < len(self.q_list):
            return True
        else:
            print(f"Your final score is: {self.score}/{len(self.q_list)}")

    def next_question(self):
        new_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number} {new_question.text} (True/False)")
        self.check_answer(user_answer, new_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right")
            self.score += 1
        else:
            print("You are wrong!")
        print(f"The correct answer is {correct_answer}")
        if self.q_number < len(self.q_list):
            print(f"Your current score is {self.score}/{self.q_number}\n")
