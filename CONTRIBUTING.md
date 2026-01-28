# Contributing to brdoc

Thank you for considering contributing to brdoc! This document outlines the process for contributing to this project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Python version and OS information
- Any relevant code snippets or error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- A clear and descriptive title
- Detailed explanation of the proposed feature
- Examples of how it would be used
- Why this enhancement would be useful

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Write tests** for any new functionality
3. **Ensure tests pass**: Run `pytest` before submitting
4. **Follow code style**: Run `black brdoc tests` to format code
5. **Update documentation** if needed
6. **Write clear commit messages**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/brdoc.git
cd brdoc

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=brdoc --cov-report=html

# Run specific test file
pytest tests/test_cpf.py

# Run specific test
pytest tests/test_cpf.py::TestCPFValidation::test_valid_cpf_formatted
```

## Code Style

This project uses:
- **Black** for code formatting (line length: 100)
- **Flake8** for linting
- **MyPy** for type checking

```bash
# Format code
black brdoc tests

# Check linting
flake8 brdoc tests --max-line-length=100

# Type checking
mypy brdoc
```

## Documentation

- Use clear, concise docstrings for all public APIs
- Follow Google-style docstring format
- Include examples in docstrings where helpful
- Update README.md for user-facing changes

## Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests when relevant

Examples:
```
Add support for RG document validation
Fix CPF validation for edge case with leading zeros
Update documentation for CNPJ.generate() method
```

## Testing Guidelines

- Write tests for all new features
- Maintain test coverage above 90%
- Test both happy paths and edge cases
- Use descriptive test names that explain what's being tested

## Release Process

Maintainers will handle releases. The process includes:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create a git tag
4. Build and publish to PyPI
5. Create GitHub release

## Questions?

Feel free to open an issue with the "question" label if you have any questions about contributing.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.