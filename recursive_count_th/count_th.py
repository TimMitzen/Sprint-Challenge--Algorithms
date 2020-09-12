'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if not word:# if not a word
        return 0

    if word[:2] == 'th': #for the th case slicing start at 0 index and end at index 2
        return 1 + count_th(word[1:])#reclusive slicing starts at 1 and goes to the end

    else:
        return count_th(word[1:]) #for all other cases, reclusive, slicing starts at 1 index to the end

