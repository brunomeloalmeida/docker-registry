import requests

class Registry:
    
    def __init__(self, username, password, registry_url, port) -> None:
        self.__auth = (username, password)
        self.url = f"{registry_url}:{port}"
        self.port = port
        
    def list_images(self) -> list:
        endpoint = f"{self.url}/v2/_catalog"
        response = requests.get(endpoint, auth=self.__auth)
        
        if response.status_code == 200:
            return response.json().get('repositories', [])
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
        
    def list_image_tags(self, image_name):
        endpoint = f"{self.url}/v2/{image_name}/tags/list"
        response = requests.get(endpoint, auth=self.__auth)
        
        if response.status_code == 200:
            return response.json().get('tags', [])
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
        
    def remove_image(self, image_name, tag_name):
        digest = self.__get_digest(image_name, tag_name)
        endpoint = f"{self.url}/v2/{image_name}/manifests/{digest}"
        response = requests.delete(endpoint, auth=self.__auth)

        if response.status_code == 202:
            print("Image deleted successfully.")
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
        
        
    def __get_digest(self, image_name, tag_name):
        headers = {
            "Accept": "application/vnd.docker.distribution.manifest.v2+json, application/vnd.oci.image.index.v1+json"
        }
        endpoint = f"{self.url}/v2/{image_name}/manifests/{tag_name}"
        response = requests.get(endpoint, headers=headers, auth=self.__auth)
        
        if response.status_code == 200:
            digest = response.headers.get("Docker-Content-Digest")
            if not digest:
                raise Exception("Docker-Content-Digest header not found in the response.")
            return digest.strip()
        else:
            raise Exception(f"Error {response.status_code}: Verifique se a tag existe e se o nome está correto.")