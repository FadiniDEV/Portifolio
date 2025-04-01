from typing import Union

from FilaNormal import FilaNormal
from FilaPrioritaria import FilaPrioritaria
from Constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA

class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria, int]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe')
        