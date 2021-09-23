from operator import attrgetter
from dataclasses import dataclass
from typing import List, Union, Tuple
from PIL import Image
import numpy
from math import floor
import math

from numpy import ndarray

BRANCO = [255, 255, 255]
PRETO = [50, 50, 50]
VERMELHO = [255, 50, 50]
VERDE = [50, 255, 50]
AZUL = [50, 50, 255]


class PintarForaDaImagem(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)


class PontosIguais(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)


class PontoInvalido(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)


class PoucosLados(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)


@dataclass
class Ponto:
    x: int
    y: int

    def __post_init__(self):
        if self.checar_se_ponto_tem_coordenada_menor_que_zero():
            raise PontoInvalido("O ponto não pode ter coordenada negativa")

    def checar_se_ponto_tem_coordenada_menor_que_zero(self):
        return any(ponto < 0 for ponto in [self.x, self.y])


class PontosEDeltas:
    ponto_origem: Ponto
    ponto_destino: Ponto
    delta_x: int
    delta_y: int


class ModeloReta:
    ponto_origem: Ponto
    ponto_destino: Ponto
    delta_x: int
    delta_y: int
    x: Union[int, float]  # x atual
    y: Union[int, float]  # y atual
    m: float
    tipo: str

    def __init__(self, dados: PontosEDeltas):
        self.ponto_origem = dados.ponto_origem
        self.ponto_destino = dados.ponto_destino
        self.x = dados.ponto_origem.x
        self.y = dados.ponto_origem.y
        self.delta_x = dados.delta_x
        self.delta_y = dados.delta_y

    def definir_m(self):
        pass

    def calcular_b(self):
        return 0.0

    def recalcular_pontos(self, b: float):
        pass


class ModeloRetaDeltaX(ModeloReta):
    tipo = "X"

    def __init__(self, dados: PontosEDeltas):
        super().__init__(dados)
        self.definir_m()

    def definir_m(self):
        self.m = self.delta_y / self.delta_x

    def calcular_b(self):
        return self.y - (self.m * self.x)

    def recalcular_pontos(self, b: float):
        self.x += 1
        self.y = int(self.m * self.x + b)


class ModeloRetaDeltaY(ModeloReta):
    tipo = "Y"

    def __init__(self, dados: PontosEDeltas):
        super().__init__(dados)
        self.definir_m()

    def definir_m(self):
        self.m = self.delta_x / self.delta_y

    def calcular_b(self):
        return self.x - (self.m * self.y)

    def recalcular_pontos(self, b: float):
        self.y += 1
        self.x = int(self.m * self.y + b)


class ModeloRetaYDecrescenteDeltaY(ModeloReta):
    tipo = "Yd"

    def __init__(self, dados: PontosEDeltas):
        super().__init__(dados)
        self.y -= 1
        self.definir_m()

    def definir_m(self):
        self.m = self.delta_x / self.delta_y

    def calcular_b(self):
        return -self.x - (self.m * self.y)

    def recalcular_pontos(self, b: float):
        self.y -= 1
        self.x = abs(int(self.m * self.y + b))


class ModeloRetaYDecrescenteDeltaX(ModeloReta):
    tipo = "Xd"

    def __init__(self, dados: PontosEDeltas):
        super().__init__(dados)
        self.y -= 1
        self.definir_m()

    def definir_m(self):
        self.m = self.delta_y / self.delta_x

    def calcular_b(self):
        return self.y - (self.m * -self.x)

    def recalcular_pontos(self, b: float):
        self.x += 1
        self.y = abs(floor(self.m * self.x - b))


class Reta:
    dados: PontosEDeltas

    def __init__(self, p1: Ponto, p2: Ponto):
        if p1 == p2:
            raise PontosIguais("Pontos não podem ser iguais")

        self.dados = PontosEDeltas()

        self.definir_pontos_de_origem_e_destino(p1, p2)
        self.definir_deltas()

    def definir_pontos_de_origem_e_destino(self, ponto1: Ponto, ponto2: Ponto):
        ponto_mais_a_esquerda, ponto_mais_a_direita = sorted([ponto1, ponto2], key=attrgetter('x'))
        self.dados.ponto_origem = ponto_mais_a_esquerda
        self.dados.ponto_destino = ponto_mais_a_direita

    def definir_deltas(self):
        self.dados.delta_x = abs(self.dados.ponto_origem.x - self.dados.ponto_destino.x)
        self.dados.delta_y = abs(self.dados.ponto_origem.y - self.dados.ponto_destino.y)

    def gerar_modelo(self):
        if self.dados.ponto_origem.y > self.dados.ponto_destino.y:
            if self.dados.delta_y > self.dados.delta_x:
                return ModeloRetaYDecrescenteDeltaY(self.dados)
            return ModeloRetaYDecrescenteDeltaX(self.dados)

        else:
            if self.dados.delta_y > self.dados.delta_x:
                return ModeloRetaDeltaY(self.dados)
            return ModeloRetaDeltaX(self.dados)


