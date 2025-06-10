import importlib.util
import subprocess
import sys
import time
from pathlib import Path

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

def check_get_dependencies():
    console.print("[bold cyan]Verificando dependencias...[/bold cyan]")
    requirements_file = Path("requirements.txt")

    if not requirements_file.exists():
        console.print("[bold red]No se encontró requirements.txt[/bold red]")
        sys.exit(1)

    with open(requirements_file, "r", encoding="utf-8") as f:
        packages = [
            line.strip().split("==")[0]
            for line in f
            if line.strip() and not line.startswith("#")
        ]

    missing = []
    for package in packages:
        if importlib.util.find_spec(package) is None:
            missing.append(package)

    if missing:
        console.print(f"[bold yellow]Faltan: {', '.join(missing)}[/bold yellow]")
        console.print("[bold blue]Instalando dependencias...[/bold blue]")

        with Progress(
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            task = progress.add_task("[cyan]Instalando...", total=None)
            start_time = time.time()                                                                                                                                                                                                

        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
            elapsed = time.time() - start_time
            if elapsed < 2:
                time.sleep(1 - elapsed)                                                                                                                                                                                                                                             
            console.print("[bold green]Dependencias instaladas.[/bold green]")                      
        except subprocess.CalledProcessError:
            console.print("[bold red]Error al instalar dependencias.[/bold red]")
            sys.exit(1)
    else:
        console.print("[bold green]Todas las dependencias están instaladas.[/bold green]")