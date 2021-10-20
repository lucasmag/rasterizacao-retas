## Computação gráfica
### Rasterização de retas e polígonos

A presente aplicação se trata de um algoritmo de rasterização de retas e polígonos regulares.

Para rodar o projeto certifique-se que o python está instalado na máquina (python>=3.6).
```bash
$ python --version
Python 3.8.10
```

Instale o gerenciador de ambientes virtuais [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):
```bash
$ sudo apt install python3-virtualenv
```

Crie um ambiente virtual:
```bash
$ virtualenv venv
```

Ative o ambiente virtual:
```bash
$ source venv/bin/activate
```

Instale as dependêcias:
```bash
$ pip install -r requirements.txt
```

Rode a aplicação:
```bash
$ python main.py
```

---

Por padrão a aplicação irá gerar somente as imagens de comparação solicitadas na atividade.

Para gerar todas as imagens presentes no relatório, execute a aplicação com o argumento *gerar_exemplos*:
```bash
$ python main.py gerar_exemplos
```

Todas as saídas devem estar presentes no diretório `/imagens`