@dataclass()
class Rasterizador:
    imagem: numpy
    modelo: ModeloReta

    def rasterizar(self):
        dict(
            X=self.rasterizacao_com_delta_x,
            Y=self.rasterizacao_com_delta_y,
            Yd=self.rasterizacao_reta_decrescente_com_delta_y,
            Xd=self.rasterizacao_reta_descrescente_com_delta_x
        )[self.modelo.tipo]()
        return self.imagem

    def rasterizacao_com_delta_x(self):
        b = self.modelo.calcular_b()

        for x in range(self.modelo.x, self.modelo.ponto_destino.x):
            self.pintar(Ponto(x, self.modelo.y))
            self.modelo.recalcular_pontos(b)

    def rasterizacao_com_delta_y(self):
        b = self.modelo.calcular_b()

        for y in range(self.modelo.y, self.modelo.ponto_destino.y):
            self.pintar(Ponto(self.modelo.x, y))
            self.modelo.recalcular_pontos(b)

    def rasterizacao_reta_decrescente_com_delta_y(self):
        b = self.modelo.calcular_b()
        self.pintar(Ponto(self.modelo.x, self.modelo.y))

        for y in range(self.modelo.y, self.modelo.ponto_destino.y, -1):
            self.modelo.recalcular_pontos(b)
            self.pintar(Ponto(self.modelo.x, self.modelo.y))

    def rasterizacao_reta_descrescente_com_delta_x(self):
        b = self.modelo.calcular_b()

        for x in range(self.modelo.x, self.modelo.ponto_destino.x):
            self.pintar(Ponto(x, self.modelo.y))
            self.modelo.recalcular_pontos(b)

    def pintar(self, ponto: Ponto):
        try:
            self.imagem[ponto.x, ponto.y] = PRETO
        except IndexError:
            raise PintarForaDaImagem("O pixel encontra-se fora da imagem. Crie uma imagem maior")


class Poligono:
    lados: int
    proporcao: int
    rotacao: int
    translacao: Tuple[int, int]
    cor: Tuple[int, int, int]

    def __init__(self, lados=3, proporcao=1, rotacao=0, translacao=(0, 0), cor=PRETO):
        assert lados > 2 and isinstance(lados, int), "O polígono deve ter mais de 2 lados."
        assert proporcao > 0, "Proporção deve ser maior que zero."
        assert self.translacao_valida(translacao), "Translação deve ser uma tupla com 2 inteiros."

        self.lados = lados
        self.proporcao = proporcao
        self.rotacao = rotacao
        self.translacao = translacao
        self.cor = cor

    def translacao_valida(self, t):
        return isinstance(t, Tuple) and all([type(x) == int for x in t]) and len(t) == 2

    def gerar_retas(self) -> List[Reta]:
        lado = math.pi * 2 / self.lados

        pontos = [
            (floor(math.sin(lado * i + self.rotacao) * self.proporcao * 100),
             floor(math.cos(lado * i + self.rotacao) * self.proporcao * 100))
            for i in range(self.lados)]

        menor_x = abs(min([ponto[0] for ponto in pontos]))
        menor_y = abs(min([ponto[1] for ponto in pontos]))

        pontos_origem = [(x + menor_x, y + menor_y) for x, y in pontos]
        print(pontos_origem)
        if self.translacao:
            pontos_origem = [[sum(pair) for pair in zip(point, self.translacao)]
                             for point in pontos_origem]

        retas = []
        for i in range(0, len(pontos_origem)):
            retas.append(Reta(Ponto(*pontos_origem[i - 1]), Ponto(*pontos_origem[i])))

        return retas


class Imagem:
    array_imagem = None
    largura: int
    altura: int

    def __init__(self, largura: int, altura: int):
        self.largura = abs(largura)
        self.altura = abs(altura)
        # Gera array tridimencional (largura, altura, cor do pixel) com todos os pixeis brancos
        self.array_imagem = numpy.full((largura, altura, 3), 255, dtype=numpy.uint8)

    def rasterizar_reta(self, reta: Reta):
        rasterizador = Rasterizador(self.array_imagem, reta.gerar_modelo())
        self.array_imagem = rasterizador.rasterizar()

    def rasterizar_varias_retas(self, retas: List[Reta]):
        for reta in retas:
            rasterizador = Rasterizador(self.array_imagem, reta.gerar_modelo())
            self.array_imagem = rasterizador.rasterizar()

    def rasterizar_poligono(self, poligono: Poligono):
        self.rasterizar_varias_retas(poligono.gerar_retas())

    def pintar_poligono(self, cor):
        quadro = numpy.full((self.largura, self.altura, 3), 255, dtype=numpy.uint8)
        dentro = False

        for linha in range(0, self.largura):
            ultimo = numpy.full(3, 255, dtype=numpy.uint8)

            for coluna in range(0, self.altura):
                atual = self.array_imagem[linha][coluna]

                if all(atual == PRETO) and all(ultimo == BRANCO):
                    dentro = not dentro

                if all(atual == BRANCO) and dentro:
                    quadro[linha][coluna] = cor

                else:
                    quadro[linha][coluna] = atual

                ultimo = atual

            if dentro:
                dentro = False
                quadro[linha] = self.array_imagem[linha]

        self.array_imagem = quadro

    def salvar(self, nome: str):
        # O ponto de origem original da matriz é no canto superior esquerdo (linha 0, coluna 0)
        # A rotação é feita para que a imagem fique de acordo com o plano cartesiano (origem no canto inferior esquerdo)
        img = Image.fromarray(self.array_imagem)
        img.save(f"{nome}.png")
