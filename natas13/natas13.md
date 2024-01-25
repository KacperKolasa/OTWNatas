<h2>Natas Level 13</h2>
<p>This level is similar to the last one but it says that they now only accept images.</p>
<img src="https://i.imgur.com/cgSIoNv.jpg"/>
<p>Lets try uploading our test.txt file again and see what happens.</p>
<img src="https://i.imgur.com/3pbj32r.jpg"/>
<p>As expected it doesn't work, so lets make another test file, but this time we'll make it an image file.</p>
<img src="https://i.imgur.com/g4VnpBj.jpg"/>
<p>The file has been uploaded and can be viewed. So, now we will do the same but capture the packet with Burp.</p>
<img src="https://i.imgur.com/35DxuDH.jpg"/>
<p>It looks similar to the last one, but the content section is a bit different, it includes a PNG header and some more information at the bottom.</p>
<p>Lets see what happens if we change the .jpg and .png file extensions to .php, and remove the bottom line of the content but keep the PNG header so that the program still thinks its a PNG file.</p>
<p>We will also replace the bottom line of the content with the same php code we used for the last level, it should look like this:</p>
<img src="https://i.imgur.com/3zyMvfz.jpg"/>
<p>We will now forward that packet and we can see that the file was uploaded so our plan worked, and if we visit the uploaded file we can see the password for the next level.</p>
<img src="https://i.imgur.com/BfYlngZ.jpg"/>
