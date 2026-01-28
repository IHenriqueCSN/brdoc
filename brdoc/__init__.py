"""
brdoc - Brazilian Document Validator
A Python library for validating, formatting, and generating Brazilian CPF and CNPJ documents.
"""

from .cpf import CPF
from .cnpj import CNPJ
from .exceptions import InvalidDocumentError

__version__ = "0.1.0"
__all__ = ["CPF", "CNPJ", "InvalidDocumentError"]
