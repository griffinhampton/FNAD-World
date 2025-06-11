import os
import src.dependancyStuff.passwordStuff.passwordConfig as passwordConfig



def password(username, password):
    file_path = os.path.join(os.path.dirname(__file__), "passwordHolder.txt")
    f = open(file_path, "r+")
    found = False
    returnMessage = ""
    userInput = username.lower() +" "+ password
    for line in f:
        if userInput in line:
            returnMessage = passwordConfig.USERFOUND
            return returnMessage

    f.write(userInput + " \n")
    returnMessage = passwordConfig.USERADDED
    return returnMessage



