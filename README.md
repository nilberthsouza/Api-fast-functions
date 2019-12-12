#Keep notes on Terminal

Em desenvolvimento usando a tecnologia

https://firefly-python.readthedocs.io/en/latest/

## Para levantar um server basta

```

$pipenv shell

$pip install firefly-python

$firefly notes.notes seleciona.seleciona insert.insert remove.remove

```

### fazendo requisição de uma nota no banco de dados  pelo id 

``` 
curl -d '{"num":1}' http://127.0.0.1:8000/seleciona

```
para armazenas é possivel usar 

para remover é a mesma coisa

``` 
curl -d '{"num":1}' http://127.0.0.1/8000/remove

```

pra colocar o resultado em um txt é possivel usar >> chamada.txt


### Para inserir no banco de dados uma nova nota

```
curl -d '{"t":2,"b":"recado novo"}' http://127.0.0.1:8000/insert

```


