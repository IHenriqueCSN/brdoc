"""Tests for CPF validation and utilities."""

import pytest
from brdoc import CPF
from brdoc.exceptions import InvalidCPFError


class TestCPFValidation:
    """Test CPF validation logic."""
    
    def test_valid_cpf_formatted(self):
        """Test validation of properly formatted valid CPF."""
        cpf = CPF("111.444.777-35")
        assert cpf.is_valid()
    
    def test_valid_cpf_unformatted(self):
        """Test validation of unformatted valid CPF."""
        cpf = CPF("11144477735")
        assert cpf.is_valid()
    
    def test_invalid_cpf_wrong_check_digit(self):
        """Test that CPF with wrong check digit is invalid."""
        cpf = CPF("111.444.777-36")
        assert not cpf.is_valid()
    
    def test_invalid_cpf_all_same_digits(self):
        """Test that CPF with all same digits is invalid."""
        for digit in range(10):
            cpf = CPF(str(digit) * 11)
            assert not cpf.is_valid()
    
    def test_invalid_cpf_wrong_length(self):
        """Test that CPF with wrong length is invalid."""
        cpf = CPF("123.456.789")
        assert not cpf.is_valid()
    
    def test_validate_class_method(self):
        """Test the class method validate()."""
        assert CPF.validate("111.444.777-35")
        assert not CPF.validate("111.444.777-36")
    
    def test_multiple_valid_cpfs(self):
        """Test multiple known valid CPFs."""
        valid_cpfs = [
            "111.444.777-35",
            "11144477735",
            "231.002.999-00",
        ]
        for cpf_str in valid_cpfs:
            assert CPF(cpf_str).is_valid()


class TestCPFFormatting:
    """Test CPF formatting functionality."""
    
    def test_formatted_property(self):
        """Test the formatted property."""
        cpf = CPF("11144477735")
        assert cpf.formatted == "111.444.777-35"
    
    def test_digits_property(self):
        """Test the digits property."""
        cpf = CPF("111.444.777-35")
        assert cpf.digits == "11144477735"
    
    def test_formatted_preserves_input(self):
        """Test that formatting works regardless of input format."""
        cpf1 = CPF("111.444.777-35")
        cpf2 = CPF("11144477735")
        assert cpf1.formatted == cpf2.formatted
    
    def test_formatted_raises_on_invalid_length(self):
        """Test that formatted property raises error on invalid length."""
        cpf = CPF("123456789")
        with pytest.raises(InvalidCPFError):
            _ = cpf.formatted
    
    def test_str_returns_formatted(self):
        """Test that __str__ returns formatted CPF."""
        cpf = CPF("11144477735")
        assert str(cpf) == "111.444.777-35"
    
    def test_repr(self):
        """Test __repr__ method."""
        cpf = CPF("111.444.777-35")
        assert repr(cpf) == "CPF('111.444.777-35')"


class TestCPFGeneration:
    """Test CPF generation functionality."""
    
    def test_generate_creates_valid_cpf(self):
        """Test that generated CPF is valid."""
        cpf = CPF.generate()
        assert cpf.is_valid()
    
    def test_generate_creates_different_cpfs(self):
        """Test that generate creates different CPFs."""
        cpfs = [CPF.generate() for _ in range(10)]
        # Check that not all CPFs are the same
        assert len(set(cpf.digits for cpf in cpfs)) > 1
    
    def test_generated_cpf_has_correct_length(self):
        """Test that generated CPF has 11 digits."""
        cpf = CPF.generate()
        assert len(cpf.digits) == 11


class TestCPFComparison:
    """Test CPF comparison and hashing."""
    
    def test_equality_same_cpf(self):
        """Test that two CPF objects with same number are equal."""
        cpf1 = CPF("111.444.777-35")
        cpf2 = CPF("11144477735")
        assert cpf1 == cpf2
    
    def test_inequality_different_cpf(self):
        """Test that two CPF objects with different numbers are not equal."""
        cpf1 = CPF("111.444.777-35")
        cpf2 = CPF("231.002.999-00")
        assert cpf1 != cpf2
    
    def test_hashable(self):
        """Test that CPF objects can be used in sets and dicts."""
        cpf1 = CPF("111.444.777-35")
        cpf2 = CPF("11144477735")
        cpf3 = CPF("231.002.999-00")
        
        cpf_set = {cpf1, cpf2, cpf3}
        assert len(cpf_set) == 2  # cpf1 and cpf2 are the same
    
    def test_dict_key(self):
        """Test that CPF can be used as dictionary key."""
        cpf1 = CPF("111.444.777-35")
        cpf2 = CPF("11144477735")
        
        data = {cpf1: "Person 1"}
        assert data[cpf2] == "Person 1"


class TestCPFEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_cpf_with_spaces(self):
        """Test CPF with spaces is cleaned properly."""
        cpf = CPF("111 444 777 35")
        assert cpf.digits == "11144477735"
        assert cpf.is_valid()
    
    def test_cpf_with_mixed_formatting(self):
        """Test CPF with mixed formatting characters."""
        cpf = CPF("111.444.777/35")
        assert cpf.digits == "11144477735"
    
    def test_empty_string(self):
        """Test empty string CPF."""
        cpf = CPF("")
        assert not cpf.is_valid()
    
    def test_letters_in_cpf(self):
        """Test that letters are stripped from CPF."""
        cpf = CPF("111ABC444DEF777GHI35")
        assert cpf.digits == "11144477735"
        assert cpf.is_valid()