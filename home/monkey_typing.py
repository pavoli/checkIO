# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

'''
You are given some text potentially including sensible words.
You should count how many words are included in the given text.
A word should be whole and may be a part of other word.
Text letter case does not matter.
Words are given in lowercase and don't repeat.
If a word appears several times in the text, it should be counted only once.
For example, text - "How aresjfhdskfhskd you?", words - ("how", "are", "you", "hello"). The result will be 3.
Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).
Output: The number of words in the text as an integer.
'''
def count_words(text, words):
    count = 0
    for i in words:
        if i in text.lower():
            count += 1
            if  text.lower().count(i) > 1:
                continue
    return count
''''''

'''
def count_words(text, words):
    return sum(w in text.lower() for w in words)
'''

'''
def count_words(text, words):
    return len([word for word in words if text.lower().find(word) >= 0])
'''


if __name__ == "__main__":
    #print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
    print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
    #print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
    #            {"sum", "hamlet", "infinity", "anything"}))