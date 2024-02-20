<h2>Natas Level 25</h2>
<p>This level displays a quote, it also allows us to choose a language for the quote.</p>
<img src="https://i.imgur.com/AAfJpF4.jpeg">
<p>However we can see that there is a language parameter in the URL, so lets capture the packet with Burp and fuzz the parameter with the PHP fuzz list we used in the previous level.</p>
<img src="https://i.imgur.com/EqFXSBQ.jpeg">
<p>Unfortunately this didnt give us anything useful, so lets look at the sourcecode.</p>
<img src="https://i.imgur.com/kTZCjru.jpeg">
<p>Whenever we choose a language, this setLanguage() function is run. It checks our input to see if its "safe" using the safeinclude() function.</p>
<img src="https://i.imgur.com/3Yr0AQH.jpeg">
<p>This function first checks for the existance of a "../" as this can be used for directory traversal, however this function isnt recursive so we can exploit that.</p>
<p>Instead of using "../" we can use "....//" so that it does remove a "../" but when it does it actually creates another one that it doesnt check for.</p>
<p>However the function also checks for the existance of "natas_webpass" which is where our password is held and we cannot bypass.</p>
<p>Lets look at the next function:</p>
<img src="https://i.imgur.com/NF1gVuo.jpeg">
<p>This function creates a log, with the date the HTTP user agent and the message.</p>
<p>We do not have access to any of these except for the user agent.</p>
<p>So lets try to capture a packet and modify the user agent to see if we can execute code from it.</p>
<img src="https://i.imgur.com/sR9I2dY.jpeg">
<p>Now, lets look at the log file which is located in var/www/natas/natas25/logs/natas25_{session-id}.log</p>
<p>We can navigate to it using our previous directory traversal technique.</p>
<p>So for our lang parameter we will instead input: ....//....//....//....//....//....//....//....//....//....//var/www/natas/natas25/logs/natas25_{session-id}.log</p>
<img src="https://i.imgur.com/reQBe8N.jpeg">
<p>And, as we can see our "hello!" message is in there so we know that we can execute code.</p>
<p>So, lets try the same but this time we will try to print the contents of the natas26 file, with the command: echo shell_exec("cat /etc/natas_webpass/natas26");</p>
<img src="https://i.imgur.com/nEFILvF.jpeg">
<p>As we can see the log now contains the password for the next level.</p>
