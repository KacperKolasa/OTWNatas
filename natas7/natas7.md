<h2>Natas Level 7</h2>
<p>This level has two hyperlinks to a "Home" webpage and an "about" webpage.</p>
<img src="https://i.imgur.com/tGayM2G.jpg"/>
<p>If we press either, it will give us some text however we can observe a change in our URL, theres a "page=" parameter at the end.</p>
<img src="https://i.imgur.com/XyjMiOd.jpg"/>
<p>Lets see if we can manipulate it by entering our own input after the "page=".</p>
<img src="https://i.imgur.com/aMH2IkR.jpg"/>
<p>When we enter a string that the webpage has not prepared for we get an error, this suggets that the input is not filtered.</p>
<p>This means that the webpage does not check if we input any potentially harmful inputs.</p>
<p>On the OverTheWire website it tells us that all passwords are stored in /etc/natas_webpass/natasX, so lets try putting that in, replacing the X with an 8.</p>
<img src="https://i.imgur.com/pNvQt65.jpg"/>
<p>It worked as expected and now we can access the next password.</p>
