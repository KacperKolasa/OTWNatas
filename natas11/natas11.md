<h2>Natas Level 11</h2>
<p>This level looks different to the others, it allows us to enter a hexadecimal colour code to change the background colour, and it tells us that the cookie is XOR encrypted.</p>
<img src="https://i.imgur.com/VztALPR.jpg"/>
<p>If we look at the source code we can see that our data is stored in an array containing the background colour and a showpassword variable.</p>
<img src="https://i.imgur.com/lGNkBkX.jpg"/>
<p>So our goal would be to change that showpassword variable to "yes".</p>
<p>Further down the sourcecode we can also see how exactly our data is encoded.</p>
<img src="https://i.imgur.com/99AzONb.jpg"/>
<p>Our data array is json encoded, followed by a XOR encryption, followed by a base64 encode.</p>
<p>The one operation here we cannot do yet is the XOR encryption, as to do that we require an encryption key.</p>
<p>However we can obtain the plaintext and the ciphertext and hence we will be able to perform an XOR operation between those two to find the key.</p>
<p>First we find the ciphertext by navigating to the webpage, we can do this by pressing the F12 key and navigating to the Application tab and then finding the Cookie drop down.</p>
<img src="https://i.imgur.com/406bvfs.jpg"/>
<p>However, the cookie is URL encoded, so to decode it we paste it into Cyberchef and then we drag URL decode into the recipe box.</p>
<img src="https://i.imgur.com/QIek7Zw.jpg"/>
<p>Now we have the ciphertext so we need the plaintext, to do this we need a php compiler, I used an online one which you can find here: https://www.programiz.com/php/online-compiler/</p>
<p>I then copied parts of the sourcecode in order to obtain the json and base 64 encoded array.</p>
<img src="https://i.imgur.com/E00Ulcn.jpg"/>
<p>Now that we have both the plaintext and the ciphertext, we can find the key, to do this we will once again use CyberChef.</p>
<p>We will paste the plaintext in the input box, then drag in "From Base64" into the recipe box followed byt he XOR operationand in the key field we will paste the ciphertext and choose base64 as the key type.</p>
<img src="https://i.imgur.com/mgNs5O6.jpg"/>
<p>We get the output KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLK. This is just the string "KNHL" repeating meaning that "KNHL" is our key, as if the key is shorter than the plaintext it will just repeat itself.</p>
<p>Now that we have the key, we will go back to the php compiler and within our php code we will change showpassword to "yes". We will also remove the base64 encode since we can perform the XOR operation on normal text.</p>
<img src="https://i.imgur.com/e5bFWec.jpg"/>
<p>Now we have the new plaintext and the key, so we will go back into CyberChef, paste our plaintext into the input box, drag the XOR operation into the recipe box and paste in our key followed by "To base64".</p>
<img src="https://i.imgur.com/UElZoY6.jpg"/>
<p>Now we have our final cookie that we will inject into the website to reveal the password.</p>
<p>We will once again press F12 and go into the application tab where we can find the Cookie we are changing, we will right click it and press edit value and then remove the old cookie and paste in our new cookie.</p>
<img src="https://i.imgur.com/VV9Or2A.jpg"/>
<p>Now all we have to do is refresh the page to reveal the passowrd.</p>
<img src="https://i.imgur.com/EToLGAm.jpg"/>
