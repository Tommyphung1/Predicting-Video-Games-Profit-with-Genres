def value_to_float(x):
    '''
    Input: x - string value with or without a K
    Output: x, 1000 or 0.0 based off the result of the string.
    
    Strings have a K and needed to be converted to the correct value. K stands for 1000. 
    '''
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000
    return 0.0

def convert_to_list(x):
    '''
    Simple Function that split a string into lists with the given special character. 
    '''
    new_list = x.strip('\'[ ]').split('\', \'')
    return new_list

def count_values(list_to_count):
    '''
    Input: List_to_count (list)
    Output: 
    Create a dictionary of counted objects and return them sorted from greatest to fewest
    '''
    split_genres = {}
    for group in list_to_count:
        for element in group:
            if element == '':
                break
            key = element
            if split_genres.get(key) == None:
                split_genres[key] = 1 
            else:
                split_genres[key] += 1
    sort_genres = dict(sorted(split_genres.items(), key = lambda x: x[1], reverse= False))
    return sort_genres

def convert_feature(clf):
    '''
    Input: clf (classifier) 
    Output: list of name and importance for the model given.
    Take the classifier and create a list of the feature importance and return them sorted
    '''
    feature_list = []
    for name, value in zip(clf.feature_names_in_, clf.feature_importances_):
        feature_list.append((name, round(value*100, 2)))
    feature_list = sorted(feature_list, key= lambda x: x[1])
    return feature_list