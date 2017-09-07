# Typograf Service

Typograf service has basic functionality and runs on localhost with help of Flask.
It can chain extra functionality. Just create a function that takes and returns a string object and add it into 'def apply_processors_chain(to_string)' in the 'typograf.py'.

## Quickstart

Example of launch on Linux, Python 3.5:

```bash
$ pip install -r requirements.txt # alternatively try pip3

$ export FLASK_DEBUG=1 # use to show '+' chars instead of 'No-Break Space'

$ export FLASK_DEBUG=0 # use to exit debug mode

$ python3 server.py # 'ctrl + C' to stop server
```

Open page [http://localhost:5000](http://localhost:5000) in browser.

Paste this broken text with functionality description into the top text area and submit:
```
<p>    Replacement of 'quotes'    .
In the right places - replace hyphens with dashes !
Replacement of hyphens with short dashes in 999-333-888;
Associating 888977 with subsequent words with 'No-Break Space'  ,
   Removing extra    spaces and line breaks  .  
Linking unions and any words of 1-2 characters followed by words .  </p>
```
In the bottom text area the following result should appear:

```
<p>Replacement of «quotes». In the right places — replace hyphens with dashes! Replacement of hyphens with short dashes in 999–333–888; Associating 888977 with subsequent words with «No-Break Space», Removing extra spaces and line breaks. Linking unions and any words of 1–2 characters followed by words.</p>
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

