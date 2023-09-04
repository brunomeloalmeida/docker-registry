import subprocess
import os
from contextlib import contextmanager

@contextmanager
def temporary_directory_change(path):
    """Temporarily change the working directory."""
    prev_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_dir)

class Docker:
    def __run_command(self, command):
        
        with temporary_directory_change('../'):
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        
            if result.returncode != 0:
                print(f"Error executing '{command}': {result.stderr}")
                return None
    
        return result.stdout
    
    def _stop_container(self, service_name):
        print("Stopping the registry...")
        self.__run_command(f"docker-compose stop {service_name}")
        
    def _garbage_collection(self, service_name):
        print("Running garbage collection...")
        self.__run_command(f"docker-compose run --rm {service_name} bin/{service_name} garbage-collect /etc/docker/registry/config.yml")
        
    def _up_container(self, service_name):
        print("Restarting the registry...")
        self.__run_command(f"docker-compose up -d {service_name}")
        
    def clean_images(self, service_name):
        print("Cleanning Images...")
        self._stop_container(service_name)
        self._garbage_collection(service_name)
        self._up_container(service_name)
        