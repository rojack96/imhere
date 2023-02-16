import inspect
import json
from datetime import datetime

from imhere.utils import separator, templates, InfoBuilder

class ImHere:
    def __init__(
        self, spr: separator = separator.BACKSLASH, 
        timestamp: bool = True,
        time_format:str="%Y-%m-%d %H:%M:%S"
    ) -> None:
    
        self.__spr:separator = spr
        self.__time_format:str = time_format
        self.__template_value:str  = templates.VALUE_TS if timestamp else templates.VALUE_NO_TS
        self.__template_no_value:str = templates.NO_VALUE if timestamp else templates.NO_VALUE_NO_TS
        pass

    def __info_builder(self) -> InfoBuilder:

        instack = inspect.stack()[2]

        info = InfoBuilder(
            file_name = instack.filename,
            context = instack.function,
            line_number = str(instack.lineno),
            var_name = instack.code_context[0].split("log(")[1].replace(")\n", ""),
            timestamp = datetime.now().strftime(self.__time_format)
        )
        return info

    def log(self, variable=None):

        info: InfoBuilder = self.__info_builder()
        
        NOW = info.timestamp

        if variable:
            var_name:str = info.var_name
            var_content = variable

            template_result = self.__template_value.format(
                ts = info.timestamp,
                spr = self.__spr.value,
                file_name = info.file_name,
                context = info.context,
                line_number = info.line_number,
                var_name = var_name,
                var_content = var_content
            )
        else:
            template_result = self.__template_no_value.format(
                ts = info.timestamp,                
                spr = self.__spr.value,
                file_name = info.file_name,
                context = info.context,
                line_number = info.line_number
            )
        return print(template_result)

    def json_log(self, variable=None):

        info: InfoBuilder = self.__info_builder()
        
        JSON_FORMAT = {
                        "FILE_NAME": info.file_name,
                        "CONTEXT": info.context,
                        "LINE": info.line_number,
                    }
        
        if variable:
            var_name:str = info.var_name
            var_content = variable

            JSON_FORMAT["VARIABLE"] = {
                            "NAME": var_name,
                            "CONTENT": var_content
                        }
            return print(json.dumps(JSON_FORMAT,indent=2))
        return print(json.dumps(JSON_FORMAT,indent=2))