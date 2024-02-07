<h2>Natas Level 20</h2>
<p>This level lets us input a string.</p>
<img src="https://i.imgur.com/q9Bpjwv.jpeg"/>
<p>There is not much for us to go off of as whatever we input doesnt give us any output. However we can notice that when we input a double quote(") it dissappears upon pressing the button whereas other characters do not.</p>
<p>So, now we will capture the packet with Burp suite.</p>
<img src="https://i.imgur.com/LN5rCAX.jpg"/>
<p>We can see that it also contains a cookie, but this one does not look like hex encoding.</p>
<p>So, we will first fuzz the name parameter by sending the packet to the intruder.</p>
<p>We will then choose the name parameter as our variable, and in the payloads section we will choose a numbers payload, from 00 to FF</p>
<img src="https://i.imgur.com/antqji7.jpg"/>
<p>We will also add a % prefix and URL decoding in the processing section. Then we will start the attack and wait for it to finish.</p>
<img src="https://i.imgur.com/WHs0E7w.jpg"/>
<p>There looks to be nothing out of the ordinary.</p>
<p>So, there is no character that breaks the application, so now lets try a list of different inputs/words.</p>
<p>I will be using a premade list by another user, which can be found here: https://github.com/fuzzdb-project/fuzzdb/blob/master/attack/all-attacks/all-attacks-unix.txt</p>
<p>I will then change the payload type to simple list, paste my list in and turn off the payload processing.</p>
<img src="https://i.imgur.com/jzQ216V.jpg"/>
<p>Now we will run the attack and wait for it to finish.</p>
<img src="https://i.imgur.com/QYvMYBh.jpg"/>
<p>It appears that we do have some anomalies.</p>
<p>There is some type of undefined offset which normally occurs in list data structures.</p>
<p>It only seems to occur when we pass a %0 character.</p>
<p>So lets send our packet to the repeater this time. The repeater allows us to send the same packet to the website over and over.</p>
<img src="https://i.imgur.com/XhwjLFB.jpg"/>
<p>When we send the packet, we dont see any different behaviour, or the undefined offset error.</p>
<p>So lets go back to the intruder to see if we can find anything else.</p>
<img src="https://i.imgur.com/gILg35U.jpg"/>
<p>We can see that the error doesnt happen every time a %0 character occurs.</p>
<p>It appears to only happen when a %0A character is sent before the next input.</p>
<p>A %0A character is a line feed or a new line in Hex.</p>
<p>So, maybe the error occurs as we are adding a new line to a list data structure which would explain the undefined offset.</p>
<p>However, if we send a %0A packet through the intruder multiple times nothing happens.</p>
<p>If we look back in the intruder the %0A character usually had something after them, so lets try that.</p>
<p>If we send multiple %0Atest packets, we now get the undefined offset error.</p>
<img src="https://i.imgur.com/KxmqN4r.jpg"/>
<p>So the error occurs whenever we try and put something in the list on a new line.</p>
<p>Lets look at the source code to help us.</p>
<img src="https://i.imgur.com/SIGMjX0.jpg"/>
<p>This function prints the password for the next level, so we want to satisfy its conditions.</p>
<p>It tells us that there is a $SESSION variable and it has a key admin, and we need to set the value of that key to 1.</p>
<p>Next, we can see the following piece of code which populates the session array.</p>
<img src="https://i.imgur.com/gvxk6iX.jpg"/>
<p>This code splits our input based on a new line character. So we can effectively populate the $SESSION variable however we want.</p>
<p>We will try to populate it with "admin" and "1" to satisfy the conditions of the previous function.</p>
<p>To do this we will send a packet such as: %0Aadmin 1.</p>
<p>And when we send the packet twice using the repeater, we get the password for the next level.</p>
<img src="https://i.imgur.com/SgojUUr.jpg"/>
