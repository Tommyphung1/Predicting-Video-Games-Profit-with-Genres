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