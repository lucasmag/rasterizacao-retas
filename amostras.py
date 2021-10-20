from utils import Reta, Ponto, Poligono, Imagem
from math import pi
from utils import Cores


retas_p = ([
    Reta(Ponto(1, 2), Ponto(5, 9)),
    Reta(Ponto(5, 5), Ponto(10, 10)),
    Reta(Ponto(3, 4), Ponto(9, 2)),
    Reta(Ponto(0, 1), Ponto(1, 9)),  # reta vertical
    Reta(Ponto(1, 0), Ponto(9, 0))  # reta horizontal
], (10, 10))

retas_m = ([
    Reta(Ponto(10, 20), Ponto(50, 90)),
    Reta(Ponto(50, 50), Ponto(100, 100)),
    Reta(Ponto(30, 40), Ponto(90, 20)),
    Reta(Ponto(5, 10), Ponto(5, 90)),  # reta vertical
    Reta(Ponto(10, 5), Ponto(90, 5))  # reta horizontal
], (100, 100))

retas_g = ([
    Reta(Ponto(100, 200), Ponto(500, 900)),
    Reta(Ponto(500, 500), Ponto(1000, 1000)),
    Reta(Ponto(300, 400), Ponto(900, 200)),
    Reta(Ponto(50, 100), Ponto(50, 900)),  # reta vertical
    Reta(Ponto(100, 50), Ponto(900, 50)),  # reta horizontal
], (1000, 1000))

poligonos_p = ([
    Poligono(lados=6, escala=0.1, translacao=(5, 5), rotacao=pi / 6, cor=Cores.VERDE.value),
    Poligono(lados=6, escala=0.16, translacao=(35, 5), cor=Cores.VERMELHO.value),
    Poligono(lados=4, escala=0.1, translacao=(5, 46), rotacao=pi / 4, cor=Cores.AZUL.value),
    Poligono(lados=4, escala=0.16, translacao=(35, 40), cor=Cores.AMARELO.value),
    Poligono(lados=3, escala=0.1, translacao=(5, 80), cor=Cores.ROXO.value),
    Poligono(lados=3, escala=0.16, translacao=(35, 75), rotacao=pi / 3, cor=Cores.CIANO.value)
], (80, 110))

poligonos_m = ([
   Poligono(lados=6, escala=0.4, translacao=(30, 10), rotacao=pi / 6, cor=Cores.VERDE.value),
   Poligono(lados=6, escala=0.6, translacao=(150, 10), cor=Cores.VERMELHO.value),
   Poligono(lados=4, escala=0.4, translacao=(30, 140), rotacao=pi / 4, cor=Cores.AZUL.value),
   Poligono(lados=4, escala=0.6, translacao=(150, 140), cor=Cores.AMARELO.value),
   Poligono(lados=3, escala=0.4, translacao=(30, 280), cor=Cores.ROXO.value),
   Poligono(lados=3, escala=0.6, translacao=(150, 280), rotacao=pi / 3, cor=Cores.CIANO.value)
], (300, 400))

poligonos_g = ([
   Poligono(lados=6, escala=1, translacao=(50, 50), rotacao=pi / 6, cor=Cores.VERDE.value),
   Poligono(lados=6, escala=1.5, translacao=(300, 50), cor=Cores.VERMELHO.value),
   Poligono(lados=4, escala=1, translacao=(50, 380), rotacao=pi / 4, cor=Cores.AZUL.value),
   Poligono(lados=4, escala=1.5, translacao=(300, 380), cor=Cores.AMARELO.value),
   Poligono(lados=3, escala=1, translacao=(50, 700), cor=Cores.ROXO.value),
   Poligono(lados=3, escala=1.5, translacao=(300, 700), rotacao=pi / 3, cor=Cores.CIANO.value)
], (700, 1000))

amostras_de_retas = [retas_p, retas_m, retas_g]
amostras_de_poligonos = [poligonos_p, poligonos_m, poligonos_g]


def exemplos_relatorio():
    """Gera as imagens utilizadas no relatório"""

    def varias_retas():
        ponto1 = Ponto(0, 0)
        ponto2 = Ponto(9, 3)

        reta = Reta(ponto1, ponto2)

        imagem = Imagem(10, 10)
        imagem.rasterizar_reta(reta)
        imagem.salvar("reta")

        reta1 = Reta(Ponto(2, 2), Ponto(28, 28))
        reta2 = Reta(Ponto(2, 28), Ponto(28, 2))
        lista_de_retas = [reta1, reta2]

        imagem = Imagem(30, 30)
        imagem.rasterizar_varias_retas(lista_de_retas)
        imagem.salvar("varias_retas")

    def triangulo_azul():
        poligono = Poligono(lados=3, escala=0.1, translacao=(2, 2), cor=[0, 0, 255])
        imagem = Imagem(20, 20)
        imagem.rasterizar_poligono(poligono)
        imagem.salvar("triangulo_azul")

    def poligonos_resolucoes():

        hexagono = Poligono(lados=6, escala=0.1, translacao=(0, 0), rotacao=pi / 6, cor=Cores.VERDE.value)
        heptagono = Poligono(lados=7, escala=0.1, translacao=(20, 0), cor=Cores.VERDE.value)
        octogono = Poligono(lados=8, escala=0.1, translacao=(40, 0), rotacao=pi / 8, cor=Cores.VERDE.value)

        imagem = Imagem(60, 20)

        imagem.rasterizar_poligono(hexagono)
        imagem.rasterizar_poligono(heptagono)
        imagem.rasterizar_poligono(octogono)

        imagem.salvar("poligonos_baixa_res")

        hexagono = Poligono(lados=6, escala=1, translacao=(0, 0), rotacao=pi / 6, cor=Cores.VERDE.value)
        heptagono = Poligono(lados=7, escala=1, translacao=(200, 0), cor=Cores.VERDE.value)
        octogono = Poligono(lados=8, escala=1, translacao=(400, 0), rotacao=pi / 8, cor=Cores.VERDE.value)

        imagem = Imagem(600, 200)

        imagem.rasterizar_poligono(hexagono)
        imagem.rasterizar_poligono(heptagono)
        imagem.rasterizar_poligono(octogono)

        imagem.salvar("poligonos_alta_res")

    def varios_poligonos():
        triangulo = Poligono(lados=3, escala=1, translacao=(0, 0), cor=Cores.VERDE.value)
        quadrado = Poligono(lados=4, escala=1, translacao=(100, 0), rotacao=pi / 4, cor=Cores.AZUL.value)
        pentagono = Poligono(lados=5, escala=1, translacao=(200, 0), cor=Cores.VERMELHO.value)

        lista_de_poligonos = [triangulo, quadrado, pentagono]

        imagem = Imagem(400, 200)
        imagem.rasterizar_varios_poligonos(lista_de_poligonos)
        imagem.salvar("varios_poligonos")

    varias_retas()
    triangulo_azul()
    varios_poligonos()
    poligonos_resolucoes()
