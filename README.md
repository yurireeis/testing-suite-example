[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6c36e2734e81411a9ff93b59da255b83)](https://www.codacy.com/gh/yurireeis/testing-suite-example/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=yurireeis/testing-suite-example&amp;utm_campaign=Badge_Grade)

# Shipay Testing Suite

## Configurando o seu ambiente

1) Sem docker:
```
virtualenv -p python3 .env
source .env/bin/activate
pip install -r requirements.txt
```
2) Com docker:

```
em breve
```

## Testes

Os testes setados neste projeto estão embasados na pirâmide prática de testes, seguindo os conceitos a seguir:

![Pratical Test Pyramid](https://arquivo.devmedia.com.br/REVISTAS/es/imagens/72/8/1.png)

Para acessar como executar cada um dos testes, basta clicar nos títulos abaixo:

[Testes fim-a-fim (E2E)]()

#### Como executar?

```
make e2e
```

ou:

```
behave -v
```

[Testes de API]()

```
make api
```

ou:

```
python -m unittest discover -s tests/api/ -p "*_test.py" -v
```

[Testes Unitários]()

```
make unit
```

ou:

```
python -m unittest discover -s tests/unit/ -p "*_test.py" -v
```