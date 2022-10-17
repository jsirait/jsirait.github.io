from re import T
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


def generateSimilarWordsLCSubseq(target, words, howmany=10):
    '''Returns some number of words that are similar to the input word from the supplied list of words, 
    where similar words are defined as words that have the longest common subsequence, most similar first'''
    lcsq_dict = dict()
    for word in words:
        if word==target: continue
        lcsq_dict[word] = calculateLCSq(target, word)
    similar_words = sorted(lcsq_dict.keys(), key=lambda w:lcsq_dict[w], reverse=True)
    return(similar_words[:howmany])

def generateSimilarWordsLCSubstr(target, words, howmany=10):
    '''Returns some number of words that are similar to the input word from the supplied list of words, 
    where similar words are defined as words that have the longest common substring, most similar first'''
    similar_words = []
    lcst_dict = dict()
    for word in words:
        if word==target: continue
        lcst_dict[word] = calculateLCSt(target, word)
    similar_words = sorted(lcst_dict.keys(), key=lambda w:lcst_dict[w], reverse=True)
    return(similar_words[:howmany])

def calculateLCSq(word1, word2):
    '''Returns the total length of the longest common subsequence between the two input words.\n
    if [same_suffix_or_prefix>0] then lcsq_score is only calculated for words with the same suffix or prefix'''
    memo = [[0 for _ in range(len(word1))] for _ in range(len(word2))]
    lcsq_score = 0
    for ii in range(len(word2)):
        for jj in range(len(word1)):
            if (ii==0 or jj==0):
                memo[ii][jj] = 1 if word1[jj] == word2[ii] else 0
            elif (word1[jj] == word2[ii]):
                memo[ii][jj] = memo[ii-1][jj-1] + 1
            else:
                memo[ii][jj] = max(memo[ii-1][jj], memo[ii][jj-1])
    lcsq_score = memo[-1][-1]
    return lcsq_score

def calculateLCSt(word1, word2):
    '''Returns the length of the longest common substring between the two input words.\n
    if [same_suffix_or_prefix>0] then lcsq_score is only calculated for words with the same suffix or prefix'''
    memo = [[0 for _ in range(len(word1))] for _ in range(len(word2))]
    lcst_score = 0
    for ii in range(len(word2)):
        for jj in range(len(word1)):
            if (ii==0 or jj==0):
                memo[ii][jj] = 1 if word1[jj] == word2[ii] else 0
            elif (word1[jj] == word2[ii]):
                memo[ii][jj] = memo[ii-1][jj-1] + 1
                lcst_score = max(lcst_score, memo[ii][jj])
            else:
                memo[ii][jj] = 0
    return lcst_score

if __name__ == "__main__":
    # word1, word2 = input("word: ").split()
    # freq = 10
    word1 = "software"
    word2 = "developer"
    assert(calculateLCSq("softly", "softwarely")==6)
    assert(calculateLCSt("softly", "softwarely")==4)
    # find words that are most similar to software
    print(word1)
    print("LCSubstring based", generateSimilarWordsLCSubstr(word1, words))
    print("LCSubsequence based", generateSimilarWordsLCSubseq(word1, words))
    # LCSubstring is the best metric to use
    # find words that are most similar to software
    print(word2)
    print("LCSubstring based", generateSimilarWordsLCSubstr(word2, words))
    print("LCSubsequence based", generateSimilarWordsLCSubseq(word2, words))
    # LCSubstring is the best metric to use
    print("***** Code works successfully yay *****")

# next steps:
# * filter the english words so that it will only contain words within max 2 shorter or longer than input word