def store_user_info(username:String, password:String): 
    '''
    This function takes in a username and password as a string, checks if it is in the database, if it is then a new username is required, 
    otherwise the users details will be added to the database
    '''
    username=str(username)
    password=str(password)
    database={'sarah': 'dolphins','tom':'puppies'}
    if username in database:
        print ('Username already exists, please try again')
    else:
        database.update({username : password})
        print ('Details updated')
    return database
  
def check_user_info(username: String, password:String):
    '''
    Checks if the username and password a user has entered matches with the details in the database
    '''
    
    database={'sarah': 'dolphins','tom':'puppies'}
    if (username, password) in database.items():
        True
    else: 
        False
    return 
    
