# Contribuindo

Este projeto utiliza alguns padrões de desenvolvimento para garantir que o código fonte seja de facil entendimento para todos.

## Padrão de escrita:

Padrão de escrita utilizado é o snake case, em conjunto com o clean code.  
Todo o projeto será codificado em português, para facilitar o entendimento de todos.

### Clean Code:

Video explicativo sobre Clean Code neste [Link](https://www.youtube.com/watch?v=ln6t3uyTveQ)

Basicamente, o clean code, define que todas as variavei, funções classes e etc, precisam de seu nome escrito por extenso, e de forma objetiva, sendo assim, ao ler o nome, já é possivel saber o que aquilo faz, ou para que serve.

### Conventional Commit:

Site explicativo sobre o conventional Commit neste [Link](https://www.conventionalcommits.org/pt-br/v1.0.0/)

Ferramenta em python para auxiliar no momento da escrita da mensagem de commit neste [Link](https://pypi.org/project/conventional-commit/)

Padronização nas mensagens de commit para facilitar o entendimento das alterações de cada commit

### Padronização de nomeclatura

Documentação do Python para consultas, neste [Link](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

Classes -> Camel Case - Exemplo: `class MinhaClasse():`  
Funções -> snake_case - Exemplo: `def minha_funcao():`  
Variáveis -> snake_case - Exemplo: `nome_completo = "Seu nome"`  
Constantes -> Maiúsculo - Exemplo: `NUMERO_MAXIMO = 5`  
  
Obs: Para as variaveis, lembre-se de definir o tipo da variavel sempre que possivel, utilizando do `:`. Exemplo: `numero_qualquer: int = 5`

Exemplo de bloco de código:

```python
class Operacoes():
    def divide_dois_numeros(numerador: int, denominador: int):
        return numerador / denominador
```
