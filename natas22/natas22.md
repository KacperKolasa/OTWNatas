<h2>Natas Level 22</h2>
<p>This level seems to be a simple blank page.</p>
<img src="https://i.imgur.com/O3F00JP.jpeg">
<p>But there is likely some hidden functionalities.</p>
<p>We will try to find hidden content via the URL, but how do we know what to type in?</p>
<p>There is no robots.txt for this webpage.</p>
<p>We will use a tool called Cewl, for which you can find more information here: https://www.kali.org/tools/cewl/#:~:text=CeWL%20(Custom%20Word%20List%20generator,CeWL%20can%20follow%20external%20links.</p>
<p>I am going to be using this tool via the Linux CLI however there are other ways to run it if you do not have Linux.</p>
<p>First, we will run the "cewl" command in the CLI to make sure we have it installed.</p>
<img src="https://i.imgur.com/jBexqbc.jpeg">
<p>Next, we will tell the command the url of our website and also the username and password to log in with. We will also tell it to store the output in a txt file using the > operator.</p>
<img src="https://i.imgur.com/0gYQocA.jpeg">
<p>As we can see, the word list is now in our txt file:</p>
<img src="https://i.imgur.com/61sTmte.jpeg">
<p>Next we will refresh our webpage to capture a packet with Burp, and we will send that packet to the intruder.</p>
<p>We will then put the variable signs infront of the forward slash after GET.</p>
<img src="https://i.imgur.com/JagPz1N.jpeg">
<p>Then we will head over to the payloads tab, select the simple list payload and paste in our word list.</p>
<img src="https://i.imgur.com/fMvblh6.jpeg">
<p>We will wait for the attack to finish and inspect the results for anything interesting.</p>
<img src="https://i.imgur.com/f4t3QSv.jpeg">
<p>There appears to be nothing abnormal, so we will try the same but we'll modify our attack.</p>
<p>We will put a "?" sign before our variable so that this time we are looking for any potential GET parameters.</p>
<img src="https://i.imgur.com/n3jHKYC.jpeg">
<p>Now it looks like we do have an abnormal result.</p>
<p>When using the GET parameter "revelio" we have a longer response than the others, so lets investigate.</p>
<img src="https://i.imgur.com/j7vNGZF.jpeg">
<p>We can see that using this parameter gave us the password for the next level.</p>
