import unittest
from model.quiz import Quiz

class TestQuiz (unittest.TestCase):
    name_quiz = 'Teste quiz'
    new_name_quiz = 'Quiz Teste'

    quiz = Quiz(name_quiz, [])

    def test_name_of_quiz(self):
        self.assertEqual(self.quiz.name, self.name_quiz)

    def test_set_name_quiz(self):
        self.quiz.name = self.new_name_quiz
        self.assertEqual(self.quiz.name, self.new_name_quiz)

    def test_finished(self):
        self.assertEqual(self.quiz.valid_is_finished(), True)

if __name__ == '__main__':
    unittest.main()