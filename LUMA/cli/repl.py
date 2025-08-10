from rich.console import Console
from rich.prompt import Prompt
from core.parsing.dual import DualParser
from parsing.dual import DualParser
from runtime.interpreter import Interpreter


class LumaREPL:
    def __init__(self):
        self.console = Console()
        self.parser = DualParser()
        self.context = {}

    def start(self):
        self.console.print("[bold magenta]🧠 LUMA REPL Interactivo[/]")
        self.console.print("Modo: [bold green]Natural[/] | Use ':sexpr' para cambiar")
        
        while True:
            try:
                inp = Prompt.ask("luma> ")
                if inp.startswith(":"):
                    self.handle_command(inp)
                else:
                    self.evaluate(inp)
            except KeyboardInterrupt:
                self.console.print("\n🛑 Interrumpido")
            except Exception as e:
                self.console.print(f"[red]❌ Error: {e}[/]")

    def evaluate(self, code):
        ast = self.parser.parse(code)
        # Aquí iría la evaluación real
        self.console.print(f"[cyan]AST Generado:[/] {ast}")

    def handle_command(self, cmd):
        commands = {
            ":sexpr": self.switch_to_sexpr,
            ":natural": self.switch_to_natural,
            ":debug": self.show_debug_info
        }
        commands.get(cmd.strip(), self.unknown_command)()

    def switch_to_sexpr(self):
        self.parser.mode = 'sexpr'
        self.console.print("[bold yellow]Modo S-Expression activado[/]")