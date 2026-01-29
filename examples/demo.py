#!/usr/bin/env python3
"""
Example usage of the brdoc library.

This script demonstrates the main features of the library.
"""

from brdoc import CPF, CNPJ


def demonstrate_cpf():
    """Demonstrate CPF functionality."""
    print("=" * 60)
    print("CPF Examples")
    print("=" * 60)

    # Validate existing CPF
    print("\n1. Validating CPFs:")
    valid_cpf = CPF("111.444.777-35")
    print(f"   CPF: {valid_cpf} -> Valid: {valid_cpf.is_valid()}")

    invalid_cpf = CPF("111.444.777-36")
    print(f"   CPF: {invalid_cpf} -> Valid: {invalid_cpf.is_valid()}")

    # Format CPF
    print("\n2. Formatting CPF:")
    unformatted = CPF("11144477735")
    print(f"   Input: {unformatted.digits}")
    print(f"   Formatted: {unformatted.formatted}")

    # Generate CPF
    print("\n3. Generating random valid CPFs:")
    for i in range(3):
        new_cpf = CPF.generate()
        print(f"   CPF #{i+1}: {new_cpf.formatted} -> Valid: {new_cpf.is_valid()}")

    # Use in collections
    print("\n4. Using CPFs in sets (deduplication):")
    cpf_set = {
        CPF("111.444.777-35"),
        CPF("11144477735"),  # Same as above
        CPF("231.002.999-00"),
    }
    print(f"   Unique CPFs: {len(cpf_set)}")
    for cpf in cpf_set:
        print(f"   - {cpf}")


def demonstrate_cnpj():
    """Demonstrate CNPJ functionality."""
    print("\n" + "=" * 60)
    print("CNPJ Examples")
    print("=" * 60)

    # Validate existing CNPJ
    print("\n1. Validating CNPJs:")
    valid_cnpj = CNPJ("11.222.333/0001-81")
    print(f"   CNPJ: {valid_cnpj} -> Valid: {valid_cnpj.is_valid()}")

    invalid_cnpj = CNPJ("11.222.333/0001-82")
    print(f"   CNPJ: {invalid_cnpj} -> Valid: {invalid_cnpj.is_valid()}")

    # Format CNPJ
    print("\n2. Formatting CNPJ:")
    unformatted = CNPJ("11222333000181")
    print(f"   Input: {unformatted.digits}")
    print(f"   Formatted: {unformatted.formatted}")

    # Generate CNPJ
    print("\n3. Generating random valid CNPJs:")
    for i in range(3):
        new_cnpj = CNPJ.generate()
        print(f"   CNPJ #{i+1}: {new_cnpj.formatted} -> Valid: {new_cnpj.is_valid()}")

    # Use as dictionary keys
    print("\n4. Using CNPJs as dictionary keys:")
    companies = {
        CNPJ("11.222.333/0001-81"): "Acme Corporation",
        CNPJ("34.028.316/0001-03"): "Tech Solutions Ltd",
    }
    for cnpj, name in companies.items():
        print(f"   {cnpj}: {name}")


def main():
    """Run all demonstrations."""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 15 + "BRDOC Library Demo" + " " * 25 + "║")
    print("║" + " " * 12 + "Brazilian Document Validator" + " " * 18 + "║")
    print("╚" + "═" * 58 + "╝")

    demonstrate_cpf()
    demonstrate_cnpj()

    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
