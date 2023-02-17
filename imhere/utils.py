from enum import Enum

class spr(Enum):
    SLASH:str = '/'
    BACKSLASH:str = '\\'
    POINT:str = '.'
    VERTICAL_BAR:str = '|'
    HYPHEN:str = '-'
    UNDERSCORE:str = '_'
    ARROW:str = '->'

class InfoBuilder:
    def __init__(self, file_name: str, context: str, line_number: str, var_name: str, timestamp: str):
        self.file_name: str = file_name
        self.context: str = context
        self.line_number: str = line_number
        self.var_name: str = var_name
        self.timestamp: str = timestamp

# class LogFormatter:
#     def __init__(self, timestamp:str, spr:str, file_name:str, context:str, line_number:str, var_name:str, var_content:str):
#         self.timestamp:str = timestamp,
#         self.spr: str = spr,
#         self.file_name: str = file_name,
#         self.context: str = context,
#         self.line_number: str = line_number,
#         self.var_name: str = var_name,
#         self.var_content: str = var_content