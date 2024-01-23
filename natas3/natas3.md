<h2>Natas Level 3</h2>
<p>This level once again tells us that there is nothing on this page.</p>
<img src="https://i.imgur.com/mIN9q4S.jpg"/>
<p>We will now look at the elements tab in the developer tools again.</p>
<img src="https://i.imgur.com/OxMBMUe.jpg"/>
<p>We can see a line saying: "No more information leaks!! Not even Google will find it this time..."</p>
<p>It may not look like it, but this is actually a hint for us.</p>
<p>Search engines such as Google use web crawlers to index all of the webpages that are available to visit.</p>
<p>In order to help these web crawlers, websites often have a robots.txt file containing all the different indexes the website contains.</p>
<p>We can use this to find any hidden indexes that the website may not want us to visit, so when we add a "/robots.txt" to the end of the URL we can see:</p>
<img src="https://i.imgur.com/hBPuiPM.jpg"/>
<p>Here we can see a index that should not be visited by the web crawler, as specified by the "Disallow" line.</p>
<p>We can now visit that index to see if it contains anything that will help us.</p>
<img src="https://i.imgur.com/W0b6jWJ.jpg"/>
<p>It appears that the index leads us to a file directory, containing a file called users.txt, when we open it we can see:</p>
<img src="https://i.imgur.com/SwR6hiU.jpg"/>
<p>Which is the username and password for the next level.</p>
