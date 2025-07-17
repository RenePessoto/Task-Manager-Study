import typer
from rich.console import Console
from rich.table import Table
from manager.task import Task
from manager import storage

app = typer.Typer()
console = Console()

@app.command("add")
def add_task(title: str, description: str = ""):
    tasks = storage.load_tasks()
    task = Task(title, description)
    tasks.append(task)
    storage.save_tasks(tasks)
    console.print(f":white_check_mark: Tarefa '{title}' adicionada com sucesso!")

@app.command("list")
def list_tasks():
    tasks = storage.load_tasks()
    if not tasks:
        console.print("Nenhuma tarefa encontrada.")
        return

    table = Table(title="Minhas Tarefas")
    table.add_column("ID", justify="right")
    table.add_column("Título")
    table.add_column("Descrição")
    table.add_column("Criada em")
    table.add_column("Status")

    for i, task in enumerate(tasks, 1):
        dt = task.created_at.split("T")[0].replace("-", "/")
        status = "✅" if task.completed else "⏳"
        table.add_row(str(i), task.title, task.description, dt, status)

    console.print(table)

@app.command("complete")
def complete_task(task_id: int):
    tasks = storage.load_tasks()
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1].complete()
        storage.save_tasks(tasks)
        console.print(f":tada: Tarefa [bold]{tasks[task_id - 1].title}[/bold] concluída!")
    else:
        console.print(f":warning: Tarefa com ID {task_id} não encontrada.")

def main():
    app()

if __name__ == "__main__":
    main()
