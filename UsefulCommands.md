<h1>Useful Miscellaneous Commands</h1>

* Send mail from terminal:  
    * `mail -s "I AM SUBJECT" recipient@wix.com` then hit `Cmd + D` when done to send the email.
    * In order to pipe from a file use: `uuencode pathToFile fileName | mail ...`.

* Copy output of command to clipboard: `SOME_COMMAND | tee >(pbcopy)`.
* Prettify JSON: `echo '{"name": "Samar", "country": "Nepal"}' | python -m json.tool`.
* * Prettify JSON into a file and open it in Sublime Text: 
	```
	pbpaste | python -m json.tool > /tmp/formatted.json && subl /tmp/formatted.json
	```
* See raw HTTP request: `echo -e HTTP/1.1 200 OK\\nConnection: close\\n\\nHello World | nc -v -l 8000` then perform an HTTP request to `http://localhost:8000`.
* Show full path in Finder header:

	```
	defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES
	killall Finder
	```
	
* Add quit to Finder menu:

	```
	defaults write com.apple.Finder QuitMenuItem -bool YES
	killall Finder
	```
	
* Copying files over SSH:
	* To copy a file from B to A while logged into B:
	
		```
		scp /path/to/file username@a:/path/to/destination
		```
	* To copy a file from B to A while logged into A:

		```
		scp username@b:/path/to/file /path/to/destination
		```
		
* URL decoding and encoding:
	* decode: `python -c "import sys, urllib as ul; retval = ul.unquote_plus(sys.argv[1]) if len(sys.argv) == 2 else \"Please pass a single argument.\"; print retval" <MY_STRING>`
	* encode: `python -c "import sys, urllib as ul; retval = ul.quote_plus(sys.argv[1]) if len(sys.argv) == 2 else \"Please pass a a single argument.\"; print retval" <MY_STRING>`

	
* Generate dependency graph for a project (formats other than DOT can also be used):
	1. Go to the topmost project directory.
	2. Run the command in order to create a `dependency.dot` file for each project.
		```
		mvn dependency:tree -DoutputType=dot -DoutputFile=dependency.dot -Dincludes=com.wix.*,com.wixpress.*
		```
		
* Delete all files with extention `.ext` recursively:

	```
	find /path/to/delete/from -name '*.ext' -delete
	```
	
* Grep through an entire directory:

	```
	grep -nr string my_directory
	```
	
* Favourite aliases in one liner:

	```
	alias ll='ls -al';alias cd..='cd ..';alias l='ls'
	```
	
* Most recent file in directory:

	```
	ls -Art | tail -n 1
	```
	
* See changes in file live:

	```
	tail -f FILENAME
	```
	
* Display free space for all partitions:

	```
	df -h
	```
	
* Convert hex IP to decimal dot notation:

	```
	python -c "import sys;b=sys.argv[1].replace('0x','');print('.'.join(map(lambda x: str(int(x, 16)), [b[i:i+2] for i in range(0,len(b), 2)])))" IP_AS_HEX_STRING
	```
	
	
* Increase heap size for JVM (both for javac and zinc):

	```
	export JAVA_OPTS="-Xms2200m -Xmx8192m -XX:MaxPermSize=1024m"
	```
	
* Cut N lines from file into another file:

	```
	head -<N> input > output && tail -n +<N> input > output_2
	```
* Count number of files of type `ext` in current folder recursively:

	```
	find . -type f -name '*.ext' | wc -l
	```
* To start maven from the latest failed module (maven will usually write the last module name as the last line of output):

	```
	mvn clean install -rf :<last-module-name>
	```