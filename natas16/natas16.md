<h2>Natas Level 16</h2>
<p>When we log into this level, we can see a similar layout to last time, but it says that more characters are now filtered.</p>
<img src="https://i.imgur.com/m67p6bV.jpeg"/>
<p>We want to figure out which characters are filtered, so we will capture the packet using burp.</p>
<p>We will then press the action button and send it to the intruder.</p>
<p>From there, we will choose the sniper attack type, and then we will highlight the text after needle= and press the "Add §" button on the right.</p>
<img src="https://i.imgur.com/Yp9Vtdq.jpg"/>
<p>Now we will head over to the payloads tab.</p>
<p>From here we will choose the numbers payload type and change the "From:" setting to "00" and the "To:" setting to "FF".</p>
<p>Also make sure to select the Hex base option.</p>
<p>This will try every character possible for us.</p>
<img src="https://i.imgur.com/TErZYwM.jpg"/>
<p>Then we will scroll down to the payload processing, where we will add a "%" prefix and then a URL decode.</p>
<p>This will URL encode the characters so that they are read as the actual characters and not for example 00 or 0a.</p>
<img src="https://i.imgur.com/eAf2zTL.jpg"/>
<p>We will then go into the setting tab and scroll down to "Grep - Extract", where we will press the Add button</p>
<p>We will then scroll and find the part of the response showing the output of the program, and we will highlight it and press OK.</p>
<img src="https://i.imgur.com/Z7ChOqG.jpg"/>
<p>Now, we will press the "Start Attack" button in the top right and wait for it to finish.</p>
<p>Once, it's finished we can see the response for each character and we can see all of the illegal characters:</p>
<img src="https://i.imgur.com/Y8bT0c6.jpg"/>
<p>A lot of characters are filtered, however there are still more we can use.</p>
<p>We can still use $(), which will pass a command to the shell to be executed.</p>
<p>Lets try this on the website by entering $(echo a) into the text box.</p>
<img src="https://i.imgur.com/UdUUpYz.jpeg"/>
<p>We get back every word in the file containing an a, indicating that our method is working, so we can likely do something with it.</p>
<p>If we try printing the files of the natas17 file, we get zero output.</p>
<p>So, lets try a different command such as grep, which returns all strings from a file containing the specified text.</p>
<p>We will try: $(grep a /etc/natas_webpass/natas17)</p>
<p>We get a list of every word in the text file.</p>
<p>Now, lets try $(grep b /etc/natas_webpass/natas17).</p>
<p>However, this time we get zero output.</p>
<p>So we are getting two different outputs based on two different conditions, likely that if our character exists or not.</p>
<p>When we tried printing the contents of the natas17 file, we also got zero output, so for now we will assume that if there is zero output, that character is within the file.</p>
<p>However this on its own is not exactly helpful as we could eventually figure out all the characters, but we still would not have those characters in order, and it would take too long to try and order them.</p>
<p>We can fix this issue using regular expressions.</p>
<p>To use regular expressions, we have to add a -E option to our grep command.</p>
<p>Then our regular expression will be: ^a.*$</p>
<p>the ^ sign signifies the start of the line, so in this case the expression will be true for any string starting with a.</p>
<p>The . allows any character to pass, the * represents zero or more occurances of the previous character and the $ signifies the end of the line.</p>
<p>So, our new command will be: $(grep -E ^a.*$ /etc/natas_webpass/natas17) where a will be the variable we change to find our character.</p>
<p>Once we find the first character, we will prepend the statement with that character and carry on.</p>
<p>So for example if b was the first character we would change our statement to ^ba.*$ where a is still a placeholder.</p>
<p>Now, we have a method for finding the password, however this would be very time consuming, so we will create a python script to automate it.</p>
<p>First we will create a basic program to log into the webpage and print the response to check that everything works.</p>
<img src="https://i.imgur.com/pGWyrOh.jpeg"/>
<p>Next we will create a list of characters for the program to go through, and the parameter variable that we will pass to the request.</p>
<img src="https://i.imgur.com/dajkpmq.jpeg"/>
<p>Now, we have all the basic functionalities complete, so we will create a nested loop to go through each index of the password and try every character and when a character is found it is appended to the final password variable.</p>
<img src="https://i.imgur.com/3aau6ng.jpeg"/>
<p>Now, after we run the program we should get the password, which is: XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd</p>
