from typing import List, Tuple
from utils import Reta, Imagem, Poligono, Parser
from amostras import amostras_de_retas, amostras_de_poligonos
import logging


logging.basicConfig(format="[%(asctime)s] %(levelname)s {%(filename)s:%(lineno)d} - %(message)s", level=logging.INFO)


def gerar_imagem_a_partir_de_lista_de_retas(lista_de_retas: List[Reta], resolucao: Tuple[int]):
    imagem = Imagem(*resolucao)
    imagem.rasterizar_varias_retas(lista_de_retas)
    imagem.salvar(nome=f"retas_{resolucao[0]}x{resolucao[1]}")


def gerar_imagem_a_partir_de_lista_de_poligonos(lista_de_poligonos: List[Poligono], resolucao: Tuple[int]):
    imagem = Imagem(*resolucao)
    imagem.rasterizar_varios_poligonos(lista_de_poligonos)
    imagem.salvar(nome=f"poligonos_{resolucao[0]}x{resolucao[1]}")


def main():
    args = Parser()

    try:
        for retas in amostras_de_retas:
            gerar_imagem_a_partir_de_lista_de_retas(*retas)

        for poligonos in amostras_de_poligonos:
            gerar_imagem_a_partir_de_lista_de_poligonos(*poligonos)

        if args.gerar_exemplos:
            from amostras import gerar_exemplos_relatorio
            gerar_exemplos_relatorio()

    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    main()
