class Carro:
    def __init__(self, marca, modelo, cor, litros, cliente):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.litros = litros
        self.cliente = cliente

    def marca_modelo(self):
        print('CLIENTE:', self.cliente, 'marca:', self.marca, 'modelo:', self.modelo) # convencional
        # print(f'marca: {self.marca}, modelo: {self.modelo}') # fstring
        # print('marca: {}, modelo: {}'.format(self.marca, self.modelo)) # .format
        # print('marca: ' + self.marca + ' modelo: ' + self.modelo) # concatenação de strings

    def concessionaria(self):
        if self.marca == 'chevrolet':
            print('CLIENTE', self.cliente, 'É uma marca boa, aconselho comprar')
        elif self.litros > 50:
            print('CLIENTE', self.cliente, 'Não é uma marca boa mas tem um bom tanque')
        else:
            print('CLIENTE', self.cliente, 'Não é uma marca confiavel!')
