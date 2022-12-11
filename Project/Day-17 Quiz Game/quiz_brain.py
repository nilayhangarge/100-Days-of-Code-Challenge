class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    # checking if we're the end of the quiz
    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        # 'list' is not callable = check the name and parenthesis
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        # asking the questions
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
