class Question:
    def __init__(self, text, answer):
        self._text = text
        self._answer = answer

    @property
    def text(self):
        return self._text

    @property
    def answer(self):
        return self._answer

