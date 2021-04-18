from typing import Tuple
from PIL import Image
import numpy

PRETO = [50, 50, 50]


class PintarForaDaImagem(IndexError):
    def __init__(self, msg):
        super().__init__(self, msg)


class ModeloReta:
    ponto_origem: Tuple[int, int]
    ponto_destino: Tuple[int, int]
    delta_x: int
    delta_y: int
    total_eixo_dominante: int
    dominante_atual: int
    secundario_atual: float
    m: float
    tipo: str

    def __init__(self, ponto1: Tuple[int, int], ponto2: Tuple[int, int]):
        self.definir_pontos_de_origem_e_destino(ponto1, ponto2)
        self.definir_deltas()

    def definir_pontos_de_origem_e_destino(self, ponto1: Tuple[int, int], ponto2: Tuple[int, int]):
        if ponto1[0] < ponto2[0]:
            self.ponto_origem = ponto1
            self.ponto_destino = ponto2
        else:
            self.ponto_origem = ponto2
            self.ponto_destino = ponto1

    def definir_deltas(self):
        self.delta_x = abs(self.ponto_origem[0] - self.ponto_destino[0])
        self.delta_y = abs(self.ponto_origem[1] - self.ponto_destino[1])

    def definir_m(self):
        pass

    def calcular_b(self):
        return self.secundario_atual - (self.m * self.dominante_atual)

    def recalcular_pontos(self, b: float):
        self.dominante_atual += 1
        self.secundario_atual = self.m * self.dominante_atual + b


class ModeloRetaDeltaX(ModeloReta):
    tipo = "X"

    def __init__(self, p1: Tuple[int, int], p2: Tuple[int, int]):
        super().__init__(p1, p2)
        self.definir_m()
        self.definir_eixos()

    def definir_m(self):
        self.m = self.delta_y / self.delta_x

    def definir_eixos(self):
        self.total_eixo_dominante = max(self.ponto_origem[0], self.ponto_destino[0])
        self.dominante_atual = self.ponto_origem[0]
        self.secundario_atual = self.ponto_origem[1]


class ModeloRetaDeltaY(ModeloReta):
    tipo = "Y"

    def __init__(self, p1: Tuple[int, int], p2: Tuple[int, int]):
        super().__init__(p1, p2)
        self.definir_m()
        self.definir_eixos()

    def definir_m(self):
        self.m = self.delta_x / self.delta_y

    def definir_eixos(self):
        self.total_eixo_dominante = max(self.ponto_origem[1], self.ponto_destino[1])
        self.dominante_atual = self.ponto_origem[1]
        self.secundario_atual = self.ponto_origem[0]


class Reta:
    ponto_origem: Tuple[int, int]
    ponto_destino: Tuple[int, int]
    delta_x: int
    delta_y: int

    def __init__(self, p1: Tuple[int, int], p2: Tuple[int, int]):
        self.definir_pontos_de_origem_e_destino(p1, p2)
        self.definir_deltas()

    def definir_pontos_de_origem_e_destino(self, ponto1: Tuple[int, int], ponto2: Tuple[int, int]):
        if ponto1[0] < ponto2[0]:
            self.ponto_origem = ponto1
            self.ponto_destino = ponto2
        else:
            self.ponto_origem = ponto2
            self.ponto_destino = ponto1

    def definir_deltas(self):
        self.delta_x = abs(self.ponto_origem[0] - self.ponto_destino[0])
        self.delta_y = abs(self.ponto_origem[1] - self.ponto_destino[1])

    def gerar_modelo(self):
        if self.delta_y > self.delta_x:
            if self.ponto_origem[1] > self.ponto_destino[1]:
                print("OOOOPSSSS")
            return ModeloRetaDeltaY(self.ponto_origem, self.ponto_destino)
            # TODO ver caso em q Y inicial é maior

        return ModeloRetaDeltaX(self.ponto_origem, self.ponto_destino)


class Rasterizador:
    imagem: numpy
    modelo: ModeloReta

    def __init__(self, imagem: numpy, modelo: ModeloReta):
        self.imagem = imagem
        self.modelo = modelo

    def rasterizar(self):
        {
            "X": self.rasterizacao_em_x,
            "Y": self.rasterizacao_em_y
        }[self.modelo.tipo]()

        return self.imagem

    def rasterizacao_em_x(self):
        b = self.modelo.calcular_b()
        self.pintar((self.modelo.dominante_atual, self.modelo.secundario_atual))

        while self.modelo.dominante_atual < self.modelo.total_eixo_dominante:
            self.modelo.recalcular_pontos(b)
            self.pintar((self.modelo.dominante_atual, self.modelo.secundario_atual))

    def rasterizacao_em_y(self):
        b = self.modelo.calcular_b()
        self.pintar((self.modelo.secundario_atual, self.modelo.dominante_atual))

        while self.modelo.dominante_atual < self.modelo.total_eixo_dominante:
            self.modelo.recalcular_pontos(b)
            self.pintar((self.modelo.secundario_atual, self.modelo.dominante_atual))

    def pintar(self, ponto):
        try:
            self.imagem[abs(int(ponto[0])), abs(int(ponto[1]))] = PRETO
        except IndexError:
            raise PintarForaDaImagem("O pixel encontra-se fora da imagem. Crie uma imagem maior")


class Imagem:
    array_imagem = None

    def __init__(self, largura: int, altura: int):
        la = abs(largura)
        al = abs(altura)

        # Gera array tridimencional (largura, altura, cor do pixel) com todos os pixeis brancos
        self.array_imagem = numpy.full((la, al, 3), 255, dtype=numpy.uint8)

    def rasterizar(self, modelo: ModeloReta):
        rasterizador = Rasterizador(self.array_imagem, modelo)
        self.array_imagem = rasterizador.rasterizar()

    def salvar(self, nome: str):
        img = Image.fromarray(self.array_imagem).transpose(Image.ROTATE_90)
        img.save(f"{nome}.png")
