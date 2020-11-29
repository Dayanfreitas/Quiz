# -*- coding: UTF-8 -*
import copy
from helper import Helper
from helper import Translation as QuizLabel
from colored import *

class Quiz: 
    menu = [ 
        ' 0 - {}'.format(QuizLabel.get_label('sair'))
        ]
                    
    disc_op = {
        'sair': 0
    }
    
    def __init__ (self, name, list_of_question):
        self._list_of_question   = copy.deepcopy(list_of_question)
        self._name               = name
        self._is_status_finished = False
        self._is_finished        = False
        self._result             = None

    def start(self):
        """
            Função principal para dar inicio ao formulário pelo prompt
        """
        while not self.is_finished:
            self.valid_is_finished()
            self.print_all_questions()
            self.play_menu()
        else:
            print(QuizLabel.get_label('formulario_finalizado') + ' !!')


    def valid_is_finished(self):
        """
            Verificar se todas as perguntas do formulário foram respodondidas
        """
        def filter_questoes_respondida(x):
            is_answered = x.get('answer') is not None
            return is_answered

        list_questions_answered = filter(filter_questoes_respondida, self.list_of_question)
        if len(list_questions_answered) == len(self.list_of_question):
            self.is_status_finished = True
        
        return self.is_status_finished

    def print_header(self): 
        """
            Função que implemanta o cabeçalho do formulário

            Titulo:::::<nome>
            Status:::::self.is_status_finished
        """
        text_finished = colored('red', QuizLabel.get_label('nao_finalizado')) 
        print('self.is_status_finished', self.is_status_finished)
        if self.is_status_finished:
            text_finished = colored('green', QuizLabel.get_label('finalizado'))
        
        # Cabeçalho do questionario
        Helper.clear()
        print("{}::::::::{}".format(QuizLabel.get_label('titulo'), self.name))
        print("{}:::::::{}".format(QuizLabel.get_label('status'), text_finished))
        Helper.new_line()
        # Cabeçalho do questionario
    
    def print_format_question(self, index, description, answer=None):
        print("{}) {}".format(index, description))
        if answer:
            print("{}: {}".format(QuizLabel.get_label('resposta'),answer))
        Helper.new_line()

    def print_all_questions(self):
        self.print_header()
        for index, item in enumerate(self.list_of_question, start=1):
            answer      = item.get('answer')
            is_answered = answer is not None
            description = item.get('description')
            
            if is_answered:
                answer = answer.get('description')
            else:
                answer = ''
            self.print_format_question(index, description, answer)
    
    def play_menu(self):
        self.print_menu_op()
        self.process_op(
            Quiz.valid_negative_op(
                int(input(
                    colored('white', 
                            QuizLabel.get_label('pergunta_op'),
                            'background_black',
                            True
                            ) 
                    )
                )
            )
        )
    
    def print_menu_op (self):
        for i in self.menu:
            print(i)

    def process_op(self, op):
        if op == self.disc_op.get('sair'):
            self.is_finished = True
        elif self.valid_question_exist(op):
            index_question = op
            self.answer_question(index_question)

    def print_header_question(self, question):
        Helper.clear()
        print(QuizLabel.get_label('para_pergunta') + ':')
        print(question.get('description'))
        Helper.division(len(question.get('description')))

    def print_possible_answers(self, quetion):
        for index, answer in enumerate(quetion.get('choices'), start=1):
            self.print_format_question(index, answer.get('description'))        

    def answer_question (self, id_question):
        question = self.get_question(id_question)
        self.print_header_question(question)
        self.print_possible_answers(question)
       
        index_answer = int(
            input(colored(
                'white', 
                QuizLabel.get_label('pergunta_op'),
                'background_black',
                True
                ) 
            )
        )

        self.set_answer(id_question, index_answer)        

    def get_question(self, index):
        return self.list_of_question[index - 1] 

    def get_answer(self, index, question):
        choices = question.get('choices')
        return choices[Quiz.valid_negative_op(index) - 1]

    def set_answer(self, id_question, index_answer):
        question = self.get_question(id_question)
        if self.valid_answer_exist(question, index_answer):
            answer = self.get_answer(index_answer, question)
            question.update({'answer': answer})

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

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(name):
        self._name = name
        
    @property
    def list_of_question(self):
        return self._list_of_question
    
    @list_of_question.setter
    def list_of_question(list_of_question):
        self._list_of_question = list_of_question
        
    @property
    def is_finished(self):
        return self._is_finished

    @property
    def is_status_finished (self):
        return self._is_status_finished
    
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, result):
        self._result = result