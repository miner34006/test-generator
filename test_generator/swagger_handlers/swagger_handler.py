from abc import ABC, abstractmethod


class SwaggerHandler(ABC):
    format_name = 'AbstractSwaggerHandler'

    @abstractmethod
    def write_swagger_interface(self, interface_file_path: str,  method: str, path: str) -> None:
        """
        Генерируем примерный интерфейс в *Api.py
        """
        ...
