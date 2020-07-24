'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    word_length = len(word)
    count = 0
    
    if word_length == 0 or word_length == 1:
      return count
    elif word[0] == 't' and word[1] == 'h':
      return 1 + count_th(word[1:])
    else:
      return count_th(word[1:])
