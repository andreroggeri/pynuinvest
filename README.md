# pynuinvest

Acesse seus investimentos da NuInvest pelo Python (Experimental)

## Instalando

`pip install git+https://github.com/andreroggeri/pynuinvest.git`

## Contornando o Cloudflare

A NuInvest utiliza o Cloudflare para evitar ataques e acessos não autorizados.

Para contornar isso utilizamos o [FlareSolverr][1] para resolver os desafios.

[1]: https://github.com/FlareSolverr/FlareSolverr

## Inicializando o FlareSolverr
Basta iniciar uma instancia utilizando docker:

`docker run -d --rm -p 8191:8191 andreroggeri/flaresolverr`

Após isso ele estará executando e acessível localmente na porta 8191

## Autenticando

Antes de obter os dados de investimentos é necessário autenticar.

```python
from pynuinvest import NuInvest

nu = NuInvest()
# uid pode ser gerado com o módulo uuid.
# Se ele for reutilizado é possível autenticar sem o easytoken depois do primeiro login
nu.authenticate('CPF sem pontos', 'senha', 'uid', 'codigo easytoken')
```

## Obtendo as informações dos investimentos

```python
from pynuinvest import NuInvest

nu = NuInvest()
# Exemplo acima de como utilizar
# nu.authenticate()
investment_data = nu.get_investment_data()

# Printa dicionário contendo os dados de todos os investimentos
print(investment_data)
```