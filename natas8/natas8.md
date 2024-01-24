<h2>Natas Level 8</h2>
<p>This level looks the same as the previous one.</p>
<img src="https://i.imgur.com/lnt9zGY.jpg"/>
<p>However, when we enter something into the input box, it does not appear in the URL. So, now we can look at the sourcecode.</p>
<img src="https://i.imgur.com/Wp7KYkA.jpg"/>
<p>We can see something interesting in the source code, we can an encoded string: "3d3d516343746d4d6d6c315669563362".</p>
<p>We can also see the algorithm used to encode that string which is: bin2hex(strrev(base64_encode($secret))).</p>
<p>This can be translated to: String -> base 64 encode string -> reverse string -> turn to hexadecimal</p>
<p>So, to get the original string back we have to do the reverse of this, which would be:</p>
<p>Encoded string -> turn from hexadecimal -> reverse string -> base 64 decode.</p>
<p>We can do all these operations with a web application called CyberChef, which can be found at: https://gchq.github.io/CyberChef/</p>
<img src="https://i.imgur.com/4DjVjvu.jpg"/>
<p>To use this application we will first put our encoded string in the top right input box.</p>
<p>Then we see all the possible operations in the sidebar on the left.</p>
<p>We will drag all of our required operations into the recipe box to the right.</p>
<p>First, we'll drag "From Hex" in, followed by "Reverse" and finally "From Base64".</p>
<p>If done correctly we should get the decoded secret back in the output box.</p>
<img src="https://i.imgur.com/YtkPU59.jpg"/>
<p>We will now take this string and enter it back into the secret input box on the natas webpage.</p>
<img src="https://i.imgur.com/Ig7ti4l.jpg"/>
<p>Now we can see the password for the next level.</p>
