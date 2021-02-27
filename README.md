# Trabalho-Comunicacoes-Digitais
Repositório Trabalho Comunicações Digitais sobre a criação de um gráfico animado em Python para comparação entre sinais digitais e analógicos.

## Pacotes Necessários

- Python 3.^
- Pip
- Pipenv
  - Linux: `sudo pip install pipenv` ou `sudo pip3 install pipenv`
- python3-tk
  - Arch: `sudo pacman -S tk`
  - Ubuntu: `sudo apt-get install python3-tk`
# Executar arquivo

## 1. Crie um shell com pipenv

- `pipenv shell`

## 2. Instale as bibliotecas

- `pipenv install`


## Observações:
- Frequencia digital == taxa de simbolo
- Observar os Códigos de linhas
## Melhorias 
- [ ] Acrescentar multiplos gráficos a interface (3 Gráficos)
  - [ ] Sinal Analogico
  - [ ] Sequência de bits aleatória
  - [ ] Sinal de digital correspondente a sequência de bits
- [ ] Controlar a taxa de símbolos (Somente)
- [ ] Ter a opção de escolher o pulso conformador (ComboBox)
  - [ ] Mapeamento (bits -> nº real) 1 -> 1 / 0 -> -1
  - [ ] Pulso retangular de meio periodo
  - [ ] Pulso retangular de periodo completo
  - [ ] Pulso trinagular

## Bibliotecas utilizadas

- scipy
- matplotlib
- autopep8
- numpy

## Todo
- [ ] [Kristhyan, Allef, Mikael]  Interface 
- [ ] [Mário] Sinal Analogico 
- [ ] [João] Sequência de bits aleatória 
- [ ] Sinal de digital correspondente a sequência de bits
- [ ] Controlar a taxa de símbolos
- [ ] Pulso conformador (ComboBox)
  - [ ] Mapeamento (bits -> nº real) 1 -> 1 / 0 -> -1
  - [ ] [Fabrício] Pulso retangular de meio periodo 
  - [ ] [Antônio] Pulso retangular de periodo completo 
  - [ ] [Felipe] Pulso trinagular