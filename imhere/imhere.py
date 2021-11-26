import inspect
from datetime import datetime
from enum import Enum
import json


class Separator(Enum):
    SLASH = '/'
    BACKSLASH = '\\'
    POINT = '.'
    VERTICAL_BAR = '|'
    HYPHEN = '-'
    UNDERSCORE = '_'


class ImHere:
    
    def __init__(
        self, separator: Separator = Separator.BACKSLASH, 
        timestamp: bool = True, 
        time_format:str="%Y-%m-%d %H:%M:%S"
    ) -> None:
        self.__separator = separator
        self.__time_format = time_format
        self.__template_value  = "[{ts}] {file_name}{spr}{context}{spr}line {line_number}{spr}{var_name}:{var_content}" if timestamp else "{file_name}{spr}{context}{spr}line {line_number}{spr}{var_name}:{var_content}"
        self.__template_no_value = "[{ts}] {file_name}{spr}{context}{spr}line {line_number}" if timestamp else "{file_name}{spr}{context}{spr}line {line_number}"
        pass

    def log(self, var=None):
        file_name = inspect.stack()[1][1]
        context = inspect.stack()[1][3]
        line_number = str(inspect.stack()[1][2])
        now = datetime.now().strftime(self.__time_format)

        if var is not None:
            
            var_name:str = inspect.stack()[1][4][0].split("log(")[1].replace(")\n", "")
            var_content = var

            template_result = self.__template_value.format(
                ts=now,
                spr=self.__separator.value,
                file_name=file_name,
                context=context,
                line_number=line_number,
                var_name=var_name,
                var_content=var_content
            )
        else:
            template_result = self.__template_no_value.format(
                ts=now,
                spr=self.__separator.value,
                file_name=file_name,
                context=context,
                line_number=line_number
            )

        return print(template_result)

    def json_log(self, var=None):
        file_name = inspect.stack()[1][1]
        context = inspect.stack()[1][3]
        line_number = str(inspect.stack()[1][2])
        
        if var is not None:
            var_name:str = inspect.stack()[1][4][0].split("log(")[1].replace(")\n", "")
            var_content = var
            
            return print(
                json.dumps(
                    {
                        "FILE_NAME": file_name,
                        "CONTEXT": context,
                        "LINE": line_number,
                        "VARIABLE":{
                            "NAME": var_name,
                            "CONTENT": var_content
                        }
                    },
                    indent=2
                )
            )
        else:
            return print(
                json.dumps(
                    {
                        "FILE_NAME": file_name,
                        "CONTEXT": context,
                        "LINE": line_number,
                    },
                    indent=2
                )
            )
        

