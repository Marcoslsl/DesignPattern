from .select import Select

class Repository:

    def __init__(self):
        # a idea seria reunir os metodos de delete update por exemplo
        # em um unico lugar para facilitar
        self.select = Select()

    def select_one(self):
        return self.select.select_single_element()

    def select_many(self):
        return self.select.select_many_elements()