<h2>Natas Level 29</h2>
<p>This level has some text and a drop down menu for us.</p>
<img src="https://i.imgur.com/lIRrFgz.jpg">
<p>When we select an option from the menu we are greeted by a lot of text, which would take too long to look through.</p>
<p>So, instead lets capture a packet and fuzz the GET parameter:</p>
<img src="https://i.imgur.com/lmAeKhI.jpg">
<p>We are going to use the numbers payload for every hex character.</p>
<p>After fuzzing with the numbers payload, we can see that there is a slight change in length when using the 0 character:</p>
<img src="https://i.imgur.com/rVpzlCH.jpg">
<p>Upon further investigation, when we use the 0 character the pre tags are removed</p>
<p>So now lets fuzz again but with the 0 character before our fuzz.</p>
<img src="https://i.imgur.com/ogYGN18.jpg">
<p>And we didnt get any abnormal results.</p>
<p>So this time lets fuzz using wordlists.</p>
<p>We will use a word list from fuzzDB which can be found here: https://github.com/fuzzdb-project/fuzzdb/blob/master/attack/all-attacks/all-attacks-unix.txt</p>
<p>We will paste this word list into a simple list payload and we will start our attack.</p>
<p>We can see that using the pipe (|) character gives us a different output:</p>
<img src="https://i.imgur.com/HqH1KZv.jpg">
<p>The pipe character allows you to pass the output of a command to the next command in Linux, so lets send our packet to the repeater and explore this more.</p>
<p>Lets try to output "Hello World" by passing "|echo 'hello world';" as the GET parameter:</p>
<img src="https://i.imgur.com/pmcbo6p.jpg">
<p>We can see that that did infact work, so now lets try to get that password using: cat /etc/natas_webpass/natas30;</p>
<p>When we send this request through, the output is "meeeeeep!" instead.</p>
<img src="https://i.imgur.com/IM3ZKtp.jpg">
<p>This is likely because of a safety feature that detects when we try to access the password.</p>
<p>If we open the source code file, we can see that it is indeed the case, as it searches for the string "natas"</p>
<img src="https://i.imgur.com/2YgmsNo.jpg">
<p>We can try to bypass this using the * operator, in perl which is the langauge this source code is written in, the * operator is a placeholder and will return us with anything that matches all the other charcaters.</p>
<img src="https://i.imgur.com/b4NfJrR.jpg">
<p>We can see that that has worked and we now have the password for the next level.</p>
