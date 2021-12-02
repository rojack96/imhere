from enum import Enum

class Separator(Enum):
    SLASH = '/'
    BACKSLASH = '\\'
    POINT = '.'
    VERTICAL_BAR = '|'
    HYPHEN = '-'
    UNDERSCORE = '_'
    ARROW = '->'

class templates:
    VALUE_TS:str = "[{ts}] {file_name}{spr}{context}{spr}line {line_number}{spr}{var_name}:{var_content}"
    VALUE_NO_TS:str ="{file_name}{spr}{context}{spr}line {line_number}{spr}{var_name}:{var_content}"
    NO_VALUE:str = "[{ts}] {file_name}{spr}{context}{spr}line {line_number}"
    NO_VALUE_NO_TS:str = "{file_name}{spr}{context}{spr}line {line_number}"