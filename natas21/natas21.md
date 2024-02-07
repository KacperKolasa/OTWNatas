<h2>Natas Level 21</h2>
<p>This level tells us that  it is colocated with another website.</p>
<img src="https://i.imgur.com/aueZmlV.jpeg"/>
<p>We can visit that website and it allows us to change the properties of some text.</p>
<img src="https://i.imgur.com/FZNC9Cv.jpeg"/>
<p>Lets look at the sourcecode of the home website:</p>
<img src="https://i.imgur.com/5taDLwz.jpeg"/>
<p>There looks to be nothing of interest there. But the colocated website has more interesting sourcecode.</p>
<img src="https://i.imgur.com/DWZ5dch.jpeg"/>
<p>This function tells us that there is a Debug GET parameter available.</p>
<p>We can access it by adding a "?debug" to the end of our url.</p>
<img src="https://i.imgur.com/zrtgVus.jpeg"/>
<p>Now we can see the contents of the session array.</p>
<p>If we go back to the first website, we can see that the sourcecode is looking for an admin key, and since the two websites are colocated they might share session cookies.</p>
<p>We can assume that the cookie stores the session data, so our goal is to add "admin" and "1" into the array.</p>
<p>Lets capture a packet from the colocated website in Burp.</p>
<img src="https://i.imgur.com/VtGpzSB.jpeg"/>
<p>We can see that the packets contains the items that we saw in the array.</p>
<p>This means that the array is being populated from this insecure packet, so maybe we can use that to our advantage.</p>
<p>We will add a "&admin=1" to the end after Update. This will hopeffully add it to the array, we also want to deleted the PHPSESSID cookie as it stores data and we want to force the website to create a new one.</p>
<img src="https://i.imgur.com/kiFrYKD.jpeg"/>
<p>Now we will go back to our page, enter the debug parameter and we should see the admin=1 in the array.</p>
<p>Next, we will press F12 to go into the developer tools, we will find the cookie and copy it.</p>
<img src="https://i.imgur.com/6FxzAne.jpeg"/>
<p>Now, we will return to the first webpage, open the developer tools and change the cookie to our new cookie. We will then refresh the page.</p>
<img src="https://i.imgur.com/Ay195R2.jpeg"/>
<p>We can now see the password for the next level.</p>
