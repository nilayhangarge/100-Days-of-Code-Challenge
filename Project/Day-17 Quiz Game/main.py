from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
    # Create objects for text, answer
    question_text = key["text"]
    question_answer = key["answer"]

    # Pass these objects to Question class
    new_question = Question(question_text, question_answer)

    # Append that class entries
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
