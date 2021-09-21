from typing import List

from utils import Reta, Imagem, Ponto, criar_poligono


def gerar_imagem_quadrada_a_partir_de_lista_de_retas(lista_de_retas: List[Reta], resolucao: int):
    imagem = Imagem(resolucao, resolucao)
    imagem.rasterizar_varios(lista_de_retas)
    imagem.salvar(nome=f"amostra_{resolucao}x{resolucao}")


def gerar_amostras():
    lista_de_retas = [
        Reta(Ponto(1, 2), Ponto(5, 9)),
        Reta(Ponto(5, 5), Ponto(10, 10)),
        Reta(Ponto(3, 4), Ponto(9, 2)),
        Reta(Ponto(0, 1), Ponto(1, 9)),  # reta vertical
        Reta(Ponto(1, 0), Ponto(9, 0))   # reta horizontal
    ]

    gerar_imagem_quadrada_a_partir_de_lista_de_retas(lista_de_retas, 10)

    lista_de_retas = [
        Reta(Ponto(10, 20), Ponto(50, 90)),
        Reta(Ponto(50, 50), Ponto(100, 100)),
        Reta(Ponto(30, 40), Ponto(90, 20)),
        Reta(Ponto(5, 10), Ponto(5, 90)),  # reta vertical
        Reta(Ponto(10, 5), Ponto(90, 5))   # reta horizontal
    ]

    gerar_imagem_quadrada_a_partir_de_lista_de_retas(lista_de_retas, 100)

    lista_de_retas = [
        Reta(Ponto(100, 200), Ponto(500, 900)),
        Reta(Ponto(500, 500), Ponto(1000, 1000)),
        Reta(Ponto(300, 400), Ponto(900, 200)),
        Reta(Ponto(50, 100), Ponto(50, 900)),  # reta vertical
        Reta(Ponto(100, 50), Ponto(900, 50)),   # reta horizontal
    ]

    gerar_imagem_quadrada_a_partir_de_lista_de_retas(lista_de_retas, 1000)


if __name__ == "__main__":
    #gerar_amostras()
    poligono = criar_poligono(6, rotation=20, translation=(500, 500))
    imagem = Imagem(1000, 1000)
    imagem.rasterizar_varias_retas(poligono)
    imagem.salvar(nome=f"soumteste")
