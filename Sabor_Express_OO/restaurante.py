class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

restaurante_shushi = Restaurante()

restaurantes = [restaurante_shushi, restaurante_praca]
print(restaurante_praca.categoria)