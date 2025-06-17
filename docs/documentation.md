# FastAPI Item Storage API

A API FastAPI Item Storage é uma API simples criada com FastAPI e Pydantic. Possui endpoints para criar e recuperar itens de um armazenamento de dados em memória.

## Endpoints

### `GET /`

Retorna uma mensagem de boas-vindas.

#### Resposta

- `Message` (string): Uma mensagem de boas-vindas.

### `GET /items/{item_id}`

Retorna um item específico pelo seu ID.

#### Parâmetros

- `item_id` (integer): O identificador do item.

#### Resposta

- Um objeto `Item` se existir um item com o `item_id` fornecido, caso contrário, retorna um erro 404.

### `POST /items/`

Cria um novo item e o armazena.

#### Parâmetros

- `item` (Item): O item a ser criado.

#### Resposta

- O item criado.

## Modelo de Item

O modelo de Item é definido usando Pydantic.

### Propriedades

- `name` (string): O nome do item.
- `price` (float): O preço do item.
- `description` (string, opcional): A descrição do item.

## Exemplos de Uso

### Criando um item

```bash
curl -X POST "http://localhost:8000/items/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"item1\",\"price\":15.2,\"description\":\"This is item1\"}"
```

### Obtendo um item

```bash
curl -X GET "http://localhost:8000/items/1" -H  "accept: application/json"
```

## Notas Importantes

- A API não persiste os dados, então, se o servidor for reiniciado, todos os dados serão perdidos.
- O `item_id` é gerado automaticamente e não pode ser especificado pelo usuário.

## Dependências Necessárias

- FastAPI: `pip install fastapi`
- Pydantic: `pip install pydantic`
- Uvicorn (para rodar o servidor): `pip install uvicorn`