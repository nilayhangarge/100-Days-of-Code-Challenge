from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
    # Create objects for text, answer
    question_text = key["question"]
    question_answer = key["correct_answer"]

    # Pass these objects to Question class
    new_question = Question(question_text, question_answer)

    # Append that class entries
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
