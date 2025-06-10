from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box

console = Console()

def show_header():
    header = """
[bold blue]
 █████╗ ████████╗██╗██████╗ 
██╔══██╗╚══██╔══╝██║██╔══██╗
███████║   ██║   ██║██████╔╝
██╔══██║   ██║   ██║██╔═══╝ 
██║  ██║   ██║   ██║██║     
╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝     
[/bold blue]
[bold white]Agencia de Transporte Interplanetario · ATIP[/bold white]
    """
    console.print(Panel(header, style="bold cyan", padding=(1, 4)))

def show_menu():
    table = Table(title="[bold green]Menú Principal[/bold green]", box=box.ROUNDED, expand=False)
    table.add_column("Opción", justify="center", style="bold cyan")
    table.add_column("Descripción", style="bold white")
    table.add_row("1", "Iniciar Simulador")
    table.add_row("2", "Ver instrucciónes")
    console.print(table)

def main():
    while True:
        console.clear()
        show_header()
        show_menu()
        choice = Prompt.ask("\n[bold cyan]Selecciona una opción[/bold cyan]", choices=["1", "2"])

        if choice == "1":
            console.print("[bold green]Iniciando el simulador...[/bold green]")
            break
        elif choice == "2":
            console.print("[bold green]Mostrando instrucciones...[/bold green]")
            break

if __name__ == "__main__":
    main()
