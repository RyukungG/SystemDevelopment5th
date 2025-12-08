"""
Test suite for the Calculator class.
"""

import pytest
import re
from calculator.calculator import Calculator, InvalidInputException

def calc():
    return Calculator()
class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc().add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc().add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc().add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc().add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc().add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc().add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc().add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc().add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc().add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_large_numbers(self):
        """Test adding large numbers."""
        # Arrange
        a = 1000000
        b = 1000000

        # Act
        # Assert    
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().add(a, b)
            
    def test_add_one_number(self):
        """Test adding one number outside valid range."""
        # Arrange
        a = 1

        # Act
        # Assert
        with pytest.raises(TypeError):
            calc().add(a)

    
    def test_add_small_numbers(self):
        """Test adding small numbers."""
        # Arrange
        a = -1000000
        b = -1000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().add(a, b)

    def test_add_large_and_small_numbers(self):
        """Test adding large and small numbers."""
        # Arrange
        a = 1000000000000000
        b = -1000000000000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().add(a, b)
    
    def test_add_zero_and_large_number(self):
        """Test adding zero and a large number."""
        # Arrange
        a = 0
        b = 1000000000000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {b} is outside the valid range (-1000000 to 1000000)")):
            calc().add(a, b)    
    
    def test_million_plus_large(self):
        """Test adding numbers resulting in just above the max limit."""
        # Arrange
        a = 1000000
        b = 100000000000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().add(a, b)

    def test_minus_million_plus_small(self):
        """Test adding numbers resulting in just below the min limit."""
        # Arrange
        a = -1000000
        b = -100000000000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().add(a, b)
    
    def test_add_none_input(self):
        """Test adding None as input."""
        # Arrange
        a = None
        b = 5

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=r"\bInput cannot be None\b"):
            calc().add(a, b)

class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc().subtract(a, b)

        # Assert
        assert result == expected
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc().subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_and_negative(self):
        """Test subtracting negative from positive number."""
        # Arrange
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc().subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_and_positive(self):
        """Test subtracting positive from negative number."""
        # Arrange
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc().subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_with_zero(self):
        """Test subtracting zero from positive number."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc().subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero_with_positive(self):
        """Test subtracting positive number from zero."""
        # Arrange
        a = 0
        b = 5
        expected = -5

        # Act
        result = calc().subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        # Arrange
        a = 5.5
        b = 2.2
        expected = 3.3

        # Act
        result = calc().subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)    
    
    def test_subtract_large_numbers(self):
        """Test subtracting large numbers."""
        # Arrange
        a = 1000000000000000
        b = 500000000000000

        
        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().subtract(a, b)

    def test_subtract_small_numbers(self):
        """Test subtracting small numbers."""
        # Arrange
        a = -1000000000000000
        b = -500000000000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().subtract(a, b)
    
    def test_subtract_large_and_small_numbers(self):
        """Test subtracting small number from large number."""
        # Arrange
        a = 1000000000000000
        b = -500000000000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().subtract(a, b)
    
    def test_subtract_zero_and_large_number(self):
        """Test subtracting large number from zero."""
        # Arrange
        a = 0
        b = 1000000000000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {b} is outside the valid range (-1000000 to 1000000)")):
            calc().subtract(a, b)

class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc().multiply(a, b)

        # Assert
        assert result == expected
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        # Arrange
        a = 5
        b = 0
        expected = 0

        # Act
        result = calc().multiply(a, b)

        # Assert
        assert result == expected
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = 15

        # Act
        result = calc().multiply(a, b)

        # Assert
        assert result == expected
    
    def test_multiply_positive_and_negative(self):
        """Test multiplying positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = -15

        # Act
        result = calc().multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_and_positive(self):
        """Test multiplying negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -15

        # Act
        result = calc().multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        # Arrange
        a = 2.5
        b = 4.0
        expected = 10.0

        # Act
        result = calc().multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_multiply_large_numbers(self):
        """Test multiplying large numbers."""
        # Arrange
        a = 1000000000000000
        b = 1000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().multiply(a, b)

    def test_multiply_small_numbers(self):
        """Test multiplying small numbers."""
        # Arrange
        a = -1000000000000000
        b = 1000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().multiply(a, b)
    
    def test_multiply_large_and_small_numbers(self):
        """Test multiplying large and small numbers."""
        # Arrange
        a = 1000000000000000
        b = -1000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().multiply(a, b)

    def test_multiply_by_large_number(self):
        """Test multiplying by a large number."""
        # Arrange
        a = 5
        b = 1000000000000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {b} is outside the valid range (-1000000 to 1000000)")):
            calc().multiply(a, b)


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # Arrange
        a = 6
        b = 3
        expected = 2

        # Act
        result = calc().divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        # Arrange
        a = -6
        b = -3
        expected = 2

        # Act
        result = calc().divide(a, b)

        # Assert
        assert result == expected
    
    def test_divide_positive_and_negative(self):
        """Test dividing positive by negative number."""
        # Arrange
        a = 6
        b = -3
        expected = -2

        # Act
        result = calc().divide(a, b)

        # Assert
        assert result == expected
    
    def test_divide_negative_and_positive(self):
        """Test dividing negative by positive number."""
        # Arrange
        a = -6
        b = 3
        expected = -2

        # Act
        result = calc().divide(a, b)

        # Assert
        assert result == expected
    
    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        # Arrange
        a = 7.5
        b = 2.5
        expected = 3.0

        # Act
        result = calc().divide(a, b)

        # Assert
        assert result == pytest.approx(expected)
    
    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError."""
        # Arrange
        a = 5
        b = 0

        # Act & Assert
        with pytest.raises(ValueError, match=r"\bCannot divide by zero\b"):
            calc().divide(a, b)
        
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        # Arrange
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc().divide(a, b)

        # Assert
        assert result == expected

    def test_divide_large_numbers(self):
        """Test dividing large numbers."""
        # Arrange
        a = 1000000000000000
        b = 1000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().divide(a, b)

    def test_divide_small_numbers(self):
        """Test dividing small numbers."""
        # Arrange
        a = -1000000000000000
        b = 1000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().divide(a, b)

    def test_divide_large_and_small_numbers(self):
        """Test dividing large number by small number."""
        # Arrange
        a = 1000000000000000
        b = -1000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {a} is outside the valid range (-1000000 to 1000000)")):
            calc().divide(a, b)

    def test_divide_by_large_number(self):
        """Test dividing by a large number."""
        # Arrange
        a = 5
        b = 1000000000000000

        # Act
        # Assert
        with pytest.raises(InvalidInputException, match=re.escape(f"Input {b} is outside the valid range (-1000000 to 1000000)")):
            calc().divide(a, b)


