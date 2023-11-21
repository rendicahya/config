# Python Config

A simple configuration for Python projects.

## Installation
This library is designed to be used as a git submodule:
```bash
git submodule add https://github.com/rendicahya/python_config.git
```

## Usage:

```python
from python_config import Config

conf = Config('config.json')

print(conf.some.value)
```
