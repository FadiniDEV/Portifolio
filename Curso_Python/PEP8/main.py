# from FilaNormal import FilaNormal
# from FilaPrioritaria import FilaPrioritaria
from FabricaFila import FabricaFila
from EstatisticaDetalhada import EstatisticaDetalhada
from EstatisticaResumida import EstatisticaResumida

# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(1))

# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# print(fila_teste_2.chama_cliente(10))
# print(fila_teste_2.chama_cliente(1))
# print(fila_teste_2.estatistica('10/1/1993', 198, 'detail'))

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(1))
print(teste_fabrica.chama_cliente(5))
print(teste_fabrica.estatistica(EstatisticaDetalhada('10/1/1993', 120)))
