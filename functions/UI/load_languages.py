def load_languages(list_of_langueges = list):
    '''This function, get a list and return
        all condition that you can make with that.
    Args:
        lsit_of_langueges (list)
    Return:
        list: a list from Args * 2 
            from list with 2 objects
    Example:
        >>>load_languages([farsi, english])
        [[farsi, english], [english, farsi]]
    '''
    list_all_conditions = list()

    for index, object in  enumerate(list_of_langueges):
        my_pop = list_of_langueges.pop(index)
 
        for other in list_of_langueges:
            list_all_conditions.append([object, other])



        list_of_langueges.insert(index, my_pop)

    return list_all_conditions
