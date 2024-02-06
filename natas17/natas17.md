<h2>Natas Level 17</h2>
<p>This level allows us to check the existance of a username.</p>
<img src="https://i.imgur.com/KaXPHGc.jpeg"/>
<p>When we enter something like test into the input box, we get a blank response.</p>
<img src="https://i.imgur.com/Bqt1Hi0.jpeg"/>
<p>We can try more inputs such as: natas18 ; " ' etc. but they all give us the same blank input.</p>
<p>This suggets that this may be a fully blind SQL injection, since we're likely dealing with a database.</p>
<p>In situations like this we can use a timing attack.</p>
<p>This is where we can use the response time of the request as a metric to see whether our statement is true or false.</p>
<p>Lets assume that the website is using an SQL database, we can also assume that there is a natas18 user since previous levels had a natas user.</p>
<p>So if we tried an injection attack such as: natas18' AND sleep(5); #, in theory if the natas18 username exists and our attack methodology is correct it should take at least 5 seconds for the server to fetch the response.</p>
<p>If we try that in our browser, the reponse is fetched instantly, so lets try to replace the single quote with a double quote as SQL queries can use either.</p>
<p>Now, we can observe that the response did infact take at least 5 seconds to be fetched.</p>
<p>Now, we have to find a way to manipulate this to find more information.</p>
<p>We can try to use the substring function we've used in one of the previous walk throughs.</p>
<p>We will modify it so that it is true when the username is natas18, the password substring is X and we will tell the server to sleep for 2 seconds.</p>
<p>So, our query will look like: natas18" AND BINARY substring(password,1,1)='a' AND Sleep(2); #</p>
<p>We also used the BINARY function to make the substring case sensitive.</p>
<p>We could now find the password by hand but this would be too time consuming, so we will create a python script.</p>
<p>First, we once again create a basic script to connect to the website:</p>
<img src="https://i.imgur.com/4WSghOt.jpeg"/>
<p>Next, we use the time library to time our request and make sure its working correctly</p>
<img src="https://i.imgur.com/soxYpr1.jpeg"/>
<p>Now, we will use a nested loop to iterate through every index of the password, try every single character and check if the response time is > 2 seconds.</p>
<p>If it is, we will append that character to the final password variable and print it when done.</p>
<img src="https://i.imgur.com/IBsckej.jpeg"/>
<p>Now if we run this program, we should get the password for the next level, which is: 8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq</p>
