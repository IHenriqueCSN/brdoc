"""CNPJ (Cadastro Nacional da Pessoa Jurídica) validation and utilities."""

import re
import random
from typing import Optional
from .exceptions import InvalidCNPJError


class CNPJ:
    """
    CNPJ validator, formatter, and generator.

    CNPJ (Cadastro Nacional da Pessoa Jurídica) is the Brazilian tax identification
    number for companies. It consists of 14 digits with a specific validation algorithm.

    Examples:
        >>> cnpj = CNPJ("11.222.333/0001-81")
        >>> cnpj.is_valid()
        True
        >>> cnpj.formatted
        '11.222.333/0001-81'
        >>> cnpj.digits
        '11222333000181'

        >>> CNPJ.validate("11.222.333/0001-81")
        True

        >>> new_cnpj = CNPJ.generate()
        >>> new_cnpj.is_valid()
        True
    """

    def __init__(self, cnpj: str):
        """
        Initialize a CNPJ instance.

        Args:
            cnpj: CNPJ string with or without formatting (dots, slash, and dash)
        """
        self._original = cnpj
        self._digits = self._clean(cnpj)

    @staticmethod
    def _clean(cnpj: str) -> str:
        """Remove all non-digit characters from CNPJ string."""
        return re.sub(r"\D", "", cnpj)

    @property
    def digits(self) -> str:
        """Get CNPJ as plain digits string."""
        return self._digits

    @property
    def formatted(self) -> str:
        """
        Get CNPJ formatted (XX.XXX.XXX/XXXX-XX).

        Returns:
            Formatted CNPJ string

        Raises:
            InvalidCNPJError: If CNPJ doesn't have exactly 14 digits
        """
        if len(self._digits) != 14:
            raise InvalidCNPJError(f"CNPJ must have 14 digits, got {len(self._digits)}")

        return f"{self._digits[:2]}.{self._digits[2:5]}.{self._digits[5:8]}/{self._digits[8:12]}-{self._digits[12:]}"

    def is_valid(self) -> bool:
        """
        Check if the CNPJ is valid.

        A valid CNPJ must:
        - Have exactly 14 digits
        - Not be a known invalid sequence (all same digits)
        - Pass the check digit algorithm

        Returns:
            True if valid, False otherwise
        """
        # Must have 14 digits
        if len(self._digits) != 14:
            return False

        # Cannot be all same digits (known invalid CNPJs)
        if self._digits == self._digits[0] * 14:
            return False

        # Validate check digits
        return self._validate_check_digits()

    def _validate_check_digits(self) -> bool:
        """Validate the two check digits using CNPJ algorithm."""
        # First check digit
        weights_first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum_first = sum(int(self._digits[i]) * weights_first[i] for i in range(12))
        first_digit = sum_first % 11
        first_digit = 0 if first_digit < 2 else 11 - first_digit

        if int(self._digits[12]) != first_digit:
            return False

        # Second check digit
        weights_second = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum_second = sum(int(self._digits[i]) * weights_second[i] for i in range(13))
        second_digit = sum_second % 11
        second_digit = 0 if second_digit < 2 else 11 - second_digit

        return int(self._digits[13]) == second_digit

    @classmethod
    def validate(cls, cnpj: str) -> bool:
        """
        Class method to quickly validate a CNPJ string.

        Args:
            cnpj: CNPJ string to validate

        Returns:
            True if valid, False otherwise

        Example:
            >>> CNPJ.validate("11.222.333/0001-81")
            True
        """
        return cls(cnpj).is_valid()

    @classmethod
    def generate(cls, formatted: bool = False) -> "CNPJ":
        """
        Generate a valid random CNPJ.

        Args:
            formatted: If True, return formatted CNPJ; otherwise plain digits

        Returns:
            A new CNPJ instance with a valid random CNPJ

        Example:
            >>> cnpj = CNPJ.generate()
            >>> cnpj.is_valid()
            True
        """
        # Generate first 12 digits randomly
        base_digits = [random.randint(0, 9) for _ in range(12)]

        # Calculate first check digit
        weights_first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum_first = sum(base_digits[i] * weights_first[i] for i in range(12))
        first_digit = sum_first % 11
        first_digit = 0 if first_digit < 2 else 11 - first_digit
        base_digits.append(first_digit)

        # Calculate second check digit
        weights_second = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum_second = sum(base_digits[i] * weights_second[i] for i in range(13))
        second_digit = sum_second % 11
        second_digit = 0 if second_digit < 2 else 11 - second_digit
        base_digits.append(second_digit)

        cnpj_str = "".join(map(str, base_digits))
        cnpj_obj = cls(cnpj_str)

        return cnpj_obj

    def __str__(self) -> str:
        """String representation returns formatted CNPJ if valid, otherwise digits."""
        try:
            return self.formatted
        except InvalidCNPJError:
            return self._digits

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"CNPJ('{self._original}')"

    def __eq__(self, other: object) -> bool:
        """Compare CNPJs by their digits."""
        if isinstance(other, CNPJ):
            return self._digits == other._digits
        return False

    def __hash__(self) -> int:
        """Make CNPJ hashable for use in sets and dicts."""
        return hash(self._digits)
