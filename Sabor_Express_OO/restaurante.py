class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Ecxpress', 'Italiana')


restaurantes = [restaurante_pizza, restaurante_praca]


print(restaurante_praca)
print(restaurante_pizza)
