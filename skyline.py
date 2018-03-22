# Define a function that takes a string
# Returns a matching string where every even letter is upper case and odd letter is lower case
# First letter of the output is lower case

# One Way 
def skyline(string):
    new_string = string[0].lower()
    #new_string = ''
    initial_count = 1
    for f in range(1,len(string)):
        if initial_count % 2 == 0:
            new_string = new_string + string[f].lower()
        else:
            new_string = new_string + string[f].upper()
        initial_count += 1
    return new_string

# Second Way
def new_skyline(string):
    #new_string = string[0].lower()
    new_string = ''
    initial_count = 0
    for f in range(0,len(string)):
        if initial_count % 2 == 0:
            new_string = new_string + string[f].lower()
        else:
            new_string = new_string + string[f].upper()
        initial_count += 1
    return new_string

skyline('UjalakumarPanda')