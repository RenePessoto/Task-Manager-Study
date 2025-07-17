import json
import os
from manager.task import Task
import pandas as pd


print("[DEBUG] storage.py carregado")
DATA_FILE = ("tarefas.json")

def load_tasks():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["title", "description", "created_at", "completed"])
        df.to_json(DATA_FILE, orient="records", force_ascii=False, indent=4)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Task(**item) for item in data]

def save_tasks(tasks):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([task.__dict__ for task in tasks], f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"[ERRO] Não foi possível salvar o arquivo JSON: {e}")
