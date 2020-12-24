import json

def store_user_info(username, password): 
 
    '''
    This function takes in a username and password as a string, checks if it is in the database, if it is then a new username is required, 
    otherwise the users details will be added to the database
    '''
    username=str(username)
    password=str(password)
    
    database={'sarah': 'dolphins','tom':'puppies'}
    
    # convert from dictionary to json - serialization
    
    json_file = json.dumps(database, indent = 4) 
    
    if username in json_file:
        return False
    else:
        new_data = {username: password} 
        parse_json = json.loads(json_file) 
        
        # appending the data 
        parse_json.update(new_data) 
        return True
    
   
def check_user_info(username, password):
    '''
    Checks if the username and password a user has entered matches with the details in the database
    '''
    
    database={'sarah': 'dolphins','tom':'puppies'}
    
    json_file = json.dumps(database, indent = 4) 
    
    
    if username in json_file:
        if password in json_file:
            return True
    else: 
        return False

    
