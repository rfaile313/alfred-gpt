#!/usr/bin/env python3

from datetime import datetime
import subprocess
import requests
import secrets
import json
import html
import sys

DEBUG=False
SOURCE_DIR="/path/to/your/dir/for/alfred-gpt"
ENDPOINT = "https://api.openai.com/v1/completions"

HELP = '''
Help info goes here :)
'''

if len(sys.argv) < 2:
    print(HELP)
    exit(1)
else:
    prompt = sys.argv[1]

with open(f"{SOURCE_DIR}/config.json", "r") as file:
    config = json.load(file)

def gen_uuid():
    # 8 character uuid
    return secrets.token_hex(4)

def get_current_date():
    now = datetime.now()
    return now.strftime('%m-%d-%y')

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
    choice = f"Something went wrong, here's the info:<br><br>{r}"
else:
    response = r.json()
    choice = response['choices'][0]['text']

HTML = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GPT3-Response - ''' + str(get_current_date()) + '-' + str(gen_uuid()) +'''</title>
    <link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/monokai-sublime.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <style>
      body {
        font-size: 12px;
        font-family: 'Lato', sans-serif;
      }
      .container {
        margin-top: 1rem;
        margin: auto;
        width: 800px;
        font-size: 1rem;
      }
      pre {
        font-family: 'Lato', sans-serif;
        background-color: #e6f1f5;
        padding: 1.5rem;
        font-size: 1rem;
        word-wrap: break-word;
        white-space: pre-wrap;
        overflow-x: hidden;
        overflow-y: auto;
        margin: 0 auto;
      }
   
      .request {
        font-weight: 800px;
        background-color: #404142;
        padding: 1rem;
      }
      .tokens {
        font-size: 0.9rem;
        color: #5a5a5a;
        text-align: center;
      }
      .copy-wrapper {
        position: relative;
        display: inline-block;
      }
      .copied-notification {
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translate(-50%, 0);
        opacity: 0;
        transition: all 0.5s;
        font-size: 18px;
        font-weight: bold;
        color: #4caf50;
      }
      .copied-notification.show {
        transform: translate(-50%, 20px);
        opacity: 1;
      }
      .nohover:hover {
        background-color: transparent;
      }
      .prompt-text{
        color:whitesmoke;
      }
    </style>
</head>
 <body>
    <div class="container">
      <div class="request">
        <div class="copy-wrapper">
        <button class="pure-button pure-button-primary" onclick="copyText()">
        <strong>🗒️ Copy</strong>
        </button>
        <span class="copied-notification" id="copiedNotification">Copied!</span>
        </div>
      <strong class="pure-button nohover"> Prompt: </strong>
      <span class="prompt-text">''' + data["prompt"] + '''</span>
            </div>

      <pre id="myCode" >
      ''' + html.escape(str(choice), quote="True") + '''
      </pre>
      <div class="tokens">
        Total tokens used: ''' + str(response['usage']['total_tokens']) + '''
      </div>
    </div>
    <script>
    const myCode = document.getElementById('myCode');
    hljs.highlightElement(myCode);
    function copyText() {
        var textToCopy = myCode.innerText;
        var textArea = document.createElement("textarea");
        textArea.value = textToCopy;
        document.body.appendChild(textArea);
        textArea.select();
        copySuccessful = document.execCommand("copy");
        textArea.remove();
        if (copySuccessful) showCopiedNotification();
}
function showCopiedNotification() {
    var notification = document.getElementById("copiedNotification");
    notification.classList.add("show");
    setTimeout(() => {
        notification.classList.remove("show");
    }, 2000); // Remove the 'show' class after 2 seconds (2000 ms)
}
    </script>
  </body>
</html>
'''

file_name = f"{SOURCE_DIR}/response_{get_current_date()}_{gen_uuid()}.html"

with open(f"{file_name}", "w") as file:
    file.write(HTML)

# Open HTML file 
command = f"open {file_name}"
subprocess.run(command, shell=True)


