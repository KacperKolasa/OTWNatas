<h2>Natas Level 4</h2>
<p>Upon logging into the next level, we now see:</p>
<img src="https://i.imgur.com/H8LnUui.jpg"/>
<p>There is nothing for us to work with on the website or in the elements tab. Therefore this level will be more challenging than the others.</p>
<p>We will need to intercept the HTTP packet coming from our browser to the web server.</p>
<p>To do this we will require a software called Burp Suite which can be obtained here: https://portswigger.net/burp</p>
<p>Upon installing Burp Suite, we open it and are welcomed by the following screen:</p>
<img src="https://i.imgur.com/49b8wwG.jpg"/>
<p>This software has a lot of functionalities and may seem overwhelming but for now, we will only use the proxy tab at the top.</p>
<img src="https://i.imgur.com/XbFlxrt.jpg"/>
<p>From here, we will press the "Intercept is off" button, followed by the "Open browser" button:</p>
<img src="https://i.imgur.com/h3xBzCO.jpg"/>
<p>This will open a new browser window, for which we are intercepting every packet being transferred.</p>
<p>In the new browser window, we will navigate back to the natas4 webpage, however it won't load as Burp has captured the packet:</p>
<img src="https://i.imgur.com/GrjQJ3Q.jpg"/>
<p>Here we can see all of the packet information and we will press the "Forward" button in the top left to send the packet to the web server.</p>
<p>After we're logged into the website again, we will refresh the webpage and inspect the packet captured by Burp.</p>
<img src="https://i.imgur.com/Eujd9PP.jpg"/>
<p>Here, we can see a bunch of information about the packet, but the part we are interested in is the "Referer" value.</p>
<p>The website told us that authorized users should be visiting from "http://natas5.natas.labs.overthewire.org/".</p>
<p>So we will manipulate the Referer value to "http://natas5.natas.labs.overthewire.org/" and then we will forward the packet.</p>
<p>And when we go back to the webpage, we can now see the password for the next level:</p>
<img src="https://i.imgur.com/wUvi3k5.jpg"/>
