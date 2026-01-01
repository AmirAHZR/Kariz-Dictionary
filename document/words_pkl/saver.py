import pickle

def saver(file_location, my_list = list):
    with open(file_location, 'wb') as f:    
        pickle.dump(my_list, f)


