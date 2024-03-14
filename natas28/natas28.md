<h2>Natas Level 28</h2>
<p>This level allows us to search a database for  computer jokes.</p>
<p>In the URL we can see that we have a large query parameter:</p>
<img src="https://i.imgur.com/BYOmaIQ.jpeg">
<p>We can URL decode it using cyberchef and we then get a string that appears to be an ECB crypto, which we will have to crack.</p>
<p>We will likely have to use python since it might be quite time consuming otherwise.</p>
<p>So lets first create a program, which will connect to the server, send a query of "a" and then retrive the query from the URL and URL decode it as such:</p>
<img src="https://i.imgur.com/TnDDlcp.jpeg">
<p>Now, we will use a for loop to add an extra a to our query each time so we can find the block size:</p>
<img src="https://i.imgur.com/Gs7qQuP.jpeg">
<p>After we run this code, we can observe the change in size as our query increases in size, and we can deduce that the block size is 16 bits.</p>
<p>Now lets go back to our code, base64 decode our data, turn it into hex and split it every 32 characters to make it more readable:</p>
<img src="https://i.imgur.com/9c6nED1.jpeg">
<p>But now, what can we do with this?</p>
<p>The server is likely using an SQL database to store the jokes, so we need to perform an SQL injection attack.</p>
<p>But if we try it normally we dont get anywhere, probably because our characters such as " are being escaped by the server.</p>
<p>So, a way to get around this is to make sure that we begin our attack right at the end of a block so that whenever the server tries to escape it, it places its \ escape before the start of our attack, which then pushes our attack to the next block which doesnt contain anything but our attack.</p>
<p>Then we can replace the block with a known good block so that our attack works as if there was no escape character.</p>
<p>To do this, we will first use our program to find out when the first block gets filled up.</p>
<p>The first 2 blocks are placeholders that are always the same.</p>
<p>Then the third block is where we start placing our A's in.</p>
<p>And we can observe that when we add 10+ A's the third block remains the same</p>
<p>This means that 10 A's fills the block.</p>
<p>So we want to input 9 A's followed by: ' UNION ALL SELECT password FROM users; #</p>
<p>So we will modify our program to now send a request with a query of: AAAAAAAAA' UNION ALL SELECT password FROM users; #</p>
<img src="https://i.imgur.com/ISxZEhs.jpeg">
<p>Now we have our data which includes our attack:</p>
<img src="https://i.imgur.com/RkZdemE.jpeg">
<p>The fourth block contains our attack, but it will not work as the third block looks something like this:</p>
<p>{unknown characters}AAAAAAAAA\</p>
<p>Therefore we will go back to our previous queries such as this one:</p>
<img src="https://i.imgur.com/VUI0fuQ.jpeg">
<p>And we will take that third block as we know what it is, it is simply full of A's. And we will replace the third block of our attack with this known good block.</p>
<p>Now, our data should look something like this:</p>
<img src="https://i.imgur.com/S8Uxf9g.jpeg">
<p>So we have our complete data, now we need to transform it back into its original state.</p>
<p>So we will put it all on one line, then we will turn decode it from hex, then we will base64 encode it and finally we will URL encode it:</p>
<img src="https://i.imgur.com/Z2e7VlB.jpeg">
<p>And finally we will take that output and insert it into the query in the URL of the website, which will give us the password for the next level:</p>
<img src="https://i.imgur.com/ONcwmg9.jpeg">
