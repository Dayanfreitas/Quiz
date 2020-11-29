import unittest
from model.factory_question import FactoryQuestion

class TestQuestion(unittest.TestCase):
    description = '2 + 2'
    question = FactoryQuestion.create_multiple_choice_question(description, [
        FactoryQuestion.create_multiple_choice_answer('4', 0),
        FactoryQuestion.create_multiple_choice_answer('5', 0),
        FactoryQuestion.create_multiple_choice_answer('8 - 4', 10)
    ])

    def test_description(self):
        self.assertEqual(self.question.get('description'), self.description)

    def test_not_answer(self):
        self.assertEqual(self.question.get('answer'), None)

if __name__ == '__main__':
    unittest.main()