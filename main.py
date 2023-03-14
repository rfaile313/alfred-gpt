#!/usr/bin/env python3

from datetime import datetime
import subprocess
import requests
import secrets
import json
import sys

DEBUG=False
CONFIG_PATH="/path/to/your/config.json"
ENDPOINT = "https://api.openai.com/v1/completions"

HELP = '''
Help info goes here :)
'''

if len(sys.argv) < 2:
    print(HELP)
    exit(1)
else:
    prompt = sys.argv[1]

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

def gen_uuid():
    # 8 character uuid
    uuid = secrets.token_hex(4)
    return uuid

def get_current_date():
    now = datetime.now()
    date_str = now.strftime('%m-%d-%y')
    return date_str


headers = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {config['API_KEY']}"
        }

data = {
        "model" : config['MODEL'],
        "prompt" : f"{prompt}",
        "temperature" : config['TEMPERATURE'],
        "max_tokens" : config['MAX_TOKENS']
        }

r = requests.post(ENDPOINT, headers=headers, json=data)

if (r.status_code != 200):
    print("Something went wrong")
    print(r.json())

response = r.json()

choice = response['choices'][0]['text']

HTML = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GPT3-Response</title>
    <style>
        #centered {
            margin: auto;
            width: 800px;
            font-size: 20px;
            font-family: courier, courier new, serif;
            border-style: solid;
        }

        #copyMe {
            margin: auto;
            width: 800px;
            height: 50px;
            cursor: pointer;
            font-size: 30px;
            font-family: font-family: Verdana, sans-serif;
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
</head>

<body>


    <div id="centered">
        <button id="copyMe" onclick="copyText()">🗒️ Copy</button>
        <pre id="myCode"> %s </pre>
    </div>

</body>
<script>
    const myCode = document.getElementById('myCode');
    hljs.highlightElement(myCode);
    function copyText() {
        var textToCopy = myCode.innerText;
        var textArea = document.createElement("textarea");
        textArea.value = textToCopy;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand("copy");
        textArea.remove();
    }
</script>

</html>
'''

final_html = HTML % choice

file_name = f"/path/to/the/directory/that/holds/main.py/response_{get_current_date()}_{gen_uuid()}.html"

with open(f"{file_name}", "w") as file:
    file.write(final_html)

command = f"open {file_name}"

subprocess.run(command, shell=True)
