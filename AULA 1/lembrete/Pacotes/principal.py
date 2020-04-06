from moduloCARRO import *
from moduloCARRO.custom import *

# import moduloCARRO

marca_veiculo('renult', 'A320')
modelo_veiculo()

cliente1 = Carro('chevrolet', 'Camaro', 'Amarelo', 50, 'cliente 1')
cliente2 = Carro('fiat', 'Fiat Toro', 'Vermelho', 100, 'cliente 2')

cliente1.marca_modelo()
cliente1.concessionaria()

cliente2.marca_modelo()
cliente2.concessionaria()