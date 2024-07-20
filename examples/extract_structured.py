"""For when you want to extract structured data from a text generation, say by GPT 3.5 or 4."""

import json

import trex

tx = trex.Trex('<YOUR AUTOMORPHIC API KEY HERE>')

json_schema_extraction = {
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "age": {
          "type": "number"
        },
        "height": {
          "type": "number"
        }
      },
    },
  ]
}
prompt = '''Below is the output from another language model. Extract the text from the output that is in the format of a valid json array.

    Here is a valid JSON array with 3 people, each having properties for name, age, and height:

```json
[
{
  "name": "Alice",
  "age": 28,
  "height": 165
},
{
  "name": "Bob",
  "age": 35,
  "height": 180
},
{
  "name": "Charlie",
  "age": 42,
  "height": 175
}
]
```'''
print(json.dumps(tx.generate_json(prompt, json_schema_extraction).response, indent=2))