import argparse
import sys
from typing import List, Tuple
from utils import Reta, Imagem, Poligono, Parser
from amostras import amostras_de_retas, amostras_de_poligonos
import logging


logging.basicConfig(format="[%(asctime)s] %(levelname)s {%(filename)s:%(lineno)d} - %(message)s", level=logging.WARNING)


def gerar_imagem_a_partir_de_lista_de_retas(lista_de_retas: List[Reta], resolucao: Tuple[int]):
    imagem = Imagem(*resolucao)
    imagem.rasterizar_varias_retas(lista_de_retas)
    imagem.salvar(nome=f"retas_{resolucao[0]}x{resolucao[1]}")


def gerar_imagem_a_partir_de_lista_de_poligonos(lista_de_poligonos: List[Poligono], resolucao: Tuple[int]):
    imagem = Imagem(*resolucao)
    imagem.rasterizar_varios_poligonos(lista_de_poligonos)
    imagem.salvar(nome=f"poligonos_{resolucao[0]}x{resolucao[1]}")


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action='store_true')
    parser.add_argument("--gerar_exemplos", "-g", action='store_true')

    return parser.parse_args()


def main():
    args = parse()

    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)

    try:
        sys.stdout.write("Executando...\n")

        for retas in amostras_de_retas:
            gerar_imagem_a_partir_de_lista_de_retas(*retas)

        for poligonos in amostras_de_poligonos:
            gerar_imagem_a_partir_de_lista_de_poligonos(*poligonos)

        if args.gerar_exemplos:
            from amostras import gerar_exemplos_relatorio
            gerar_exemplos_relatorio()

        sys.stdout.write("Concluído!\n")

    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    main()
