# TODO: 1. asking the questions
# TODO: 2. checking if the answer was correct
# TODO: 3. checking if we're the end of the quiz


class QuizBrain():
    def __init__(self, question_list):
        self._question_number = 0
        self._questions_list = question_list
        self._score = 0

    def next_question(self):
        question_text = self._questions_list[self._question_number].text
        question_answer = self._questions_list[self._question_number].answer
        self._question_number += 1

        user_answer = input(f'Q.{self._question_number}: {question_text} (True/False): ')

        self.check_answer(user_answer, question_answer)

    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            self._score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f'The correct answer was: {question_answer}.')
        print(f'Your current score is {self._score}/{self._question_number}.')

    def not_ends(self):
        return self._question_number < len(self._questions_list)

    @property
    def total_score(self):
        return f'{self._score}/{len(self._questions_list)}'

