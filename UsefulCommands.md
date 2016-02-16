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