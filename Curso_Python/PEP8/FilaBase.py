import abc

from typing import List

from Constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else: 
            self.codigo += 1

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)
    
    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def atualiza_fila(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...
