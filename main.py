from typing import List
from utils import Reta, Imagem, Ponto, Poligono, VERDE, VERMELHO, AZUL
from math import pi
from amostras import amostras_de_retas


def gerar_imagem_a_partir_de_lista_de_retas(lista_de_retas: List[Reta], resolucao: int):
    imagem = Imagem(resolucao, resolucao)
    imagem.rasterizar_varias_retas(lista_de_retas)
    imagem.salvar(nome=f"amostra_{resolucao}x{resolucao}")


if __name__ == "__main__":
    # Gera amostras de retas
    # for retas in amostras_de_retas:
    #     gerar_imagem_a_partir_de_lista_de_retas(*retas)

    hexagono_p1 = Poligono(lados=6, proporcao=0.1, translacao=(3, 10), rotacao=pi / 6)
    hexagono_p2 = Poligono(lados=6, proporcao=0.16, translacao=(30, 3))

    quadrado_p1 = Poligono(lados=4, proporcao=0.1, translacao=(5, 46), rotacao=pi / 4)
    quadrado_p2 = Poligono(lados=4, proporcao=0.16, translacao=(25, 38))

    triangulo_p1 = Poligono(lados=3, proporcao=0.1, translacao=(5, 80))
    triangulo_p2 = Poligono(lados=3, proporcao=0.16, translacao=(28, 75), rotacao=pi / 3)

    imagem = Imagem(60, 100)

    imagem.rasterizar_poligono(hexagono_p1, cor=VERDE)
    imagem.rasterizar_poligono(hexagono_p2, cor=AZUL)

    imagem.rasterizar_poligono(quadrado_p1, cor=VERDE)
    imagem.rasterizar_poligono(quadrado_p2, cor=AZUL)

    imagem.rasterizar_poligono(triangulo_p1, cor=VERDE)
    imagem.rasterizar_poligono(triangulo_p2, cor=AZUL)

    imagem.salvar(nome=f"poligonos_p")

    # -----------------------------

    hexagono_m1 = Poligono(lados=6, proporcao=0.3, translacao=(3, 10), rotacao=pi / 6)
    hexagono_m2 = Poligono(lados=6, proporcao=0.5, translacao=(100, 3))

    quadrado_m1 = Poligono(lados=4, proporcao=0.3, translacao=(10, 100), rotacao=pi / 4)
    quadrado_m2 = Poligono(lados=4, proporcao=0.5, translacao=(100, 100))

    triangulo_m1 = Poligono(lados=3, proporcao=0.3, translacao=(5, 200))
    triangulo_m2 = Poligono(lados=3, proporcao=0.5, translacao=(28, 200), rotacao=pi / 3)

    imagem = Imagem(300, 400)

    imagem.rasterizar_poligono(hexagono_m1, cor=VERDE)
    imagem.rasterizar_poligono(hexagono_m2, cor=AZUL)

    imagem.rasterizar_poligono(quadrado_m1, cor=VERMELHO)
    imagem.rasterizar_poligono(quadrado_m2, cor=AZUL)

    imagem.rasterizar_poligono(triangulo_m1, cor=VERDE)
    imagem.rasterizar_poligono(triangulo_m2, cor=AZUL)

    imagem.salvar(nome=f"poligonos_m")

    # -----------------------------

    hexagono_g1 = Poligono(lados=6, proporcao=1, translacao=(3, 10), rotacao=pi / 6)
    hexagono_g2 = Poligono(lados=6, proporcao=2, translacao=(100, 3))

    quadrado_g1 = Poligono(lados=4, proporcao=1, translacao=(10, 100), rotacao=pi / 4)
    quadrado_g2 = Poligono(lados=4, proporcao=2, translacao=(100, 100))

    triangulo_g1 = Poligono(lados=3, proporcao=1, translacao=(5, 200))
    triangulo_g2 = Poligono(lados=3, proporcao=2, translacao=(28, 200), rotacao=pi / 3)

    imagem = Imagem(600, 1000)

    imagem.rasterizar_poligono(hexagono_g1, cor=VERDE)
    imagem.rasterizar_poligono(hexagono_g2, cor=AZUL)

    imagem.rasterizar_poligono(quadrado_g1, cor=VERMELHO)
    imagem.rasterizar_poligono(quadrado_g2, cor=AZUL)

    imagem.rasterizar_poligono(triangulo_g1, cor=VERDE)
    imagem.rasterizar_poligono(triangulo_g2, cor=AZUL)

    imagem.rasterizar_poligono(quadrado_m1, cor=VERMELHO)
    imagem.rasterizar_poligono(quadrado_m2, cor=AZUL)

    imagem.rasterizar_poligono(triangulo_p1, cor=VERDE)
    imagem.rasterizar_poligono(hexagono_p1, cor=AZUL)

    imagem.salvar(nome=f"poligonos_g")

