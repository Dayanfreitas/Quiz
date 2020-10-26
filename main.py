# -*- coding: UTF-8 -*-
from quiz import Quiz
from abc import ABC
from factory_question import FactoryQuestion


class Context:
    def __init__ (self, Strategy):
        self._strategy = Strategy

    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, Strategy):
        self._strategy = strategy

    def start(self):
        return self._strategy.do_algorithm()

class Strategy:
    def __init__(self, Quiz):
        self.quiz = Quiz
    
    def do_algorithm(self):
        pass

class ConcreteStrategyEvaluatorMultiple(Strategy):
    
    def do_algorithm(self):
        """Algoritmo de avalição de multiplas escolhas baseadas no peso de cada resposta e 
            quantidade de perguntas
        """

        list_of_question = self.quiz.list_of_question
        sum_of_weights = 0
        for question in list_of_question:
            answer = question.get('answer')
            if answer: 
                sum_of_weights += float(answer.get('weight'))

        return sum_of_weights/len(list_of_question)

class ConcreteStrategyEvaluatorObjectives(Strategy):
    @staticmethod
    def filter_correct_answers(question):
        return question.get('answer').get('value')

    def do_algorithm(self):
        """Algoritmo de avalição de objetivas
            faz um filtro nas respostas certas
        """
        list_of_question = self.quiz.list_of_question
        size_list_of_question = len(list_of_question)

        list_correct_answers = filter(self.filter_correct_answers, list_of_question)
        size_list_correct_answers = len(list_correct_answers)
        
        return size_list_of_question - size_list_correct_answers

list_of_questions_objetivo = [
    FactoryQuestion.create_multiple_choice_question('2 + 2 = ', [
        FactoryQuestion.create_multiple_choice_answer('2', False),
        FactoryQuestion.create_multiple_choice_answer('3', False),
        FactoryQuestion.create_multiple_choice_answer('4', True),
        FactoryQuestion.create_multiple_choice_answer('5',False)
    ]),
    FactoryQuestion.create_multiple_choice_question('Quem conquistou o Brasil', [
        FactoryQuestion.create_multiple_choice_answer('Mc pedrinho', False),
        FactoryQuestion.create_multiple_choice_answer('Nego ney', False),
        FactoryQuestion.create_multiple_choice_answer('Pedro Alvares Cabra', True),
        FactoryQuestion.create_multiple_choice_answer('Xup', False)
    ])
]

list_of_question = [
    FactoryQuestion.create_multiple_choice_question('Você encontra um morador de rua que te pede comida...', [
        FactoryQuestion.create_multiple_choice_answer('Pago um lanche para ele', 1),
        FactoryQuestion.create_multiple_choice_answer('Falo que também sou morador de rua', 5),
        FactoryQuestion.create_multiple_choice_answer('Ignoro e vou embora', 10)
    ]),
    FactoryQuestion.create_multiple_choice_question('Uma pessoa caí do seu lado...', [
        FactoryQuestion.create_multiple_choice_answer('Pergunto se ela está bem e ajudo ela', 1),
        FactoryQuestion.create_multiple_choice_answer('Rio dela', 5),
        FactoryQuestion.create_multiple_choice_answer('Finjo que não vi', 10)
    ]),
    FactoryQuestion.create_multiple_choice_question('Um estranho pede seu celular emprestado para fazer uma ligação internacional... (Obs: você possuí créditos no celular)', [
        FactoryQuestion.create_multiple_choice_answer('Falo que não vou emprestar', 1),
        FactoryQuestion.create_multiple_choice_answer('Empresto o celular para ela', 5),
        FactoryQuestion.create_multiple_choice_answer('Saio correndo', 10)
    ]),
    FactoryQuestion.create_multiple_choice_question('Uma pessoa te pede informação sobre a localização de um estabelecimento... (Obs: você sabe a localização)', [
        FactoryQuestion.create_multiple_choice_answer('Explico para ela como chegar', 1),
        FactoryQuestion.create_multiple_choice_answer('Passo um caminho errado', 5),
        FactoryQuestion.create_multiple_choice_answer('Falo que não conheço o lugar', 10)
    ]),
    FactoryQuestion.create_multiple_choice_question('Quando você está cansando, você quer...', [
        FactoryQuestion.create_multiple_choice_answer('Descansar/dormir', 1),
        FactoryQuestion.create_multiple_choice_answer('Trabalhar', 5),
        FactoryQuestion.create_multiple_choice_answer('Esperar o cansaço passar', 10)
    ])
]


if __name__ == "__main__":
    Main_Quiz_1 = Quiz('Formulário sabidão!', list_of_questions_objetivo)
    Main_Quiz_1.start()
    Main_Quiz_2 = Quiz('Questionario de pessoas boas "!', list_of_question) 
    Main_Quiz_2.start()
    
    value_form_1 = Context(ConcreteStrategyEvaluatorObjectives(Main_Quiz_1)).start()
    value_form_2 = Context(ConcreteStrategyEvaluatorObjectives(Main_Quiz_2)).start()

    # print("Valor do Formulário :" + str(Context(ConcreteStrategyEvaluatorObjectives(Main_Quiz_1)).start()))
    # print("Valor do Formulário: " + str(Context(ConcreteStrategyEvaluatorMultiple(Main_Quiz_2)).start()))