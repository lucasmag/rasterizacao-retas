from utils import Reta, Imagem, Ponto

if __name__ == "__main__":
    lista_de_retas = [
        Reta(Ponto(0, 0), Ponto(900, 200)),
        Reta(Ponto(0, 0), Ponto(500, 500)),
        Reta(Ponto(100, 200), Ponto(500, 1000))
    ]

    imagem = Imagem(1000, 1000)
    imagem.rasterizar_varios(lista_de_retas)
    imagem.salvar(nome="teste")
