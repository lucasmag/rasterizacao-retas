from operator import attrgetter
from dataclasses import dataclass
from typing import List, Union
from PIL import Image
import numpy
from math import ceil, floor

PRETO = [50, 50, 50]


class PintarForaDaImagem(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)


class PontosIguais(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)


class PontoInvalido(Exception):
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


class ModeloReta:
    ponto_origem: Ponto
    ponto_destino: Ponto
    delta_x: int
    delta_y: int
    x: Union[int, float]  # x atual
    y: Union[int, float]  # y atual
    m: float
    tipo: str

    def __init__(self, ponto1: Ponto, ponto2: Ponto):
        self.definir_pontos_de_origem_e_destino(ponto1, ponto2)
        self.definir_deltas()

    def definir_pontos_de_origem_e_destino(self, ponto1: Ponto, ponto2: Ponto):
        self.ponto_origem, self.ponto_destino = sorted([ponto1, ponto2], key=attrgetter('x'))
        self.x = self.ponto_origem.x
        self.y = self.ponto_origem.y

    def definir_deltas(self):
        self.delta_x = abs(self.ponto_origem.x - self.ponto_destino.x)
        self.delta_y = abs(self.ponto_origem.y - self.ponto_destino.y)

    def definir_m(self):
        pass

    def calcular_b(self):
        return 0.0

    def recalcular_pontos(self, b: float):
        pass


class ModeloRetaDeltaX(ModeloReta):
    tipo = "X"

    def __init__(self, p1: Ponto, p2: Ponto):
        super().__init__(p1, p2)
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

    def __init__(self, p1: Ponto, p2: Ponto):
        super().__init__(p1, p2)
        self.definir_m()

    def definir_m(self):
        self.m = self.delta_x / self.delta_y

    def calcular_b(self):
        return self.x - (self.m * self.y)

    def recalcular_pontos(self, b: float):
        self.y += 1
        self.x = int(self.m * self.y + b)


class ModeloRetaDeltaYDescrescente(ModeloReta):
    tipo = "Yd"

    def __init__(self, p1: Ponto, p2: Ponto):
        super().__init__(p1, p2)
        self.y -= 1
        self.definir_m()

    def definir_m(self):
        self.m = self.delta_x / self.delta_y

    def calcular_b(self):
        return self.x - (self.m * self.y)

    def recalcular_pontos(self, b: float):
        self.y -= 1
        self.x = abs(int(self.m * self.y + b))


class ModeloRetaDeltaXDescrescente(ModeloReta):
    tipo = "Xd"

    def __init__(self, p1: Ponto, p2: Ponto):
        super().__init__(p1, p2)
        self.y -= 1
        self.definir_m()

    def definir_m(self):
        self.m = self.delta_y / self.delta_x

    def calcular_b(self):
        return self.y - (self.m * -self.x)

    def recalcular_pontos(self, b: float):
        self.x += 1
        self.y = abs(floor(self.m * self.x - b))
        print(self.x, (self.m * self.x - b))


class Reta:
    ponto_origem: Ponto
    ponto_destino: Ponto
    delta_x: int
    delta_y: int

    def __init__(self, p1: Ponto, p2: Ponto):
        if p1 == p2:
            raise PontosIguais("Pontos não podem ser iguais")

        self.definir_pontos_de_origem_e_destino(p1, p2)
        self.definir_deltas()

    def definir_pontos_de_origem_e_destino(self, ponto1: Ponto, ponto2: Ponto):
        ponto_mais_a_esquerda, ponto_mais_a_direita = sorted([ponto1, ponto2], key=attrgetter('x'))
        self.ponto_origem = ponto_mais_a_esquerda
        self.ponto_destino = ponto_mais_a_direita

    def definir_deltas(self):
        self.delta_x = abs(self.ponto_origem.x - self.ponto_destino.x)
        self.delta_y = abs(self.ponto_origem.y - self.ponto_destino.y)

    def gerar_modelo(self):
        if self.ponto_origem.y > self.ponto_destino.y:
            if self.delta_y > self.delta_x:
                print("YD ------------------------")
                return ModeloRetaDeltaYDescrescente(self.ponto_origem, self.ponto_destino)
            return ModeloRetaDeltaXDescrescente(self.ponto_origem, self.ponto_destino)

        else:
            if self.delta_y > self.delta_x:
                return ModeloRetaDeltaY(self.ponto_origem, self.ponto_destino)
            return ModeloRetaDeltaX(self.ponto_origem, self.ponto_destino)


@dataclass()
class Rasterizador:
    imagem: numpy
    modelo: ModeloReta

    def rasterizar(self):
        dict(
            X=self.rasterizacao_em_x_crescente,
            Y=self.rasterizacao_em_y_crescente,
            Yd=self.rasterizacao_em_y_decrescente,
            Xd=self.rasterizacao_em_x_decrescente
        )[self.modelo.tipo]()
        return self.imagem

    def rasterizacao_em_x_crescente(self):
        b = self.modelo.calcular_b()

        for x in range(self.modelo.x, self.modelo.ponto_destino.x):
            self.pintar(Ponto(x, self.modelo.y))
            self.modelo.recalcular_pontos(b)

    def rasterizacao_em_y_crescente(self):
        b = self.modelo.calcular_b()

        for y in range(self.modelo.y, self.modelo.ponto_destino.y):
            self.pintar(Ponto(self.modelo.x, y))
            self.modelo.recalcular_pontos(b)

    def rasterizacao_em_y_decrescente(self):
        b = self.modelo.calcular_b()

        while self.modelo.y >= self.modelo.ponto_destino.y:
            self.pintar(Ponto(self.modelo.x, self.modelo.y))
            self.modelo.recalcular_pontos(b)

    def rasterizacao_em_x_decrescente(self):
        b = self.modelo.calcular_b()

        for x in range(self.modelo.x, self.modelo.ponto_destino.x):
            self.pintar(Ponto(x, self.modelo.y))
            self.modelo.recalcular_pontos(b)

    def pintar(self, ponto: Ponto):
        try:
            self.imagem[ponto.x, ponto.y] = PRETO
        except IndexError:
            raise PintarForaDaImagem("O pixel encontra-se fora da imagem. Crie uma imagem maior")


class Imagem:
    array_imagem = None

    def __init__(self, largura: int, altura: int):
        larg = abs(largura)
        alt = abs(altura)
        # Gera array tridimencional (largura, altura, cor do pixel) com todos os pixeis brancos
        self.array_imagem = numpy.full((larg, alt, 3), 255, dtype=numpy.uint8)

    def rasterizar(self, reta: Reta):
        rasterizador = Rasterizador(self.array_imagem, reta.gerar_modelo())
        self.array_imagem = rasterizador.rasterizar()

    def rasterizar_varios(self, retas: List[Reta]):
        for reta in retas:
            rasterizador = Rasterizador(self.array_imagem, reta.gerar_modelo())
            self.array_imagem = rasterizador.rasterizar()

    def salvar(self, nome: str):
        # O ponto de origem original da matriz é no canto superior esquerdo (linha 0, coluna 0)
        # A rotação é feita para que a imagem fique de acordo com o plano cartesiano (origem no canto inferior esquerdo)
        img = Image.fromarray(self.array_imagem).transpose(Image.ROTATE_90)
        img.save(f"{nome}.png")
