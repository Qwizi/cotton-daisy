import typer

from cotton_daisy.base import generate, list_available

app = typer.Typer(
    help="CLI tool for creating DaisyUI components for Django-Cotton."
)


@app.command()
def add(component: str):
    """
    Generate a new DaisyUI component.
    """
    typer.echo(f"Adding component: {component}...")
    generate(component)


@app.command()
def list():
    """
    List all available DaisyUI components.
    """
    typer.echo("Available components:")
    list_available()


if __name__ == "__main__":
    app()
