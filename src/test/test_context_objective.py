# -*- coding: UTF-8 -*-
import unittest
from helper import Context 
from helper import ConcreteStrategyEvaluatorObjectives

from model.factory_question import FactoryQuestion 
from model.quiz import Quiz 

class TestContextObjective(unittest.TestCase):

    def test_context_objective_not_assert(self):
        Main_Quiz_1 = Quiz('Formulário sabidão!', [
            FactoryQuestion.create_multiple_choice_question('2 + 2 = ', [
                FactoryQuestion.create_objective_responses('2'),
                FactoryQuestion.create_objective_responses('3'),
                FactoryQuestion.create_objective_responses('4', True),
                FactoryQuestion.create_objective_responses('5')
            ]),
            
            FactoryQuestion.create_multiple_choice_question('Quem conquistou o Brasil', [
                FactoryQuestion.create_objective_responses('Mc pedrinho'),
                FactoryQuestion.create_objective_responses('Nego ney'),
                FactoryQuestion.create_objective_responses('Pedro Alvares Cabra', True),
                FactoryQuestion.create_objective_responses('Xup')
            ]),
        ])
        self.assertEqual(0, Context(ConcreteStrategyEvaluatorObjectives(Main_Quiz_1)).start())

    def test_context_objective_assert_one(self):
        nota_esperada = 1

        Main_Quiz_1 = Quiz('Formulário sabidão!', [
            FactoryQuestion.create_multiple_choice_question('2 + 2 = ', [
                FactoryQuestion.create_objective_responses('2'),
                FactoryQuestion.create_objective_responses('3'),
                FactoryQuestion.create_objective_responses('4', True),
                FactoryQuestion.create_objective_responses('5')
            ]),
            
            FactoryQuestion.create_multiple_choice_question('Quem conquistou o Brasil', [
                FactoryQuestion.create_objective_responses('Mc pedrinho'),
                FactoryQuestion.create_objective_responses('Nego ney'),
                FactoryQuestion.create_objective_responses('Pedro Alvares Cabra', True),
                FactoryQuestion.create_objective_responses('Xup')
            ]),
        ])


        Main_Quiz_1.set_answer(1, 3)        
        self.assertEqual(nota_esperada, Context(ConcreteStrategyEvaluatorObjectives(Main_Quiz_1)).start())

    def test_context_objective_assert_all(self):
        lista_de_perguntas = [
            FactoryQuestion.create_multiple_choice_question('2 + 2 = ', [
                    FactoryQuestion.create_objective_responses('2'),
                    FactoryQuestion.create_objective_responses('3'),
                    FactoryQuestion.create_objective_responses('4', True),
                    FactoryQuestion.create_objective_responses('5')
                ]),

                FactoryQuestion.create_multiple_choice_question('5 + 5 = ', [
                    FactoryQuestion.create_objective_responses('10', True),
                    FactoryQuestion.create_objective_responses('10', True),
                    FactoryQuestion.create_objective_responses('10', True),
                    FactoryQuestion.create_objective_responses('10', True)
                ]),

                FactoryQuestion.create_multiple_choice_question('Quem conquistou o Brasil', [
                    FactoryQuestion.create_objective_responses('Mc pedrinho'),
                    FactoryQuestion.create_objective_responses('Nego ney'),
                    FactoryQuestion.create_objective_responses('Pedro Alvares Cabral', True),
                    FactoryQuestion.create_objective_responses('Xup')
                ])
        ]
        
        Main_Quiz_1 = Quiz('Formulário sabidão!', lista_de_perguntas)
        
        Main_Quiz_1.set_answer(1, 3)
        Main_Quiz_1.set_answer(2, 1)
        Main_Quiz_1.set_answer(3, 3)

        self.assertEqual(len(Main_Quiz_1.list_of_question), Context(ConcreteStrategyEvaluatorObjectives(Main_Quiz_1)).start())

if __name__ == '__main__':
    unittest.main()