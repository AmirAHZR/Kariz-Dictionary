def translate(word= str ,origin=list, destination=list):
    """find a word that have a same index in anither list

    Args:
        word (str):
        origin (list): a list that we have the word
        destination (list): a list that we want to find the same indexed word
    Return:
        str: a word with same index in destination list"""
    try:
        n = destination[origin.index(word)]
    except :
        n = ''
    return n
