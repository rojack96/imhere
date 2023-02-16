from enum import Enum

class separator(Enum):
    SLASH:str = '/'
    BACKSLASH:str = '\\'
    POINT:str = '.'
    VERTICAL_BAR:str = '|'
    HYPHEN:str = '-'
    UNDERSCORE:str = '_'
    ARROW:str = '->'

class templates:
    VALUE_TS:str = "[{ts}] {file_name}{spr}{context}{spr}line {line_number}{spr}{var_name}:{var_content}"
    VALUE_NO_TS:str ="{file_name}{spr}{context}{spr}line {line_number}{spr}{var_name}:{var_content}"
    NO_VALUE:str = "[{ts}] {file_name}{spr}{context}{spr}line {line_number}"
    NO_VALUE_NO_TS:str = "{file_name}{spr}{context}{spr}line {line_number}"

class InfoBuilder:
    def __init__(self, file_name: str, context: str, line_number: str, var_name: str, timestamp: str):
        self.file_name: str = file_name
        self.context: str = context
        self.line_number: str = line_number
        self.var_name: str = var_name
        self.timestamp: str = timestamp
    