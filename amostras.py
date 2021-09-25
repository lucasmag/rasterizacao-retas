from utils import Reta, Ponto

# retas = Tupla[Lista[Reta[Ponto, Ponto]], Resolucao: int]
retas_p = ([
    Reta(Ponto(1, 2), Ponto(5, 9)),
    Reta(Ponto(5, 5), Ponto(10, 10)),
    Reta(Ponto(3, 4), Ponto(9, 2)),
    Reta(Ponto(0, 1), Ponto(1, 9)),  # reta vertical
    Reta(Ponto(1, 0), Ponto(9, 0))  # reta horizontal
], 10)

retas_m = ([
    Reta(Ponto(10, 20), Ponto(50, 90)),
    Reta(Ponto(50, 50), Ponto(100, 100)),
    Reta(Ponto(30, 40), Ponto(90, 20)),
    Reta(Ponto(5, 10), Ponto(5, 90)),  # reta vertical
    Reta(Ponto(10, 5), Ponto(90, 5))  # reta horizontal
], 100)

retas_g = ([
    Reta(Ponto(100, 200), Ponto(500, 900)),
    Reta(Ponto(500, 500), Ponto(1000, 1000)),
    Reta(Ponto(300, 400), Ponto(900, 200)),
    Reta(Ponto(50, 100), Ponto(50, 900)),  # reta vertical
    Reta(Ponto(100, 50), Ponto(900, 50)),  # reta horizontal
], 1000)

amostras_de_retas = [retas_p, retas_m, retas_g]