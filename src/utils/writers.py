from abc import ABC, abstractmethod
import json


class DataTypeNotSupported(Exception):
    def __init__(self, data):
        self.data = data
        self.message = f"Data type {type(data)} is not supported for ingestion"
        super().__init__(self.message)


class Writer(ABC):
    """Interface for all writers."""

    def __init__(self):
        pass

    @abstractmethod
    def write(self, data: list | dict, *args, **kwargs) -> None:
        raise NotImplementedError("Subclasses must implement write() method")


class JSONWriter(Writer):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def _write_row(self, row: dict):
        with open(file=self.filepath, mode="a") as jout:
            json.dump(row, jout)
            jout.write("\n")

    def write(self, data: list | dict, *args, **kwargs) -> None:
        if isinstance(data, dict):
            self._write_row(data)
        elif isinstance(data, list):
            for element in data:
                self.write(element)
        else:
            raise DataTypeNotSupported(data)
