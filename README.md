# ✅ Gerenciador de Tarefas CLI

Um gerenciador de tarefas simples via linha de comando (CLI) usando **Python**, **Typer**, **Rich** e **JSON** para persistência local.

---

## 🚀 Funcionalidades

- 📌 Adicionar tarefas
- 📋 Listar tarefas
- ✅ Marcar tarefas como concluídas
- 🗑️ Remover tarefas
- 📊 Visualizar estatísticas (total, pendentes, concluídas)

---

## 🧰 Tecnologias

- [Python 3.12+](https://www.python.org/)
- [Typer](https://typer.tiangolo.com/)
- [Rich](https://github.com/Textualize/rich)
- [JSON](https://www.json.org/)
- Estrutura modular com pacote `manager/`

---

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/RenePessoto/gerenciador_tarefas.git
cd gerenciador_tarefas
```

2. Crie o ambiente virtual:
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:

- Windows:
  ```bash
  .venv\Scripts\activate
  ```

- Linux/Mac:
  ```bash
  source .venv/bin/activate
  ```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## ▶️ Como usar

### ➕ Adicionar uma tarefa:
```bash
python -m manager.main add "Estudar Python com ChatGPT"
```

### 📋 Listar tarefas:
```bash
python -m manager.main list
```

### ✅ Concluir uma tarefa:
```bash
python -m manager.main done 1
```

### 🗑️ Remover uma tarefa:
```bash
python -m manager.main remove 1
```

### 📊 Ver estatísticas:
```bash
python -m manager.main stats
```

---

## 📁 Estrutura do Projeto

```
gerenciador_tarefas/
├── tarefas.json               # Armazenamento local das tarefas
├── requirements.txt
└── src/
    └── manager/
        ├── __init__.py
        ├── main.py            # Ponto de entrada
        ├── storage.py         # Leitura/gravação de tarefas
        └── task.py            # Definição da classe Task
```

---

## 💡 Próximos Passos

- [ ] Suporte a prazos e lembretes
- [ ] Exportação em CSV
- [ ] Interface web com FastAPI
- [ ] Testes automatizados com Pytest

---

## 👨‍💻 Autor

Desenvolvido por [Rene Pessoto](https://github.com/RenePessoto) — buscando dominar Python e se tornar engenheiro de software 💻🚀

---

## 🧠 Licença

Projeto livre para fins educacionais. Faça bom uso e contribua!