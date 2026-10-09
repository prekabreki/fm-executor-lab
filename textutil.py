"""Tiny text helpers for the firstmate executor lab."""


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())
