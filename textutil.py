"""Tiny text helpers for the firstmate executor lab."""


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def char_count(text: str, *, include_spaces: bool = True) -> int:
    """Return the number of characters in text.

    By default every character is counted. When include_spaces is False,
    whitespace characters are excluded.
    """
    if include_spaces:
        return len(text)
    return sum(1 for char in text if not char.isspace())
