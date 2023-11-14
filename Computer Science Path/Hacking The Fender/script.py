import csv
import os
import json
working_directory = os.getcwd()
project = "Computer Science Path/Hacking The Fender"

filePath = os.path.join(working_directory, project, 'passwords.csv')
password_file = open(filePath)

compromised_users = []

# Read the csv file and store all the usernames in a list
password_csv = csv.DictReader(password_file)
for password in password_csv:
    password_row = password
    # print(password_row['Username'])
    compromised_users.append(password_row['Username'])


# Write usernames of compromised users
usersFilePath = filePath = os.path.join(
    working_directory, project, 'compromised_users.txt')
with open(usersFilePath, 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(f"{user}\n")


# Notify the boss
bossFile = os.path.join(
    working_directory, project, 'boss_message.json')

with open(bossFile, 'w') as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Sucess"}
    json.dump(boss_message_dict, boss_message)

# Scrambling the password
newPasswords = os.path.join(
    working_directory, project, 'new_passwords.csv')


slash_null_sig = """ _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \\
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

with open(newPasswords, 'w') as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)
