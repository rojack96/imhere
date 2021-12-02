import inspect
from datetime import datetime
import json
from typing import Dict
from imhere.utils import Separator, templates

class ImHere:
    def __init__(
        self, separator: Separator = Separator.BACKSLASH, 
        timestamp: bool = True,
        time_format:str="%Y-%m-%d %H:%M:%S"
    ) -> None:
        self.__separator:Separator = separator
        self.__time_format:str = time_format
        self.__template_value:str  = templates.VALUE_TS if timestamp else templates.VALUE_NO_TS
        self.__template_no_value:str = templates.NO_VALUE if timestamp else templates.NO_VALUE_NO_TS
        pass

    def log(self, var=None):
        FILE_NAME = inspect.stack()[1][1]
        CONTEXT = inspect.stack()[1][3]
        LINE_NUMBER = str(inspect.stack()[1][2])
        NOW = datetime.now().strftime(self.__time_format)

        if var is not None:
            
            var_name:str = inspect.stack()[1][4][0].split("log(")[1].replace(")\n", "")
            var_content = var

            template_result = self.__template_value.format(
                ts=NOW,
                spr=self.__separator.value,
                file_name=FILE_NAME,
                context=CONTEXT,
                line_number=LINE_NUMBER,
                var_name=var_name,
                var_content=var_content
            )
        else:
            template_result = self.__template_no_value.format(
                ts=NOW,
                spr=self.__separator.value,
                file_name=FILE_NAME,
                context=CONTEXT,
                line_number=LINE_NUMBER
            )

        return print(template_result)

    def json_log(self, var=None):
        FILE_NAME = inspect.stack()[1][1]
        CONTEXT = inspect.stack()[1][3]
        LINE_NUMBER = str(inspect.stack()[1][2])
        var_name:str = inspect.stack()[1][4][0].split("log(")[1].replace(")\n", "")
        var_content = var
        JSON_PRINT = {
                        "FILE_NAME": FILE_NAME,
                        "CONTEXT": CONTEXT,
                        "LINE": LINE_NUMBER,
                        "VARIABLE":{
                            "NAME": var_name,
                            "CONTENT": var_content
                        }
                    }
        
        if var is not None:
            return print(json.dumps(JSON_PRINT,indent=2))
        else:
            return print(json.dumps({key: JSON_PRINT[key] for key in ['FILE_NAME','CONTEXT','LINE']},indent=2))