<h2>Natas Level 12</h2>
<p>This level allows us to upload a file and then have it displayed on the webpage.</p>
<img src="https://i.imgur.com/K8xb9o2.jpg"/>
<p>First, we'll create a txt file called test and see what happens.</p>
<img src="https://i.imgur.com/wAvk0pa.jpg"/>
<p>Our file has been uploaded to the website and we can view it if we press on the hyperlink.</p>
<p>Lets try that again but capture the packet with Burp Suite as we did previously.</p>
<img src="https://i.imgur.com/8h1IUm8.jpg"/>
<p>We can see a bunch of information about the file such as the name and contents.</p>
<p>We will now try to modify these files to execute code for us, first we will change the .jpg and .txt file extensions to .php, and then we will change the file contents to some php test code.</p>
<img src="https://i.imgur.com/p8VmGA4.jpg"/>
<p>We will then forward this packet and we will see that it succesfully uploads, so we will press the file hyperlink to view it.</p>
<img src="https://i.imgur.com/utCjaCh.jpg"/>
<p>We can see the text "test" on screen which means that we now have the ability to execute php code.</p>
<p>We can use this to our advantage and attempt to print the contents of the natas13 file.</p>
<p>We will once again capture the packet and modify it like last time but this time we will change the php code.</p>
<p>We will use the passthru() command to pass any command to the shell so it can be executed.</p>
<p>We'll want to pass the command "cat /etc/natas_webpass/natas13" which essentially prints out all of the text in the specified file.</p>
<p>We also have to put an echo command infront of the passthru() so that the output can be printed to the screen.</p>
<p>So, our new php code will be: echo passthru('cat /etc/natas_webpass/natas13')</p>
<img src="https://i.imgur.com/5Df0IlC.jpg"/>
<p>And when we forward the packet and check the uploaded file we can see the password for the next level:</p>
<img src="https://i.imgur.com/tQ5I8lP.jpg"/>
