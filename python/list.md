
# Setup Local env

* https://setuptools.pypa.io/en/latest/userguide/declarative_config.html
* https://setuptools.pypa.io/en/latest/setuptools.html

### [install extr package](https://github.com/Lightning-AI/lightning/issues/2654)
If we make use of the extras_require kwarg of setup() in setup.py, we can install these extras like this:
```
pip install -e ".[testing]"
```
# or
```
pip install -e ".[dev]"
```

- Verify it: `pytest --cov-report html`


# TestCases

- test_pass-by-reference.py

- test_swap.py 
