from utils import Reta, Imagem

if __name__ == "__main__":
    reta = Reta((1, 1), (8, 6))
    imagem = Imagem(10, 10)
    imagem.rasterizar(reta.gerar_modelo())
    imagem.salvar(nome="teste")
