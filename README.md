# 📌 fast_zero

Pequena API de exemplo construída com **FastAPI** para gerenciar um cadastro simples de usuários em memória. O projeto foi desenvolvido como parte de um curso de FastAPI e visa demonstrar os conceitos básicos de criação de rotas, validação com Pydantic e testes automatizados.

---

## 🔍 Estrutura do projeto

```
fast_zero/
├── pyproject.toml          # metadados do pacote e dependências
├── README.md               # (esta documentação)
├── fast_zero/
│   ├── __init__.py
│   ├── app.py              # aplicação FastAPI principal
│   └── schemas.py          # modelos Pydantic usados pela API
└── tests/
    ├── __init__.py
    └── test_app.py         # testes com TestClient
```

---

## 🚀 Funcionalidades

- **GET /**: rota raiz retorna uma mensagem de boas‑vindas.
- **POST /users/**: cria um novo usuário com `username`, `email` e `password`. Retorna a representação pública do usuário (sem senha) e atribui um `id` incremental.
- **DELETE /users/{user_id}**: remove um usuário pelo `id` e responde com uma mensagem de sucesso.

⚠️ *Dados são mantidos apenas em uma lista na memória (`database`) – não há persistência entre execuções.*

---

## 🧠 Modelos de dados (schemas.py)

- **UserSchema** – entrada para criação de usuário.
- **UserPublic** – saída pública (exclui a senha).
- **UserDB** – modelo interno que estende `UserSchema` adicionando `id`.
- **Message** – resposta genérica com um campo `message`.

Todos os modelos usam Pydantic para validação automática.

---

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU_USUARIO/fastAPI_course_todo_list.git
   cd fastAPI_course_todo_list/fast_zero
   ```

2. Crie e ative um virtualenv (recomendado):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt   # ou 'pip install fastapi[all] pytest'
   ```

> **Nota:** o `pyproject.toml` contém as dependências; você pode usar `poetry install` se preferir.

---

## 🏃‍♂️ Executando a API

Inicie o servidor com `uvicorn`:

```bash
uvicorn fast_zero.app:app --reload
```

Acesse a documentação interativa no navegador:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🔧 Testes

O conjunto de testes usa `fastapi.testclient` e `pytest`.

Execute-os com:

```bash
pytest
```

Os testes cobrem:

1. Verificação da rota raiz.
2. Criação de usuário.
3. Exclusão de usuário existente.

---

## ✍️ Contribuições

1. Faça um *fork* do repositório.
2. Crie um branch com a sua feature/bugfix.
3. Abra um *pull request* descrevendo as alterações.

---

## 📝 Licença

Distribuído sob a licença **MIT**. Consulte o arquivo `LICENSE` para detalhes.

---

> 💡 **Dica de melhoria**: há um pequeno erro na rota de exclusão (`app.delete('/users/`{users_id}')`); deveria ser `'/users/{user_id}'`. Corrija se for utilizar em produção.

---

Se precisar de ajuda com qualquer etapa, estou à disposição!
