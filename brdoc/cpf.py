"""CPF (Cadastro de Pessoas Físicas) validation and utilities."""

import re
import random
from typing import Optional
from .exceptions import InvalidCPFError


class CPF:
    """
    CPF validator, formatter, and generator.

    CPF (Cadastro de Pessoas Físicas) is the Brazilian tax identification number
    for individuals. It consists of 11 digits with a specific validation algorithm.

    Examples:
        >>> cpf = CPF("111.444.777-35")
        >>> cpf.is_valid()
        True
        >>> cpf.formatted
        '111.444.777-35'
        >>> cpf.digits
        '11144477735'

        >>> CPF.validate("111.444.777-35")
        True

        >>> new_cpf = CPF.generate()
        >>> new_cpf.is_valid()
        True
    """

    def __init__(self, cpf: str):
        """
        Initialize a CPF instance.

        Args:
            cpf: CPF string with or without formatting (dots and dash)
        """
        self._original = cpf
        self._digits = self._clean(cpf)

    @staticmethod
    def _clean(cpf: str) -> str:
        """Remove all non-digit characters from CPF string."""
        return re.sub(r"\D", "", cpf)

    @property
    def digits(self) -> str:
        """Get CPF as plain digits string."""
        return self._digits

    @property
    def formatted(self) -> str:
        """
        Get CPF formatted with dots and dash (XXX.XXX.XXX-XX).

        Returns:
            Formatted CPF string

        Raises:
            InvalidCPFError: If CPF doesn't have exactly 11 digits
        """
        if len(self._digits) != 11:
            raise InvalidCPFError(f"CPF must have 11 digits, got {len(self._digits)}")

        return f"{self._digits[:3]}.{self._digits[3:6]}.{self._digits[6:9]}-{self._digits[9:]}"

    def is_valid(self) -> bool:
        """
        Check if the CPF is valid.

        A valid CPF must:
        - Have exactly 11 digits
        - Not be a known invalid sequence (all same digits)
        - Pass the check digit algorithm

        Returns:
            True if valid, False otherwise
        """
        # Must have 11 digits
        if len(self._digits) != 11:
            return False

        # Cannot be all same digits (known invalid CPFs)
        if self._digits == self._digits[0] * 11:
            return False

        # Validate check digits
        return self._validate_check_digits()

    def _validate_check_digits(self) -> bool:
        """Validate the two check digits using CPF algorithm."""
        # Calculate first check digit
        sum_first = sum(int(self._digits[i]) * (10 - i) for i in range(9))
        first_digit = (sum_first * 10) % 11
        if first_digit == 10:
            first_digit = 0

        if int(self._digits[9]) != first_digit:
            return False

        # Calculate second check digit
        sum_second = sum(int(self._digits[i]) * (11 - i) for i in range(10))
        second_digit = (sum_second * 10) % 11
        if second_digit == 10:
            second_digit = 0

        return int(self._digits[10]) == second_digit

    @classmethod
    def validate(cls, cpf: str) -> bool:
        """
        Class method to quickly validate a CPF string.

        Args:
            cpf: CPF string to validate

        Returns:
            True if valid, False otherwise

        Example:
            >>> CPF.validate("111.444.777-35")
            True
        """
        return cls(cpf).is_valid()

    @classmethod
    def generate(cls, formatted: bool = False) -> "CPF":
        """
        Generate a valid random CPF.

        Args:
            formatted: If True, return formatted CPF; otherwise plain digits

        Returns:
            A new CPF instance with a valid random CPF

        Example:
            >>> cpf = CPF.generate()
            >>> cpf.is_valid()
            True
        """
        # Generate first 9 digits randomly
        base_digits = [random.randint(0, 9) for _ in range(9)]

        # Calculate first check digit
        sum_first = sum(base_digits[i] * (10 - i) for i in range(9))
        first_digit = (sum_first * 10) % 11
        if first_digit == 10:
            first_digit = 0
        base_digits.append(first_digit)

        # Calculate second check digit
        sum_second = sum(base_digits[i] * (11 - i) for i in range(10))
        second_digit = (sum_second * 10) % 11
        if second_digit == 10:
            second_digit = 0
        base_digits.append(second_digit)

        cpf_str = "".join(map(str, base_digits))
        cpf_obj = cls(cpf_str)

        return cpf_obj

    def __str__(self) -> str:
        """String representation returns formatted CPF if valid, otherwise digits."""
        try:
            return self.formatted
        except InvalidCPFError:
            return self._digits

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"CPF('{self._original}')"

    def __eq__(self, other: object) -> bool:
        """Compare CPFs by their digits."""
        if isinstance(other, CPF):
            return self._digits == other._digits
        return False

    def __hash__(self) -> int:
        """Make CPF hashable for use in sets and dicts."""
        return hash(self._digits)
