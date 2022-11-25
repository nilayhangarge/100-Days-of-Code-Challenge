class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list

    def next_question(self):
        # 'list' is not callable = check the name and parenthesis
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        # asking the questions
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")


# checking if the answer was correct
# checking if we're the end of the quiz
