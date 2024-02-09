<h2>Natas Level 24</h2>
<p>This level looks the exact same as the last level.</p>
<img src="https://i.imgur.com/HcUH6nS.jpeg"/>
<p>Lets capture a packet with burp, send it to the intruder, and set our variables as shown below:</p>
<img src="https://i.imgur.com/g8Kdcla.jpeg"/>
<p>We will now choose the numbers payload type and cycle through all Hex characters:</p>
<img src="https://i.imgur.com/hK0IlXj.jpeg"/>
<p>That didnt work so we will try the same thing with PHP fuzz words, the wordlist I used has been uploaded to the natas24 folder.</p>
<img src="https://i.imgur.com/VwLuM56.jpeg"/>
<p>And, as we can see, when the [] input was entered we got the password for the next level.</p>
