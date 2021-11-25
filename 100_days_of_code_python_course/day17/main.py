from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []

for q in question_data:
    questions.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(questions)

while quiz.not_ends():
    quiz.next_question()

print("You've completed the quiz!")
print(f'Your final score was: {quiz.total_score}.')
