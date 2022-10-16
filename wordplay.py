from english_words import english_words_lower_alpha_set as words
import difflib
import random
from thefuzz import process, fuzz

def generateSimilarWord(word1, word2, freq, cutoff=0.6):
    for _ in range(1):
        # find similar word in the English language
        # new_word1 = random.choice(difflib.get_close_matches(word1, words, n=5, cutoff=cutoff)[1:])
        # new_word2 = random.choice(difflib.get_close_matches(word2, words, n=5, cutoff=cutoff)[1:])
        new_word1 = process.extract(word1, words, limit=2, scorer=fuzz.token_sort_ratio)
        new_word2 = process.extract(word2, words, limit=2, scorer=fuzz.token_sort_ratio)
        print("{} {}".format(new_word1, new_word2))
        word1 = new_word1
        word2 = new_word2


if __name__ == "__main__":
    # theword = input("word: ").split()
    # theword = "software engineer".split()
    generateSimilarWord("software", "engineer", 10)