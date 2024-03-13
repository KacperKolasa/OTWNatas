<h2>Natas Level 27</h2>
<p>This level allows us to login or create an account depening on if that username already exists.</p>
<img src="https://i.imgur.com/1qYiEEn.jpeg">
<p>First lets try putting charcaters such as: ' " ; into the fields to see if we get anything abnormal.</p>
<img src="https://i.imgur.com/JT7CQfV.jpeg">
<p>Using these characters did not seem to do anything, but we should note that natas28 is a valid user. So lets dive deeper.</p>
<p>Lets try logging in and lets capture the packet using Burp.</p>
<img src="https://i.imgur.com/k6TY7Sw.jpeg">
<p>Lets send this packet to the intruder, and fuzz both variables, using the battering ram attack which input our payload into both variables.</p>
<img src="https://i.imgur.com/3k8HlDt.jpeg">
<p>For our payload we are going to use the numbers payload to iterate through all hex numbers.</p>
<img src="https://i.imgur.com/ESBA5ac.jpeg">
<p>After doing this we have some interesting results.</p>
<img src="https://i.imgur.com/N1T8TVr.jpeg">
<p>From this we can gather that usernames are not case sensitive, and that the space character triggers a "Go away hacker" message.</p>
<p>We will now further investigate the space character.</p>
<p>To do this we will choose the cluster bomb attack type which is essentially a nested for loop. In our first payload we will use a simple list containing of simply the space character.</p>
<p>Our second payload will once again be the numbers payload from 00 to FF.</p>
<p>The results from this attack are similair to the previous one.</p>
<p>So lets try something else with the space character.</p>
<p>We will change our attack type to sniper and remove one of the variables. We will also user the natas28 username before the spaces.</p>
<img src="https://i.imgur.com/JOf93ph.jpeg">
<p>For our payload we are going to use the brute forcer, with only the space character.</p>
<p>We wil then set the min length to 1 and max to 100 so we can see if we can possibly input too many spaces.</p>
<img src="https://i.imgur.com/VOd3hGG.jpeg">
<p>We see nothing useful, so lets look at the source code.</p>
<img src="https://i.imgur.com/DgAQKtp.jpeg">
<p>We see that the username and password fields have a max length of 64 and we know that spaces/null characters are truncated.</p>
<p>So, lets try putting natas28{64 spaces}test in the username field.</p>
<p>We dont see any change so lets try the same but with null characters through burp.</p>
<p>It tells us that user natas28test was created, so now lets try logging in as natas28</p>
<p>And as we can see, we have got the password for the next level.</p>
<img src="https://i.imgur.com/VkkPLum.jpeg">
