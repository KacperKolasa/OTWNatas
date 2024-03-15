<h2>Natas Level 29</h2>
<p>This level has some text and a drop down menu for us.</p>
<img src=>
<p>When we select an option from the menu we are greeted by a lot of text, which would take too long to look through.</p>
<p>So, instead lets capture a packet and fuzz the GET parameter:</p>
<img src=>
<p>We are going to use the numbers payload for every hex character.</p>
<p>After fuzzing with the numbers payload, we can see that there is a slight change in length when using the 0 character:</p>
<img src=>
<p>Upon further investigation, when we use the 0 character the pre tags are removed</p>
<p>So now lets fuzz again but with the 0 character before our fuzz.</p>
<img src=>
<p>And we didnt get any abnormal results.</p>
<p>So this time lets fuzz using wordlists.</p>
