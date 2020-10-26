# -*- coding: UTF-8 -*-
import copy
from helper import Helper

class Quiz: 
    menu = ['0 - Para sair do formulario' ]
    disc_op = {
        'sair': 0
    }

    def __init__ (self, name, list_of_question):
        self.is_finished = False
        self.name = name
        self.list_of_question = copy.deepcopy(list_of_question)

    def print_out (self):
        # Cabeçalho do questionario
        print("Titulo: " + self.name)
        print("Finalizado: " + str(self.is_finished))
        Helper.new_line()
        # Cabeçalho do questionario

        for index, item in enumerate(self.list_of_question, start=1):
            description = item.get('description')
            is_answered = item.get('answer') != None

            answer = ''
            if is_answered:
                answer = item.get('answer').get('description')

            print("{} - {}".format(index, description))
            print("Responsta: " + answer)

    def start (self):
        while not self.is_finished:
            self.valid_is_finished()

            Helper.clear()
            self.print_out()
            Helper.new_line()
            self.render_menu()

            op = int(input("Qual questão deseja responder:"))

            if op == self.disc_op.get('sair'):
                self.is_finished = True
            elif self.valid_question_exist(op):
                id_question = op
                self.answer_question(id_question)

        else: 
            print('Formulario foi finalizado!!')

    def render_menu (self):
        for i in self.menu:
            print(i)

    def valid_is_finished(self):
        def filter_questoes_respondida(x):
            is_answered = x.get('answer') == None
            return is_answered
            
        l = filter(filter_questoes_respondida, self.list_of_question)
        if len(l) == 0:
            self.is_finished = True

    def answer_question (self, id_question):
        question = self.list_of_question[Quiz.valid_negative_op(id_question)-1]
        description = question.get('description')
        choices = question.get('choices')

        # Display pegutna
        Helper.clear()
        print('Para a pergunta:')
        print(description)
        Helper.division(len(description))
        # /Display pegutna

        for index, answer in enumerate(choices, start=1):
            description = answer.get('description')
            print("{} - {}".format(index, description))

        op = int(input("Qual sua resposta:"))
        position_answer_in_array = op

        if self.valid_answer_exist(question, position_answer_in_array):
            answer = choices[Quiz.valid_negative_op(position_answer_in_array)-1]
            question.update({'answer': answer})
            # question['answer'] = answer

    def valid_question_exist (self, n):
        is_valid = Quiz.valid_negative_op(n) <= len(self.list_of_question)
        if(not is_valid):
            print('Questão {} não é existe!'. format(n))
        return is_valid
    
    def valid_answer_exist (self, question, n):
        is_valid = Quiz.valid_negative_op(n) <= len(question.get('choices'))
        if(not is_valid):
            print('Resposta {} não foi encontrada'. format(n))
        return is_valid

    @staticmethod
    def valid_negative_op(n):
        if (n < 0):
            return n*-1

        return n
