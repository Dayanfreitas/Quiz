# # -*- coding: UTF-8 -*-

# from Tkinter import *
from model.quiz import Quiz
from model.factory_question import FactoryQuestion
from helper import *


# class Application:
#     def __init__(self, master=None):
#         self.quiz = Quiz('Questionario de pessoas boas!', [])
        

#         master.title(self.quiz.name)
#         master.geometry('300x300')

#         self.widget1 = Frame(master)
#         self.widget1.pack()



#         self.sair = Button(self.widget1)
#         self.sair["text"] = "Finalizar"
#         self.sair["width"] = 20
#         # self.sair["command"] =
#         self.sair.pack()

# root = Tk()
# Application(root)
# root.mainloop()

if __name__ == "__main__":
    Main_Quiz_1 = Quiz('Formulário sabichão!', [
        FactoryQuestion.create_multiple_choice_question('2 + 2 = ', [
            FactoryQuestion.create_objective_responses('2', False),
            FactoryQuestion.create_objective_responses('3', False),
            FactoryQuestion.create_objective_responses('4', True),
            FactoryQuestion.create_objective_responses('5',False)
        ]),
        FactoryQuestion.create_multiple_choice_question('Quem conquistou o Brasil', [
            FactoryQuestion.create_objective_responses('Mc pedrinho', False),
            FactoryQuestion.create_objective_responses('Nego ney', False),
            FactoryQuestion.create_objective_responses('Pedro Alvares Cabra', True),
            FactoryQuestion.create_objective_responses('Xup', False)
        ])
    ])
    
    Main_Quiz_2 = Quiz('Questionario de pessoas boas "!', [
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
    ]) 

    Main_Quiz_1.start()
    Main_Quiz_2.start()
    value_form_1 = Context(ConcreteStrategyEvaluatorObjectives(Main_Quiz_1)).start()
    value_form_2 = Context(ConcreteStrategyEvaluatorObjectives(Main_Quiz_2)).start()

    print("Valor do Formulário :" + str(Context(ConcreteStrategyEvaluatorObjectives(Main_Quiz_1)).start()))
    print("Valor do Formulário: " + str(Context(ConcreteStrategyEvaluatorMultiple(Main_Quiz_2)).start()))