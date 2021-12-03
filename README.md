# ImHere
### simple log for simple debug
<br>
ImHere is an alternative of a simple print for debugging.

Return print with:

- Timestamp
- File name
- Context (function or class)
- Line of code
- Variable mame
- Variable value

## Get started

```python
from imhere import ImHere

imhere = ImHere()

def function():
    variable = 97
    imhere.log(variable)

#[2021-11-26 19:44:50] test.py\function\line 6\variable:97
```

Change default settings

```python
from imhere import ImHere, separator

imhere = ImHere(
   spr=separator.ARROW, 
   timestamp=True, 
   time_format="%y-%m-%d %H:%M:%S"
)

def function():
    variable = 97
    imhere.log(variable)

#[21-11-26 19:44:50] test.py->function->line 6->variable:97
```

Settings `separator`:

```python
SLASH = '/'
BACKSLASH = '\\'
POINT = '.'
VERTICAL_BAR = '|'
HYPHEN = '-'
UNDERSCORE = '_'
ARROW = '->'
```
To disable the timestamp print, set `timestamp=False`

To change format timestamp, set `time_format=formatTimestamp`

