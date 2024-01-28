<h2>Natas Level 15</h2>
<p>This level checks for the existance of a username.</p>
<img src="https://i.imgur.com/V9cezBY.jpg"/>
<p>It allows us to enter a username and tells us that the user doesn't exist if it doesnt match.</p>
<p>We can try inputting common characters used for SQL injection such as: ; ' " etc.</p>
<p>When we enter a " (double quote) character, we get an error:</p>
<img src="https://i.imgur.com/MVfQWpo.jpg"/>
<p>This means that the character is causing some type of error. The code possibly suffers from the same vulnerability as the previous level.</p>
<p>So, lets try the same input we used to find the previous password, which is: " OR 1=1 #</p>
<img src="https://i.imgur.com/0yxXObc.jpg"/>
<p>The web page tells us that this user exists.</p>
<p>This means that the SQL query is likely just used to give a true/false value to an if statement.</p>
<p>Therefore, this might be a blind SQL injection, think of it as asking the computer a question and it responds only with yes or no.</p>
<p>We might be able to crack the password through a series of these yes/no questions.</p>
<p>Essentially, we want to brute force the password, but first we need a username to match it with.</p>
<p>We can try common usernames, which in this case would be natas, natas16 etc.</p>
<p>When we enter the username "natas16" we can see that this use exists.</p>
<p>But now, we need to crack the password of this user.</p>
<p>SQL has a function called substring that returns the value of a specified index in a string.</p>
<p>We can use this function to guess each character of the password 1 by 1.</p>
<p>To do this we will need to modify the SQL query to be: ... WHERE username="natas16" AND SUBSTRING(password, 1, 1)="X".</p>
<p>Where X is a placeholder for a character.</p>
<p>So our input would be: natas16" AND SUBSTRING(password, 1, 1)="X" #.</p>
<p>This will modify the SQL query so that it will return "This user exists" if the 1st index of the password matches X.</p>
<p>We could do this process manually for every character, however it would be very time consuming.</p>
<p>Therefore, we will automate this process with Python.</p>
<p>We will make use of the "requests" python library to make HTTP requests.</p>
<p>Then we will first make a basic script to connect to the website and login, as such:</p>
<img src="https://i.imgur.com/DEouYAH.jpg"/>
<p>If done correctly, the program should return the response.</p>
<p>Now, we need to modify our code so it can input data for us, we need to add a "params" parameter to our GET request.</p>
<p>Then we need to pass the form name and desired input into the parameter as such:</p>
<img src="https://i.imgur.com/dR5y93i.jpg"/>
<p>If done correctly, the response should tell us if the user exists or not.</p>
<p>Now that we have the base function of the program working, we can start to brute force the password.</p>
<p>From previous levels, we know that the password is 32 characters long.</p>
<p>We will create a blank string variable to hold the final password, next we will create a string variable containing all the possible characters.</p>
<p>Next, we will create a nested loop, to iterate over every character 32 times.</p>
<p>We will also declare a variable for our query inside of the nested loop as it will change every time.</p>
<p>Then we want to check if the length of the reponse is 913, as thats how long it is when a user exists.</p>
<p>Then if a character matches we want to append it to the final password variable, our code should look somewhat like this:</p>
<img src="https://i.imgur.com/NAgsB6J.jpg"/>
<p>And if we run our code, we should eventually get the password, which is: TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V.</p>
