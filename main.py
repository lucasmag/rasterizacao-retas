from typing import List, Tuple
from utils import Reta, Imagem, Poligono, Cores
from amostras import amostras_de_retas, amostras_de_poligonos


cores = [cor.value for cor in Cores]


def gerar_imagem_a_partir_de_lista_de_retas(lista_de_retas: List[Reta], resolucao: Tuple[int]):
    imagem = Imagem(*resolucao)
    imagem.rasterizar_varias_retas(lista_de_retas)
    imagem.salvar(nome=f"retas_{resolucao[0]}x{resolucao[1]}")


def gerar_imagem_a_partir_de_lista_de_poligonos(lista_de_poligonos: List[Poligono], resolucao: Tuple[int]):
    imagem = Imagem(*resolucao)

    for poligono, cor in zip(lista_de_poligonos, cores):
        imagem.rasterizar_poligono(poligono, cor=cor)

    imagem.salvar(nome=f"poligonos_{resolucao[0]}x{resolucao[1]}")


if __name__ == "__main__":
    for retas in amostras_de_retas:
        gerar_imagem_a_partir_de_lista_de_retas(*retas)

    for poligonos in amostras_de_poligonos:
        gerar_imagem_a_partir_de_lista_de_poligonos(*poligonos)
