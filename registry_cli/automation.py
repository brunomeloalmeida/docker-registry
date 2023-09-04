from dotenv import load_dotenv
from registry_cli.registry import Registry
from registry_cli.utils.core import Core
import os

class Automation:
    def __init__(self) -> None:
        load_dotenv()
        __registry_username = os.getenv("REGISTRY_USERNAME")
        __registry_password = os.getenv("REGISTRY_PASSWORD")
        __registry_url = os.getenv("REGISTRY_URL")
        __registry_port = os.getenv("REGISTRY_PORT")
        self.registry_client = Registry(
            username=__registry_username,
            password=__registry_password,
            registry_url=__registry_url,
            port=__registry_port
        )
        self.core_client = Core()
        
    
    def list_images(self) -> None:
        images = self.registry_client.list_images()
        self.core_client.print_table(["Image Names"], [(img,) for img in images])
    
    def list_tags(self, image_name: str) -> None:
        tags = self.registry_client.list_image_tags(image_name=image_name)
        self.core_client.print_table(["Image Tags"], [(tag,) for tag in tags])
    
    def remove_image(self, image_name, tag_name):
        self.registry_client.remove_image(
            image_name=image_name,
            tag_name=tag_name
        )
