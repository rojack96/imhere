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
from imhere.imhere import ImHere

imhere = ImHere()

def function():
    variable = 97
    imhere.log(variable)

#[2021-11-26 19:44:50] test.py\function\line 6\variable:97
```

È possibile cambiare alcune impostazioni

```python
from imhere.imhere import ImHere, Separator

imhere = ImHere(
   separator=Separator.ARROW, 
   timestamp=True, 
   time_format="%y-%m-%d %H:%M:%S"
)

def function():
    variable = 97
    imhere.log(variable)

#[21-11-26 19:44:50] test.py->function->line 6->variable:97
```

Tra le impostazioni del Separator abbiamo:

```python
SLASH = '/'
BACKSLASH = '\\'
POINT = '.'
VERTICAL_BAR = '|'
HYPHEN = '-'
UNDERSCORE = '_'
ARROW = '->'
```

Se si vuole disattivare il timestamp settarlo a `False`
Se si vuole cambiare il formato del timestamp si può farlo tramite `time_format`

