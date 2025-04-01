from typing import Union

from FilaBase import FilaBase
from Constantes import CODIGO_PRIORITARIO
from EstatisticaResumida import EstatisticaResumida
from EstatisticaDetalhada import EstatisticaDetalhada

Classes = Union[EstatisticaDetalhada, EstatisticaResumida]


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')
    
    def estatistica(self, retorna_estatistica: Classes)-> dict:

        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
