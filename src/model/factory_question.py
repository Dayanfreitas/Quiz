class FactoryQuestion:

    def __init__(self):
        pass

    number_id_answer = 1
    number_id_question = 1

    @staticmethod
    def create_multiple_choice_question(description, choices=[]):
        question = {
            'id' : FactoryQuestion.number_id_question,
            'description': description,
            'choices': choices,
            'answer': None
        }

        FactoryQuestion.number_id_question += 1
        return question

    @staticmethod
    def create_multiple_choice_answer(description, weight):
        response = {
            'id': FactoryQuestion.number_id_answer,
            'description': description,
            'weight': weight,
        }

        FactoryQuestion.number_id_answer+= 1
        return response
    
    @staticmethod
    def create_objective_responses(description, value=False):
        response = {
            'id': FactoryQuestion.number_id_answer,
            'description': description,
            'value:': value,
        }

        return response
