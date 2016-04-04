<h1>Useful Miscellaneous Commands</h1>

* Send mail from terminal:  
    * `mail -s "I AM SUBJECT" recipient@wix.com` then hit `Cmd + D` when done to send the email.
    * In order to pipe from a file use: `uuencode pathToFile fileName | mail ...`.

* Copy output of command to clipboard: `SOME_COMMAND | tee >(pbcopy)`.
* Prettify JSON: `echo '{"name": "Samar", "country": "Nepal"}' | python -m json.tool`.
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