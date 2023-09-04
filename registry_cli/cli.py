from registry_cli.automation import Automation
import typer
from registry_cli import __app_name__, __version__

app = typer.Typer(
    add_completion=False,
    help=f"{__app_name__} | Version: {__version__}",
    no_args_is_help=True
)

@app.command("list-images")
def list_images():
    return Automation().list_images()

@app.command("list-tags")
def list_tags(image_name: str = typer.Argument(...)):
    return Automation().list_tags(image_name)

@app.command("remove-image")
def remove_image(
    image_name: str = typer.Argument(...),
    tag_name: str = typer.Argument(...)
):
    return Automation().remove_image(image_name, tag_name)

if __name__ == "__main__":
    app()
    


