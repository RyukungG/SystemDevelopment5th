"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""

    MAX_VALUE = 1000000
    MIN_VALUE = -1000000

    def _validate(self, values):
        for value in values:
            if value is None:
                raise InvalidInputException("Input cannot be None")
            if (
                (self.MIN_VALUE >= value)
                or (value >= self.MAX_VALUE)
                or (not isinstance(value, (int, float)))
            ):
                raise InvalidInputException(
                    f"Input {value} is outside the valid range "
                    f"({self.MIN_VALUE} to {self.MAX_VALUE})"
                )


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    def __init__(self):
        self._validate = InvalidInputException()._validate

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate([a, b])
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate([a, b])
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate([a, b])
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self._validate([a, b])
        return a / b
