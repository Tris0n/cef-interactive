# CEF Interactive

### Description
Script to interact with node inspector and execute commands in OS.


### Usage
Connect to node inspector running at 127.0.0.1:9229
```
./cef-interactive.py -i 127.0.0.1
```
<br/>

Connect to node inspector running at 127.0.0.1:9228
```
./cef-interactive.py -i 127.0.0.1 -p 9228
```
<br/>

Connect to inspector running at `http://127.0.0.1:8000/node-inspector-proxy`
```
./cef-interactive.py -u http://127.0.0.1:8000/node-inspector-proxy
```

Use flag `-s` to get interactive shell.
