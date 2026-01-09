from utils.helper import formata_float_moeda

class Produto:
    contador: int = 1

    def __init__(self, nome: str, preco: float, estoque: int):
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        self.__estoque: int = estoque
        Produto.contador += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def preco(self) -> float:
        return self.__preco

    @property
    def estoque(self) -> int:
        return self.__estoque
    
    @estoque.setter
    def estoque(self, estoque: int) -> None:
        self.__estoque = estoque
    
    def __str__(self) -> str:
        return f"Código: {self.codigo} \nNome: {self.nome} \nPreço: {formata_float_moeda(self.preco)} \nEstoque: {self.estoque}\n"
    
