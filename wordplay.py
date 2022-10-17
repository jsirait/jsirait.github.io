from english_words import english_words_lower_alpha_set as words
import difflib
import random

def generateSimilarWordsDifflib(word, cutoff=0.6):
    '''Returns random words that are similar to the input word, where similar words 
    are defined as words that have minimum Levensteihn distance 
    (or as implemented by difflib using Ratcliff/Obershelp algorithm)'''
    new_word = random.choice(difflib.get_close_matches(word, words, n=5, cutoff=cutoff)[1:])
    # new_word1 = process.extract(word, words, limit=2, scorer=fuzz.token_set_ratio)[1][0]
    return(new_word)


def generateSimilarWordsLCSubseq(word):
    '''Returns words that are similar to the input word, where similar words 
    are defined as words that have the longest common subsequence'''
    new_word = word
    return(new_word)

def generateSimilarWordsLCSubstr(word):
    '''Returns words that are similar to the input word, where similar words 
    are defined as words that have the longest common substring'''
    new_word = word
    return(new_word)

def calculateLCSq(word1, word2):
    '''Returns the total length of the longest common subsequence between the two input words'''
    return 0

def calculateLCSt(word1, word2):
    '''Returns the length of the longest common substring between the two input words'''
    return 0

if __name__ == "__main__":
    # word1, word2 = input("word: ").split()
    freq = 10
    word1 = "software"
    word2 = "developer"
    for _ in range(freq):
        print("{} {}".format(word1, word2))
        word1 = generateSimilarWordsDifflib(word1)
        word2 = generateSimilarWordsDifflib(word2)
