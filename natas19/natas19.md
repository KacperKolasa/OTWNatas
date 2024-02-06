<h2>Natas Level 19</h2>
<p>This level tells us that the session id is no longer sequential.</p>
<img src="https://i.imgur.com/xZIm1Gp.jpeg"/>
<p>When we try to login in as admin, we get the same message as last level, so lets capture the packet using Burp.</p>
<img src="https://i.imgur.com/Ni67Hdm.jpeg"/>
<p>It looks like the session id is now encoded, lets see if we can quickly decode it.</p>
<p>We will put it into cyber chef, and it look like the session id is simply turned into Hex.</p>
<img src="https://i.imgur.com/B4Q97M7.jpg"/>
<p>The decoded session id is 571-admin, which leads me to believe the session ids are sequential and there may again be a certain id that will let us through.</p>
<p>So, lets forward this packet to the intruder, and surround the session id with § signs.</p>
<img src="https://i.imgur.com/oKvLQwz.jpeg"/>
<p>Next we head over to the payloads tab, choose the numbers payload and set it to go through the numbers 1-1000.</p>
<p>Next we will go to the payload processing and add a "-natas20" suffix to our payload and the hex encode it so its in the form of the original id.</p>
<img src="https://i.imgur.com/qqEdATt.jpg"/>
<p>Next go the the Grep Extract option and highlight the wanted text and press add:</p>
<img src="https://i.imgur.com/jvLG7rh.jpg"/>
<p>Now we want to start the attack and wait for it to finish.</p>
<img src="https://i.imgur.com/GbFkOLh.jpg"/>
<p>We can see that one session id logged us in as admin, we can click on that request to get the password which is: guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH</p>
