from utils import Reta, Imagem

if __name__ == "__main__":
    lista_de_retas = []
    lista_de_retas.append(Reta((0, 0), (900, 200)).gerar_modelo())
    lista_de_retas.append(Reta((0, 0), (500, 500)).gerar_modelo())
    lista_de_retas.append(Reta((100, 200), (500, 1000)).gerar_modelo())

    imagem = Imagem(1000, 1000)
    imagem.rasterizar_varios(lista_de_retas)
    imagem.salvar(nome="teste")
