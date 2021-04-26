from utils import Reta, Imagem, Ponto


def gerar_amostras():
    lista_de_retas = [
        Reta(Ponto(10, 5), Ponto(20, 0))
    ]

    imagem = Imagem(20, 20)
    imagem.rasterizar_varios(lista_de_retas)
    imagem.salvar(nome="teste")


if __name__ == "__main__":
    gerar_amostras()
