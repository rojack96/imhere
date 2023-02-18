# ImHere

### simple log for simple debug

<br>

ImHere is an alternative of a simple print for debugging.

Return print with:

- Timestamp

- File name

- Context (function_name or class_name)

- Line of code

- Variable name

- Variable value



## Get started

```python
from imhere import ImHere

imhere = ImHere()

def foo_function():
    foo = 96
    imhere.log(foo)    
"""[2023-02-17 08:30:50] test.py/foo_function/line 6/foo:96""""
```

Change default settings

```python
from imhere import ImHere, spr

imhere = ImHere(
    separator = spr.ARROW,
    timestamp = True,
    time_format = "%y-%m-%d %H:%M"
)

imhere_json = ImHere(
    json_indent = True,
    indent_space = 4
)

def foo_function():
    foo = 96
    imhere.log(foo)
"""[23-02-17 08:30] test.py->foo_function->line 6->variable:96"""

    imhere_json.json_log(foo)
"""
{
    "FILE_NAME": "/test.py",
    "CONTEXT": "foo_function",
    "LINE": "6",
    "VARIABLE": {
        "NAME": "foo",
        "CONTENT": 96
    }
}
"""
```

setting for **log()**

| Variable      | Type            | Info                                                                                                                                                                                                                                                                                                      |
| ------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `separator`   | `<class 'spr'>` | **SLASH** = '/'<br/>**BACKSLASH** = '\\'<br/>**DOT** = '.'<br/>**VERTICAL_BAR** = '\|'<br/>**HYPHEN** = '-'<br/>**UNDERSCORE** = '_'<br/>**ARROW** = '->'<br/><u>separator default</u>: **SLASH**                                                                                                         |
| `timestamp`   | `bool`          | set `True` if you choose to show timestamp, `False` otherwise<br/>__timestamp default_: `True`                                                                                                                                                                                                            |
| `time_format` | `str`           | set a custom timestamp format<br/><u>format default</u>: `"%Y-%m-%d %H:%M:%S"`                                                                                                                                                                                                                            |
| `template`    | `str`           | template log.<br/>**NOTICE** use same name from base template:<br/><br/>- *ts*<br/>- *file_name*<br/>- *spr*<br/>- *context*<br/>- *line_number*<br/>- *var_name*<br/>- *var_content*<br/><u>template default</u>: <br/>`"{file_name}{spr}{context}{spr}line {line_number}{spr}{var_name}:{var_content}"` |

setting for **json_log()**

| Variable       | Type   | Info                                                                                     |
| -------------- | ------ | ---------------------------------------------------------------------------------------- |
| `json_indent`  | `bool` | set `True` f you choose to show json with indent<br/><u>json_indent default</u>: `False` |
| `indent_space` | `int`  | if `json_indent = True` set the number of indent space<br/><u>indent_space</u>: `2`      |




