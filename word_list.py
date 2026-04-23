"""Read this first."""

from typing import List, Set


class WordList:
    def __init__(self, words: List[str]) -> None:
        self._words: List[str] = []
        self._word_set: Set[str] = set()

        for word in words:
            if self.is_valid_word(word) and word not in self._word_set:
                self._words.append(word)
                self._word_set.add(word)

    def is_valid_word(self, word: str) -> bool:
        if ' ' in word:
            return False
        return True

    def get_words(self) -> List[str]:
        return self._words.copy()

    def get_word_set(self) -> Set[str]:
        return self._word_set.copy()

    def contains_as_substring(self, container: str, contained: str) -> bool:
        if len(contained) <= len(container):
            return contained in container
        return False

    def word_count(self) -> int:
        return len(self._words)
