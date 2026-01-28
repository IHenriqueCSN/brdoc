"""Custom exceptions for the brdoc library."""


class InvalidDocumentError(ValueError):
    """Raised when a document number is invalid."""
    pass


class InvalidCPFError(InvalidDocumentError):
    """Raised when a CPF number is invalid."""
    pass


class InvalidCNPJError(InvalidDocumentError):
    """Raised when a CNPJ number is invalid."""
    pass
