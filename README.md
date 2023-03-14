# alfred-gpt
Alfred GPT lookup 

## Requirements:

`python3` > 3.6
`requests` module (`python3 -m pip install requests`)

## How to use:

1. Clone this repository and double click the "GPT-3 Lookup.alfredworkflow" file to add it to Alfred.

2. **You must add an API KEY** to config.json:

```
{
	"API_KEY" : "YOUR_API_KEY_GOES_HERE",
	"MODEL" : "text-davinci-003",
	"TEMPERATURE" : 0.0,
	"MAX_TOKENS" : 1000
}
```
You can also change the model, temperature, or tokens here. Refer to the OpenAI docs for more information.

3. Unfortunately because this is run through alfred, the tool requires absolute paths which are not the same at runtime (meaning trying to find them with tools like python's `os` module will not work).

So you must add these yourself. There are 3 manual paths to change:

https://github.com/rfaile313/alfred-gpt/blob/63942ae471c2adb630de8a1c5f87cb4b42917cd9/main.py#L11

https://github.com/rfaile313/alfred-gpt/blob/63942ae471c2adb630de8a1c5f87cb4b42917cd9/main.py#L120

And in the Alfred workflow itself: 

<img width="543" alt="Screenshot 2023-03-14 at 12 55 46 PM" src="https://user-images.githubusercontent.com/13829168/225095458-0284b092-4e0e-42b0-ae5f-5410c88ec9cd.png">

<img width="733" alt="Screenshot 2023-03-14 at 12 56 23 PM" src="https://user-images.githubusercontent.com/13829168/225095538-daca57fc-4cf0-4173-97c1-f1839e684da4.png">




