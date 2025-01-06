import re
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "templates"


def generate_component(component_name: str):
    """
    Generate a specific component from a template.
    """
    template_path = TEMPLATE_DIR / f"{component_name}.html"
    if not template_path.exists():
        raise ValueError(f"Component {component_name} does not exist.")

    output_dir = Path.cwd() / "templates/cotton/ui"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{component_name}.html"

    with open(template_path, "r") as template, open(output_file, "w") as output:
        content = template.read()
        cleaned_content = re.sub(r'class="\s*(.*?)\s*"', lambda m: f'class="{m.group(1).strip()}"', content,
                                 flags=re.DOTALL)
        output.write(cleaned_content)

    print(f"Generated {component_name} component at {output_file}")


def get_available_components():
    """
    Get a list of available components.
    """
    available = [file.stem for file in TEMPLATE_DIR.glob("*.html")]
    return available


def generate(component_name: str):
    """
    Generate a new DaisyUI component.
    """
    if component_name == "all":
        available = get_available_components()
        for comp in available:
            generate_component(comp)
    else:
        generate_component(component_name)


def list_available():
    """
    List all available component templates.
    """
    available = get_available_components()
    for comp in available:
        print(f" - {comp}")
