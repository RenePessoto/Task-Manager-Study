from datetime import datetime
from typing import Optional

class Task:
    def __init__(self, title: str, description: Optional[str] = None, created_at=None, completed=False):
        self.title = title
        self.description = description or ""
        self.created_at = created_at or datetime.now().isoformat()
        self.completed = completed

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        # Converte o ISO para datetime
        dt = datetime.fromisoformat(self.created_at)
        data_formatada = dt.strftime("%d/%m/%Y %H:%M")
        return f"[{status}] {self.title} - {self.description} (Criada em: {data_formatada})"
