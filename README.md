# alfred-gpt
Alfred GPT lookup 

## Requirements:

`python3` > 3.6

`requests` module (`python3 -m pip install requests`)

## How to use:

1. Clone this repository and double click the "GPT-3 Lookup.alfredworkflow" file to add it to Alfred.

2. **You must add an [API KEY](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)** to config.json:

https://github.com/rfaile313/alfred-gpt/blob/53245728e4087252cab76c555ec4a18153ef1210/config.json#L1-L6

You can also change the model, temperature, or tokens here. Refer to the OpenAI docs for more information.

3. Unfortunately because this is run through alfred, the tool requires absolute paths which are not the same at runtime (meaning trying to find them with tools like python's `os` module will not work).

So you must add these yourself. There are 3 manual paths to change:

https://github.com/rfaile313/alfred-gpt/blob/63942ae471c2adb630de8a1c5f87cb4b42917cd9/main.py#L11

https://github.com/rfaile313/alfred-gpt/blob/1cd0a02a9b2d88aca31c53baae564c7b7189bf16/main.py#L120

And in the Alfred workflow itself: 

<img width="543" alt="Screenshot 2023-03-14 at 12 55 46 PM" src="https://user-images.githubusercontent.com/13829168/225095458-0284b092-4e0e-42b0-ae5f-5410c88ec9cd.png">

<img width="733" alt="Screenshot 2023-03-14 at 12 56 23 PM" src="https://user-images.githubusercontent.com/13829168/225095538-daca57fc-4cf0-4173-97c1-f1839e684da4.png">




