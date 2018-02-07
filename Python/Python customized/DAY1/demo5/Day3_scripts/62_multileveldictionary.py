import itertools
import copy


def dict_2_list_of_keys(d, l, loc):
    """ Return a list containing lists describing the dictionary nodes' paths

    dict_2_list_of_keys({'k1': 'v1', 'k2': {'k21': 'v21', 'k22': 'v22'}})
    [['k1'], ['k2', 'k21'], ['k2', 'k22']]
    """
    for k in iter(d):
        loc.append(k)
        l.append(loc * 1)
        if isinstance(d[k], dict):
            dict_2_list_of_keys(d[k], l, loc)
        loc.pop()
    return l


def list_of_keys_2_dict_less_sweep(orig_d, swept_key):
    """ Reduce a SINGLE '_sweep' parameter

    list_of_keys_2_dict_less_sweep({'k1_sweep': ['v1a', 'v1b'] ,
                                        'k2': {'k21_sweep': ['v21a', 'v21b'],
                                               'k22': 'v22'}}, 'k1_sweep')
    [{'k1': 'v1a' ,'k2': {'k21_sweep': ['v21a', 'v21b'],'k22': 'v22'}},
     {'k1': 'v1b' ,'k2': {'k21_sweep': ['v21a', 'v21b'],'k22': 'v22'}}]
    """
    #TODO: assert swept_key has a list as value
    swept_key_values = nested_get(orig_d, swept_key)
    new_dictionaries = []
    for i in range(len(swept_key_values)):
        new_dictionaries.append(copy.deepcopy(orig_d))
        nested_set(new_dictionaries[-1], swept_key, swept_key_values[i])
        new_dictionaries[-1] = nested_rename(new_dictionaries[-1], swept_key, swept_key[-1].replace('_sweep', ''))
    return new_dictionaries


def find_swept_key(l):
    """ Look for first parameter, whose leaf-layer name ends with '_sweep'

    [['k1'], ['k2', 'k21_sweep'], ['k2_sweep', 'k22']]
    ['k2', 'k21_sweep']
    """
    try:
        return list(itertools.dropwhile(lambda x: "_sweep" not in x[-1], l))[0]
    except:
        return None


def nested_set(dic, keys, value):
    """ Set the pair (keys[-1], value) nested in dic, according to the path depicted by keys[:-1]

    # http://stackoverflow.com/questions/13687924/setting-a-value-in-a-nested-python-dictionary-given-a-list-of-indices-and-value

    nested_set({'k1': 'v1', 'k2': {'k21': 'v21', 'k22': 'v22'}}, ['k2', 'k21'], 'v21b')
    {'k1': 'v1', 'k2': {'k21': 'v21b', 'k22': 'v22'}}
    nested_set({'k1': 'v1', 'k2': {'k21': 'v21', 'k22': 'v22'}}, ['k2', 'k23'], 'v23')
    {'k1': 'v1', 'k2': {'k21': 'v21', 'k22': 'v22', 'k23': 'v23'}}
    """
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def nested_get(dic, keys):
    """ Get the value from a nested key in dic, according to the path depicted by keys

    # http://stackoverflow.com/questions/14692690/access-python-nested-dictionary-items-via-a-list-of-keys

    nested_get({'k1': 'v1', 'k2': {'k21': 'v21', 'k22': 'v22'}}, ['k2', 'k21'])
    'v21'
    """
    return reduce(lambda d, k: d[k], keys, dic)


def nested_rename(dic, keys, new_key):
    """ Rename the key name of a nested pair of dic

    nested_rename({'k1': 'v1', 'k2': {'k21': 'v21', 'k22': 'v22'}}, ['k2', 'k21'], 'k21_new')
    {'k1': 'v1', 'k2': {'k21_new': 'v21', 'k22': 'v22'}}
    """
    if len(keys) == 1:
        dic[new_key] = dic.pop(keys[0])
        return dic
    else:
        dic[keys[0]] = nested_rename(dic[keys[0]], keys[1:], new_key)
        return dic


def detonate_sweeps(d):
    """ Iteratively pop dictionaries with swept keys and replace it with corresponding dictionaries without the swept key

    new_d = detonate_sweeps({'k1_sweep': ['v1a', 'v1b'] ,'k2': {'k21_sweep': ['v21a', 'v21b'], 'k22': 'v22'}})
    new_d = [{'k1': 'v1a' ,'k2': {'k21': 'v21a', 'k22': 'v22'}},
             {'k1': 'v1a' ,'k2': {'k21': 'v21b', 'k22': 'v22'}},
             {'k1': 'v1b' ,'k2': {'k21': 'v21a', 'k22': 'v22'}},
             {'k1': 'v1b' ,'k2': {'k21': 'v21b', 'k22': 'v22'}}]
    """
    new_dictionaries = [d]
    l = dict_2_list_of_keys(d, [], [])
    swept_key = find_swept_key(l)
    while swept_key:
        new_dictionaries = list_of_keys_2_dict_less_sweep(new_dictionaries[-1], swept_key) + new_dictionaries[:-1]
        l = dict_2_list_of_keys(new_dictionaries[-1], [], [])
        swept_key = find_swept_key(l)
    return new_dictionaries


def main():
    d = {'k1': {'k11': 'v11',
                'k12_sweep': ['v12a', 'v12b', 'v12c'],
                'k13': 'v13'},
         'k2_sweep': ['v2a', 'v2b', 'v2c'],
         'k3': 'v3'}
    res = detonate_sweeps(d)


if __name__ == '__main__':
    main()