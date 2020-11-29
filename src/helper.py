# # -*- coding: UTF-8 -*-
import os
import subprocess

class Helper:

    @staticmethod
    def clear():
        if os.name in ('nt', 'dos'):
            subprocess.call("cls")
        elif os.name in ('linux', 'osx', 'posix'):
            subprocess.call("clear")

    @staticmethod
    def new_line(n=1):
        print("\n"*n)

    @staticmethod
    def division(n=1):
        print("="*n)

class Translation:
    def __init__(self):
        pass

    @staticmethod
    def get_label(l):
        translate = {
            'ing': {
                'titulo': 'Title',
                'resposta': 'Answer',
                'nao_finalizado': 'Not Finished',
                'finalizado': 'Finished',
                'pergunta_op': "Which question do you want to answer:",
                'para_pergunta': "For the question",
                'formulario_finalizado' : 'Finished form',
                'qual_sua_resposta':"What's your answer",

                'sair': 'Exit',

                'status': 'Status',

                'vermelho': 'red',
                'verde'   : 'green',
                'azul'    : 'blue',
                'ciano'   : 'cian',
                'magenta' : 'magenta',
                'amarelo' : 'yellow',
                'branco'  : 'white',
                'preto'   : 'black',

                'fundo_vermelho' : 'background_red',
                'fundo_amarelo'  : 'background_yellow',
                'fundo_magenta'  : 'background_magenta',
                'fundo_branco'   : 'background_white',
                'fundo_verde'    : 'background_green',
                'fundo_preto'    : 'background_black',
                'fundo_ciano'    : 'background_cian',
                'fundo_azul'     : 'background_blue',
            }
        }
        lt = translate.get('ing').get(l) 
        
        if lt is not None:
            return lt
        
        return l

class Colored:
    pass

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
        question = question.get('answer')
        
        if question:
            return question.get('value')
        
        return True


    def do_algorithm(self):
        """Algoritmo de avalição de objetivas
            faz um filtro nas respostas certas
        """
        list_of_question      = self.quiz.list_of_question
        size_list_of_question = len(list_of_question)
        
        list_correct_answers = filter(self.filter_correct_answers, list_of_question)
        size_list_correct_answers = len(list_correct_answers)
        
        return size_list_of_question - size_list_correct_answers

