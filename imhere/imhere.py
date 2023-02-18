import inspect
import json
from datetime import datetime

from imhere.utils import spr, InfoBuilder

class ImHere:
    """
    ImHere is an alternative of a simple print for debugging.
    """
    def __init__(
        self, 
        separator: spr = spr.SLASH, 
        timestamp: bool = True,
        time_format:str="%Y-%m-%d %H:%M:%S",
        json_indent: bool = False,
        indent_space: int = 2,
        #template: str = "[{ts}] {file_name}{spr}{context}{spr}line {line_number}{spr}{var_name}:{var_content}" 
        template: str = "{file_name}{spr}{context}{spr}line {line_number}{spr}{var_name}:{var_content}"
    ) -> None:
    
        self.__separator:spr = separator
        self.__time_format:str = time_format
        self.__template:str  = template if not timestamp else "[{ts}] " + template
        self.__json_indent: bool = json_indent
        self.__indent_space: int = indent_space
        pass

    def log(self, variable=None):
        """
        log(variable_foo) return a log in this format:

        [2023-02-17 08:30:50] test.py/function_name/line 6/variable_foo:96
        """
        try:
            if variable:
                return self.__log_formatter(variable)
            return self.__log_formatter()
        except Exception as e:
            return e

    def json_log(self, variable=None):
        """
        json_log(variable_foo) return a log in this format:

        {
            "FILE_NAME": "/test.py",
            "CONTEXT": "function_name",
            "LINE": "6",
            "VARIABLE": {
                "NAME": "variable_foo",
                "CONTENT": 96
            }
        }
        """
        try:
            if variable:    
                return self.__log_formatter(variable,True)
            return self.__log_formatter(None,True)
        except Exception as e:
            return e

    def __info_builder(self) -> InfoBuilder:
        """
        constructor of info retrived from inspect.stack()
        """
        try:
            #TODO
            # try to improve a detect a stck level
            # remove a static number (in this case 3)
            instack = inspect.stack()[3]

            _, _, after = instack.code_context[0].partition("log(")
            variable_name, _, _ = after.partition(")")

            info = InfoBuilder(
                file_name = instack.filename,
                context = instack.function,
                line_number = instack.lineno,
                var_name= variable_name,
                timestamp = datetime.now().strftime(self.__time_format)
            )
            return info
        except Exception as e:
            return e

    def __log_formatter(self, variable=None, json_log: bool = False) -> None:
        """
        log formatter, return a format in simple line text or json
        """
        try:
            indent:int = self.__indent_space if self.__json_indent else None
            info: InfoBuilder = self.__info_builder()

            JSON_FORMAT_BASE = {
                            "FILE_NAME": info.file_name,
                            "CONTEXT": info.context,
                            "LINE": info.line_number,
                        }

            if variable:
                var_name:str = info.var_name
                var_content = variable

                if json_log:
                    result = JSON_FORMAT_BASE 
                    result["VARIABLE"] = {
                                "NAME": var_name,
                                "CONTENT": var_content
                            }
                    result = json.dumps(result, indent=indent)
                else:
                    result = self.__template.format(
                        ts = info.timestamp,
                        spr = self.__separator.value,
                        file_name = info.file_name,
                        context = info.context,
                        line_number = info.line_number,
                        var_name = var_name,
                        var_content = var_content
                    )
            else:
                if json_log:
                    result = json.dumps(JSON_FORMAT_BASE,indent=indent)
                else:
                    template_value = self.__template.replace("{spr}{var_name}:{var_content}", "")    
                    
                    result = template_value.format(
                        ts = info.timestamp,                
                        spr = self.__separator.value,
                        file_name = info.file_name,
                        context = info.context,
                        line_number = info.line_number
                    )
            
            return print(result)
        except Exception as e:
            return e

    