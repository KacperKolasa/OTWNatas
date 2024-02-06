<h2>Natas Level 18</h2>
<p>This level allows us to enter a password and username.
<img src="https://i.imgur.com/7kknLnv.jpeg"/>
<p>We'll try to enter natas19 as a username and see what happens:</p>
<img src="https://i.imgur.com/ml4Rpm2.jpeg"/>
<p>We can try other inputs such as admin or ; but they all yield the same result. So refresh the page and capture the packet using Burp Suite.</p>
<img src="https://i.imgur.com/xBrHBe6.jpeg"/>
<p>We can see that we have a session id cookie which has a value 336, this is unusual as cookies are usually long encoded strings.</p>
<p>This may suggest that the cookies are not random and there may be a special cookie that has a different function.</p>
<p>So, lets send this packet to the intruder and and surround the session id number with §</p>
<img src="https://i.imgur.com/XVmIbCU.jpeg"/>
<p>Now lets go into the payloads tab and choose the numbers payload, then set it to try numbers from 1-1000.</p>
<img src="https://i.imgur.com/yFHEVrB.jpeg"/>
<p>Next navigate to the setting tab and find grep extract, we will then highlight the login message:</p>
<img src="https://i.imgur.com/hmPg9q9.jpeg"/>
<p>We will then start the attack and wait for it to finish.</p>
<img src="https://i.imgur.com/rpM3HMk.jpeg"/.
<p>We can see that one cookie gave us a different result from the rest, it tells us that we are logged in as an admin and gives us the password.</p>
<p>We can press on that request to view it in full and we can see the password which is: 8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s</p>
