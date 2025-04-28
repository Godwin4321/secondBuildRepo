# tests/test_example.py

def test_example():
  assert 1 + 1 == 2

# assert is a keyword in Python used for testing whether a condition is True.
# If the condition after assert is True, Python does nothing and moves on.
# If the condition is False, Python will raise an AssertionError and stop the program (or fail the test).

# Why use assert in tests?
# When you run tests using pytest, it looks for assert statements.
# If all asserts pass ➔ test passes.
# If any assert fails ➔ test fails ❌ and you get an error message.
