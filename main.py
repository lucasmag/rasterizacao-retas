from typing import List, Tuple
from utils import Reta, Imagem, Poligono
from amostras import amostras_de_retas, amostras_de_poligonos


def gerar_imagem_a_partir_de_lista_de_retas(lista_de_retas: List[Reta], resolucao: Tuple[int]):
    imagem = Imagem(*resolucao)
    imagem.rasterizar_varias_retas(lista_de_retas)
    imagem.salvar(nome=f"retas_{resolucao[0]}x{resolucao[1]}")


def gerar_imagem_a_partir_de_lista_de_poligonos(lista_de_poligonos: List[Poligono], resolucao: Tuple[int]):
    imagem = Imagem(*resolucao)
    imagem.rasterizar_varios_poligonos(lista_de_poligonos)
    imagem.salvar(nome=f"poligonos_{resolucao[0]}x{resolucao[1]}")


if __name__ == "__main__":
    for retas in amostras_de_retas:
        gerar_imagem_a_partir_de_lista_de_retas(*retas)

    for poligonos in amostras_de_poligonos:
        gerar_imagem_a_partir_de_lista_de_poligonos(*poligonos)
