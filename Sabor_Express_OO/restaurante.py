class Restaurante:
    restaurantes = []
    #faz o objeto ter necessariamente os itens da classe com o (self.)
    def __init__(self ,nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'        
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
    

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')


restaurantes = [restaurante_pizza, restaurante_praca]

Restaurante.listar_restaurantes()

