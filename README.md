# brdoc - Brazilian Document Validator

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A lightweight, fast, and reliable Python library for validating, formatting, and generating Brazilian CPF and CNPJ documents.

## Features

**Easy to use** - Simple, intuitive API  
**Fast** - Pure Python implementation with no dependencies  
**Reliable** - Comprehensive test coverage  
**Well documented** - Clear examples and docstrings  
**Type hints** - Full typing support for better IDE integration  

## Installation

```bash
pip install brdoc
```

Or install from source:

```bash
git clone https://github.com/IHenriqueCSN/brdoc.git
cd brdoc
pip install -e .
```

## Quick Start

### CPF (Cadastro de Pessoas Físicas)

```python
from brdoc import CPF

# Validate a CPF
cpf = CPF("111.444.777-35")
print(cpf.is_valid())  # True

# Quick validation
print(CPF.validate("111.444.777-35"))  # True

# Format a CPF
cpf = CPF("11144477735")
print(cpf.formatted)  # "111.444.777-35"

# Get only digits
print(cpf.digits)  # "11144477735"

# Generate a valid CPF
new_cpf = CPF.generate()
print(new_cpf.formatted)  # "XXX.XXX.XXX-XX" (random valid CPF)
print(new_cpf.is_valid())  # True
```

### CNPJ (Cadastro Nacional da Pessoa Jurídica)

```python
from brdoc import CNPJ

# Validate a CNPJ
cnpj = CNPJ("11.222.333/0001-81")
print(cnpj.is_valid())  # True

# Quick validation
print(CNPJ.validate("11.222.333/0001-81"))  # True

# Format a CNPJ
cnpj = CNPJ("11222333000181")
print(cnpj.formatted)  # "11.222.333/0001-81"

# Get only digits
print(cnpj.digits)  # "11222333000181"

# Generate a valid CNPJ
new_cnpj = CNPJ.generate()
print(new_cnpj.formatted)  # "XX.XXX.XXX/XXXX-XX" (random valid CNPJ)
print(new_cnpj.is_valid())  # True
```

## Advanced Usage

### Working with Collections

CPF and CNPJ objects are hashable and can be used in sets and as dictionary keys:

```python
from brdoc import CPF, CNPJ

# Use in sets
cpfs = {
    CPF("111.444.777-35"),
    CPF("11144477735"),  # Same as above, will be deduplicated
    CPF("231.002.999-00"),
}
print(len(cpfs))  # 2

# Use as dictionary keys
people = {
    CPF("111.444.777-35"): "João Silva",
    CNPJ("11.222.333/0001-81"): "Acme Corp",
}
```

### Input Flexibility

The library handles various input formats:

```python
from brdoc import CPF

# All of these work
CPF("111.444.777-35")  # Formatted
CPF("11144477735")      # Plain digits
CPF("111 444 777 35")   # With spaces
CPF("111.444.777/35")   # Mixed formatting
```

### Error Handling

```python
from brdoc import CPF
from brdoc.exceptions import InvalidCPFError

cpf = CPF("123")  # Too short

# Check validity
if cpf.is_valid():
    print(cpf.formatted)
else:
    print("Invalid CPF")

# Or handle exceptions when formatting
try:
    print(cpf.formatted)
except InvalidCPFError as e:
    print(f"Error: {e}")
```

## API Reference

### CPF Class

#### Methods
- `__init__(cpf: str)` - Initialize with a CPF string
- `is_valid() -> bool` - Check if CPF is valid
- `validate(cpf: str) -> bool` - Class method for quick validation
- `generate() -> CPF` - Class method to generate a valid random CPF

#### Properties
- `digits: str` - Get CPF as plain digits (11 characters)
- `formatted: str` - Get formatted CPF (XXX.XXX.XXX-XX)

### CNPJ Class

#### Methods
- `__init__(cnpj: str)` - Initialize with a CNPJ string
- `is_valid() -> bool` - Check if CNPJ is valid
- `validate(cnpj: str) -> bool` - Class method for quick validation
- `generate() -> CNPJ` - Class method to generate a valid random CNPJ

#### Properties
- `digits: str` - Get CNPJ as plain digits (14 characters)
- `formatted: str` - Get formatted CNPJ (XX.XXX.XXX/XXXX-XX)

## Validation Rules

### CPF
- Must have exactly 11 digits
- Cannot be all the same digit (e.g., "111.111.111-11")
- Must pass the check digit algorithm

### CNPJ
- Must have exactly 14 digits
- Cannot be all the same digit (e.g., "11.111.111/1111-11")
- Must pass the check digit algorithm

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/brdoc.git
cd brdoc

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=brdoc --cov-report=html

# Run specific test file
pytest tests/test_cpf.py
```

### Code Quality

```bash
# Format code with black
black brdoc tests

# Check code style
flake8 brdoc tests

# Type checking
mypy brdoc
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Guidelines
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for your changes
4. Ensure all tests pass (`pytest`)
5. Format your code (`black .`)
6. Commit your changes (`git commit -m 'Add some amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Validation algorithms based on official Brazilian government specifications
- Inspired by the need for a modern, well-tested CPF/CNPJ library

## Related Projects

- [validate-br](https://github.com/othername/validate-br) - Another Brazilian document validator
- [python-cpf](https://github.com/anothername/python-cpf) - CPF-only validator

## Support

If you encounter any issues or have questions, please file an issue on the [GitHub issue tracker](https://github.com/IHenriqueCSN/brdoc/issues).
