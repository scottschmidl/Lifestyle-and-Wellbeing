#this function was used to get the males/females/ages ranges into dictionaries.
#it is no longer being used for the sake of condensed code


def group_to_dict(group):
  
    '''returns dictionary with group as the key and a subset of the
       balance score list as the value'''

    if group == 'Male':

    elif group == 'Female':


    elif group == '20 or less':
        dict_20 = {}
        for a in bal_20.iloc[0:, 0:1]:
            dict_20[a] = balacc_list_20
            return dict_20

    elif group == '21 to 35':
        dict_21 = {}
        for a in bal_21.iloc[0:, 0:1]:
            dict_21[a] = balacc_list_21
            return dict_21

    elif group == '36 to 50':
        dict_36 = {}
        for a in bal_36.iloc[0:, 0:1]:
            dict_36[a] = balacc_list_36
            return dict_36

    elif group == '51 or more':
        dict_51 = {}
        for a in bal_51.iloc[0:, 0:1]:
            dict_51[a] = balacc_list_51
            return dict_51

    return 'not a valid group'

dict_20 = group_to_dict('20 or less')    

dict_21 = group_to_dict('21 to 35')    

dict_36 = group_to_dict('36 to 50')    

dict_51 = group_to_dict('51 or more') 
