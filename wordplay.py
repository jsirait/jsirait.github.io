from english_words import english_words_lower_alpha_set as words
import difflib
import random
from thefuzz import process, fuzz

def generateSimilarWordsLevensteihn(word, cutoff=0.6):
    '''Prints words that are similar to the input word, where similar words 
    are defined as words that have minimum Levensteihn distance'''
    new_word1 = random.choice(difflib.get_close_matches(word, words, n=5, cutoff=cutoff)[1:])
    # new_word1 = process.extract(word, words, limit=2, scorer=fuzz.token_set_ratio)[1][0]
    return(new_word1)


if __name__ == "__main__":
    # word1, word2 = input("word: ").split()
    freq = 10
    word1 = "software"
    word2 = "developer"
    for _ in range(freq):
        print("{} {}".format(word1, word2))
        word1 = generateSimilarWordsLevensteihn(word1)
        word2 = generateSimilarWordsLevensteihn(word2)
