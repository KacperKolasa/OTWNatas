<h2>Natas Level 14</h2>
<p>This level gives us a username and password box.</p>
<img src="https://i.imgur.com/sHvk8Vz.jpg"/>
<p>Therefore the web server is likely using a database to store usernames and passwords, for which SQL is a common solution.</p>
<p>A lot of SQL code can be vulnerable to SQL injections.</p>
<p>An SQL injection is when you modify your input in such a way that you actually modify the SQL query to the database.</p>
<p>So, first we will try to input common characters that are used in SQL into the username box, to see if we can escape the statement.</p>
<p>The ; and ' characters work as expected however when we try the " (double quote) character we can see an error in the web page:</p>
<img src="https://i.imgur.com/Oru7kKK.jpg"/>
<p>From the error we can see that it is indeed an SQL database and that the " character has caused an error.</p>
<p>This is likely because the SQL statement used is not protected.</p>
<p>We can assume that the SQL statment looks something like: SELECT field FROM users WHERE username = "[input]" AND password = "[input]"</p>
<p>And we our input is a ", then the statement would look like: username = """.</p>
<p>Therefore we have escaped the statement and we can add extra code after the " to have it executed.</p>
<p>A common way for SQL injections to select all the fields is to include an "OR 1=1 #" at the end.</p>
<p>So our new statement would look like:</p>
<p>SELECT field FROM users WHERE username = "" OR 1=1 #" AND password=""</p>
<p>This query will select all fields where the username is blank OR where 1=1 and since 1=1 is always true, it will select all fields. The "#" sign is a comment operator and everything after it will be commented out so it is not executed</p>
<p>So, to do this our input will be: " OR 1=1 #</p>
<p>Upon entering this into the username field, we get the password for the next level:</p>
<img src="https://i.imgur.com/rhQybwT.jpg"/>
