import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python {} <filename.js>".format(sys.argv[0]))
    sys.exit()

js_file = sys.argv[1]

with open(js_file, 'r') as f:
    js = f.read()

payload = {'input': js}
url = 'https://javascript-minifier.com/raw'
print("[+] Requesting mini-me of {}. . .".format(f.name))
r = requests.post(url, payload)

minified = js_file.rstrip('.js')+'.min.js'
with open(minified, 'w') as m:
    m.write(r.text)

print("[+] Minification complete. See {}".format(m.name))