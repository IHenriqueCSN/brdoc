"""Tests for CNPJ validation and utilities."""

import pytest
from brdoc import CNPJ
from brdoc.exceptions import InvalidCNPJError


class TestCNPJValidation:
    """Test CNPJ validation logic."""

    def test_valid_cnpj_formatted(self):
        """Test validation of properly formatted valid CNPJ."""
        cnpj = CNPJ("11.222.333/0001-81")
        assert cnpj.is_valid()

    def test_valid_cnpj_unformatted(self):
        """Test validation of unformatted valid CNPJ."""
        cnpj = CNPJ("11222333000181")
        assert cnpj.is_valid()

    def test_invalid_cnpj_wrong_check_digit(self):
        """Test that CNPJ with wrong check digit is invalid."""
        cnpj = CNPJ("11.222.333/0001-82")
        assert not cnpj.is_valid()

    def test_invalid_cnpj_all_same_digits(self):
        """Test that CNPJ with all same digits is invalid."""
        for digit in range(10):
            cnpj = CNPJ(str(digit) * 14)
            assert not cnpj.is_valid()

    def test_invalid_cnpj_wrong_length(self):
        """Test that CNPJ with wrong length is invalid."""
        cnpj = CNPJ("11.222.333/0001")
        assert not cnpj.is_valid()

    def test_validate_class_method(self):
        """Test the class method validate()."""
        assert CNPJ.validate("11.222.333/0001-81")
        assert not CNPJ.validate("11.222.333/0001-82")

    def test_multiple_valid_cnpjs(self):
        """Test multiple known valid CNPJs."""
        valid_cnpjs = [
            "11.222.333/0001-81",
            "11444777000161",
            "34.028.316/0001-03",
        ]
        for cnpj_str in valid_cnpjs:
            assert CNPJ(cnpj_str).is_valid()


class TestCNPJFormatting:
    """Test CNPJ formatting functionality."""

    def test_formatted_property(self):
        """Test the formatted property."""
        cnpj = CNPJ("11222333000181")
        assert cnpj.formatted == "11.222.333/0001-81"

    def test_digits_property(self):
        """Test the digits property."""
        cnpj = CNPJ("11.222.333/0001-81")
        assert cnpj.digits == "11222333000181"

    def test_formatted_preserves_input(self):
        """Test that formatting works regardless of input format."""
        cnpj1 = CNPJ("11.222.333/0001-81")
        cnpj2 = CNPJ("11222333000181")
        assert cnpj1.formatted == cnpj2.formatted

    def test_formatted_raises_on_invalid_length(self):
        """Test that formatted property raises error on invalid length."""
        cnpj = CNPJ("1122233300")
        with pytest.raises(InvalidCNPJError):
            _ = cnpj.formatted

    def test_str_returns_formatted(self):
        """Test that __str__ returns formatted CNPJ."""
        cnpj = CNPJ("11222333000181")
        assert str(cnpj) == "11.222.333/0001-81"

    def test_repr(self):
        """Test __repr__ method."""
        cnpj = CNPJ("11.222.333/0001-81")
        assert repr(cnpj) == "CNPJ('11.222.333/0001-81')"


class TestCNPJGeneration:
    """Test CNPJ generation functionality."""

    def test_generate_creates_valid_cnpj(self):
        """Test that generated CNPJ is valid."""
        cnpj = CNPJ.generate()
        assert cnpj.is_valid()

    def test_generate_creates_different_cnpjs(self):
        """Test that generate creates different CNPJs."""
        cnpjs = [CNPJ.generate() for _ in range(10)]
        # Check that not all CNPJs are the same
        assert len(set(cnpj.digits for cnpj in cnpjs)) > 1

    def test_generated_cnpj_has_correct_length(self):
        """Test that generated CNPJ has 14 digits."""
        cnpj = CNPJ.generate()
        assert len(cnpj.digits) == 14


class TestCNPJComparison:
    """Test CNPJ comparison and hashing."""

    def test_equality_same_cnpj(self):
        """Test that two CNPJ objects with same number are equal."""
        cnpj1 = CNPJ("11.222.333/0001-81")
        cnpj2 = CNPJ("11222333000181")
        assert cnpj1 == cnpj2

    def test_inequality_different_cnpj(self):
        """Test that two CNPJ objects with different numbers are not equal."""
        cnpj1 = CNPJ("11.222.333/0001-81")
        cnpj2 = CNPJ("34.028.316/0001-03")
        assert cnpj1 != cnpj2

    def test_hashable(self):
        """Test that CNPJ objects can be used in sets and dicts."""
        cnpj1 = CNPJ("11.222.333/0001-81")
        cnpj2 = CNPJ("11222333000181")
        cnpj3 = CNPJ("34.028.316/0001-03")

        cnpj_set = {cnpj1, cnpj2, cnpj3}
        assert len(cnpj_set) == 2  # cnpj1 and cnpj2 are the same

    def test_dict_key(self):
        """Test that CNPJ can be used as dictionary key."""
        cnpj1 = CNPJ("11.222.333/0001-81")
        cnpj2 = CNPJ("11222333000181")

        data = {cnpj1: "Company 1"}
        assert data[cnpj2] == "Company 1"


class TestCNPJEdgeCases:
    """Test edge cases and special scenarios."""

    def test_cnpj_with_spaces(self):
        """Test CNPJ with spaces is cleaned properly."""
        cnpj = CNPJ("11 222 333 0001 81")
        assert cnpj.digits == "11222333000181"
        assert cnpj.is_valid()

    def test_cnpj_with_mixed_formatting(self):
        """Test CNPJ with mixed formatting characters."""
        cnpj = CNPJ("11.222.333-0001-81")
        assert cnpj.digits == "11222333000181"

    def test_empty_string(self):
        """Test empty string CNPJ."""
        cnpj = CNPJ("")
        assert not cnpj.is_valid()

    def test_letters_in_cnpj(self):
        """Test that letters are stripped from CNPJ."""
        cnpj = CNPJ("11ABC222DEF333GHI0001IJK81")
        assert cnpj.digits == "11222333000181"
        assert cnpj.is_valid()
