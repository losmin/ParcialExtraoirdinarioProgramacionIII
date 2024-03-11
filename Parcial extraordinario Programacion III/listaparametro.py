class lista_parametro:
    def __init__(self, Lista):
        self.Lista = Lista

    def sum_of_elements(self):
        return sum(self.Lista)

numbers = [1, 2, 3, 4, 5]
params = lista_parametro(numbers)

sum_of_numbers = params.sum_of_elements()
print(sum_of_numbers)