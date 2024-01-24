<H2>Natas Level 5</H2>
<p>This level tells us that access is disallowed.</p>
<img src="https://i.imgur.com/IiSbUwm.jpg"/>
<p>We will now use Burp to capture the packet like we learned to in the last walkthrough.</p>
<p>When we capture the packet we can see a new data field called "Cookie: loggedin=0".</p>
<img src="https://i.imgur.com/Fkd0l1R.jpg"/>
<p>In computer science, 0 tends to mean false while 1 tends to mean true. So we will change the "loggedin=0" to "loggedin=1" and then forward the packet to see if it works.</p>
<img src="https://i.imgur.com/DXHLZZI.jpg"/>
<p>As we can see, that did infact work and we have unlocked the password for the next level.</p>
