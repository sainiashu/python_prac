import pytest


def is_even_or_odd(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"

# @pytest.mark.smoke
def test_even_number():
    result = is_even_or_odd(4)
    print(f"Test for 4: {result}")

# @pytest.mark.skip(reason="not ready")
def test_odd_number():
    result = is_even_or_odd(3)
    print(f"Test for 4: {result}")

# @pytest.mark.regression
def test_large_number():
    result = is_even_or_odd(1000000)
    assert result == "Even", "1000000"
#
# def is_even_odd(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "Odd"
#
# def test_even():
#     result = is_even_odd(2)
#     print(f"Test:", {result})