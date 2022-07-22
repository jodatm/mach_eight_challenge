#from curses import raw
from gettext import find
import pandas as pd
from urllib.request import urlopen
import json

# Load the json from the webpage
response = urlopen("https://mach-eight.uc.r.appspot.com")
json_data = response.read().decode('utf-8', 'replace')
json_data = json.loads(json_data)

data = pd.json_normalize(json_data['values'])
data = data.fillna("NA")

# The column h_in is transformed to int to operate with it
data['h_in'] = pd.to_numeric(data['h_in'], errors = 'coerce')


def find_pairs(num: int)->None:
    '''
    Print all pairs of players whose height adds up to an integer input 

            Parameters:
                    num (int): An integer corresponding to the sum of heights
            Returns:
                    None.
    '''
    raw_values = data.values    
    hash_dic = {}    
    index_h_in = data.columns.get_loc("h_in")    
    index_first_name = data.columns.get_loc("first_name")
    index_last_name = data.columns.get_loc("last_name")    
    not_found_cople = True
        
    for i in range(raw_values.shape[0]): # Loop to populate the hash dictionary
        if raw_values[i][index_h_in] in hash_dic:            
            hash_dic[raw_values[i][index_h_in]].append(i)
        else:
            hash_dic[raw_values[i][index_h_in]] = [i]
    
    for i in range(raw_values.shape[0]):
        difference = num-raw_values[i][index_h_in] # The difference between the num parameter and the h_in per player is stored        
        if difference in hash_dic:                        
            players_match = hash_dic[difference]
            for k in players_match:
                if i < k: #This validation is made to ensure order
                    not_found_cople = False 
                    print("- {player1:<25s}{player2}".format(
                        player1 = raw_values[i][index_first_name] + " " + raw_values[i][index_last_name],                         
                        player2 = raw_values[k][index_first_name] + " " + raw_values[k][index_last_name],
                        ))                                            
    if not_found_cople:
        print("No matches found")
