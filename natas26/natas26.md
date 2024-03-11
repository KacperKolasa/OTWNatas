<h2>Natas Level 26</h2>
<p>This level allows us to enter a pair of coordinates, after which it draws a line between them.</p>
<img src="https://i.imgur.com/rHG7OvS.jpeg">
<p>Lets look at the source code to see if we can gather any more information.</p>
<img src="https://i.imgur.com/T7uftlK.jpeg">
<p>This function creates a log file and writes to it, which may be useful in the future.</p>
<img src="https://i.imgur.com/D0kZ6WD.jpg">
<p>Here we can see that the coordinates are gathered via GET parameters after which they are passed to a different function.</p>
<img src="https://i.imgur.com/TwhthrM.jpg">
<p>Here, we have a more interesting function, we can see that there exists a drawing cookie, which is serialized and base64 encoded.</p>
<p>Lets capture a packet using Burp to see if we can retrieve this cookie.</p>
<img src="https://i.imgur.com/T1Qt3Er.jpg">
<p>Now that we have the cookie, lets decode it using an online php compiler, we want to url decode it first, then base64 decode it and finally unserialize it as shown:</p>
<img src="https://i.imgur.com/CJP9j4O.jpg">
<p>We can see that the cookie represents the array of coordinates that make up each line.</p>
<p>However, since we can control our cookie, we may be able use that to our advantage.</p>
<p>We now want to further explore the behaviour of the application, so on a Linux VM I will create a new php file and paste all of the websites source code in there.</p>
<p>You can make a new folder from the CLI using mkdir {name} and then you can create and edit a file using vim {name}</p>
<p>Now, we want to make a live development serve for our code so we can see it in action.</p>
<p>We can do this using the command: php -S 127.0.0.1:1508</p>
<img src="https://i.imgur.com/Yb6O9Ul.jpg">
<p>After we've done this we can visit our code on a browser.</p>
<img src="https://i.imgur.com/qc612FE.jpg">
<p>However, when we try to draw a line, nothing happens. Lets go back to our console to see any errors.</p>
<img src="https://i.imgur.com/Tee4VaJ.jpg">
<p>As we can see there is an error, which tells us that the line image was not generated as there is no "img" folder so the image cannot be retrieved.</p>
<p>To fix this we will create an img folder in our directory using mkdir img. After which we should be able to draw a line.</p>
<p>Next, we want to edit the source code a bit. First we will head to the construct function where we will change the log file to: img/natas26_ ... and we will change the file type to .php</p>
<p>We do this as the img directory is one we have access to as this is where the line image is stored.</p>
<img src="https://i.imgur.com/ZDG76oE.jpg">
<p>Now we will go to the bottom of the code, where we will create a new logger object and we will print it to the screen.</p>
<img src="https://i.imgur.com/eWoGhiX.jpg">
<p>Now if we save that and refresh our webpage, we can see the contents of the logger object:</p>
<img src="https://i.imgur.com/yeKeYrn.jpg">
<p>So, lets go back to the file editor and this time change the exit message.</p>
<p>We will change it to php code that prints out a simple hello world:</p>
<img src="https://i.imgur.com/enVf1bH.jpg">
<p>Next we will refresh our page to see if it worked.</p>
<img src="https://i.imgur.com/GxgO7Ud.jpg">
<p>We can see that our exit message is empty, this means that our code was executed but for some reason we can't see it.</p>
<p>So we will edit the code to instead output a serialized and base64 encoded string as such:</p>
<img src="https://i.imgur.com/Pzk9TS3.jpg">
<p>Which now gives us this output:</p>
<img src="https://i.imgur.com/3NdfYwH.jpg">
<p>And after we put that into CyberChef, we can see our whole logger object and our code is indeed there:</p>
<img src="https://i.imgur.com/JPdxj5A.jpg">
<p>So lets go back to the file editor and change the exit message to print the next level password.</p>
<img src="https://i.imgur.com/4lsAITx.jpg">
<p>Now lets copy our new encoded string, and go back to the real natas webpage.</p>
<p>After which we will access the cookie using the developer tools and we will paste our own cookie in after we URL encode it.</p>
<img src="https://i.imgur.com/o3YC3Pk.jpg">
<p>And now we will navigate to the /img/natas26_test.php file where we can find our password:</p>
<img src="https://i.imgur.com/G3szcRJ.jpg">
