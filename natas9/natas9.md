<h2>Natas Level 9</h2>
<p>This level allows us to search for a string through a file, and outputs them all for us.</p>
<img src="https://i.imgur.com/qbK3vQz.jpg"/>
<p>If we look at the sourcecode, we can see that our input is taken in and stored as the "key" variable.</p>
<img src="https://i.imgur.com/r3jcgM8.jpg"/>
<p>This variable is then inserted into: "passthru("grep -i $key dictionary.txt");".</p>
<p>The passthru command will essentially pass any command into the shell and execute it, so in this case it will execute the grep command.</p>
<p>The grep command searches for a given string(the key variable in this case) in the file provided after.</p>
<p>However, this command can take multiple files to search through, and it appears that the input in unfiltered.</p>
<p>We will try to enter a "." as input, and we get back every string in the file as a "." matches everything in regular expressions.</p>
<img src="https://i.imgur.com/I0u7G4h.jpg"/>
<p>Since the input is unfiltered we can try to pass in another file for the command to search through.</p>
<p>We want to search through /etc/natas_webpass/natas10, so our input will be ". /etc/natas_webpass/natas10".</p>
<p>The command should now look like: "grep -i . /etc/natas_webpass/natas10 dictionary.txt", which means its looking for any string in both files specified.</p>
<p>And when we enter the input ". /etc/natas_webpass/natas10" into the text box the first line provides us with the password for the next level:</p>
<img src="https://i.imgur.com/6KfGa0j.jpg"/>
