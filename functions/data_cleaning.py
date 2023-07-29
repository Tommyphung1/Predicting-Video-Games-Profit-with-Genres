def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000
    return 0.0

def convert_to_list(x):
    new_list = x.strip('\'[ ]').split('\', \'')
    return new_list

def count_values(list_to_count):
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