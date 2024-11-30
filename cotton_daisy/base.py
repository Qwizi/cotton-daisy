from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "templates"


def generate(component_name: str):
    """
    Generate a specific component from a template.
    """
    template_path = TEMPLATE_DIR / f"{component_name}.html"
    if not template_path.exists():
        raise ValueError(f"Component {component_name} does not exist.")

    output_dir = Path.cwd() / "templates/cotton"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / f"{component_name}.html"

    with open(template_path, "r") as template, open(output_file, "w") as output:
        output.write(template.read())

    print(f"Generated {component_name} component at {output_file}")


def list_available():
    """
    List all available component templates.
    """
    available = [file.stem for file in TEMPLATE_DIR.glob("*.html")]
    for comp in available:
        print(f" - {comp}")