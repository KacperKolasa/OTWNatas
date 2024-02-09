<h2>Natas Level 23</h2>
<p>This level allows us to enter a password.</p>
<img src="https://i.imgur.com/yTl3L4b.jpeg">
<p>We can try using characters such as " ' ; etc. but they all give us the same output of "Wrong!"</p>
<img src="https://i.imgur.com/P1rae1N.jpeg">
<p>Lets capture a packet using burp.</p>
<img src="https://i.imgur.com/im50p6X.jpeg">
<p>We can see that the request has a passwd parameter, so we will try to fuzz this.</p>
<p>We will send it to the intruder and set the payload type to Numbers, and have it search through 00 to FF in Hex.</p>
<img src="https://i.imgur.com/QNDLoY0.jpeg">
<p>We will now start the attack and see if anything abnormal happens.</p>
<img src="https://i.imgur.com/md8aGnk.jpeg">
<p>Nothing abnormal happened, so lets look at the source code to get a better idea.</p>
<img src="https://i.imgur.com/QnKVrZM.jpeg">
<p>From the source code, we can see that the password needs to contain the string "iloveyou" and the password has to be greater than 10.</p>
<p>But, the password is a string so how can it be greater than 10?</p>
<p>This can actually be done due to PHP's flawed type system.</p>
<p>In PHP you do not have to declare types yourself, PHP determines the types of variables at runtime, which therefore makes it very user friendly, but also vulnerable to attacks like these.</p>
<p>Therefore, if we have a string such as "1234string", PHP will start reading it and due to the 1234 at the start it will think its an integer.</p>
<p>And this is how we can make the web server think that our password which is a string is indeed greater than 10.</p>
<p>So, we will use "1234iloveyou" as our password.</p>
<img src="https://i.imgur.com/11JJ3h6.jpeg">
<p>And, as we can see we've got the password for the next level.</p>
