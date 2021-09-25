from utils import Reta, Ponto, Poligono, Imagem
from math import pi

# retas = Tupla[Lista[Reta[Ponto, Ponto]], Resolucao: int]
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
    Poligono(lados=6, proporcao=0.1, translacao=(5, 5), rotacao=pi / 6),
    Poligono(lados=6, proporcao=0.16, translacao=(35, 5)),
    Poligono(lados=4, proporcao=0.1, translacao=(5, 46), rotacao=pi / 4),
    Poligono(lados=4, proporcao=0.16, translacao=(35, 40)),
    Poligono(lados=3, proporcao=0.1, translacao=(5, 80)),
    Poligono(lados=3, proporcao=0.16, translacao=(35, 75), rotacao=pi / 3)
], (80, 110))


poligonos_m = ([
   Poligono(lados=6, proporcao=0.4, translacao=(30, 10), rotacao=pi / 6),
   Poligono(lados=6, proporcao=0.6, translacao=(150, 10)),
   Poligono(lados=4, proporcao=0.4, translacao=(30, 140), rotacao=pi / 4),
   Poligono(lados=4, proporcao=0.6, translacao=(150, 140)),
   Poligono(lados=3, proporcao=0.4, translacao=(30, 280)),
   Poligono(lados=3, proporcao=0.6, translacao=(150, 280), rotacao=pi / 3)
], (300, 400))


poligonos_g = ([
   Poligono(lados=6, proporcao=1, translacao=(50, 50), rotacao=pi / 6),
   Poligono(lados=6, proporcao=1.5, translacao=(300, 50)),
   Poligono(lados=4, proporcao=1, translacao=(50, 380), rotacao=pi / 4),
   Poligono(lados=4, proporcao=1.5, translacao=(300, 380)),
   Poligono(lados=3, proporcao=1, translacao=(50, 700)),
   Poligono(lados=3, proporcao=1.5, translacao=(300, 700), rotacao=pi / 3)
], (700, 1000))

amostras_de_retas = [retas_p, retas_m, retas_g]
amostras_de_poligonos = [poligonos_p, poligonos_m, poligonos_g]