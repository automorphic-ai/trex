<h1 align="center">Trex</h1>

<h2 align="center"><em>T</em>ransformer <em>R</em>egular <em>EX</em>pressions</h2>

<!--- <p align="center"><img src="https://media.discordapp.net/attachments/1107132978859085824/1128974288381288523/Screenshot_2023-07-13_050009-transformed.png" width="25%"/></p> -->
<p align="center"><img src="https://s11.gifyu.com/images/Sczlg.gif" width="50%"/></p>

### _Transform unstructured to structured data_

Trex transforms your unstructured to structured data—just specify a regex or context free grammar and we'll intelligently restructure your data so it conforms to that schema.

## Installation

To experiment with Trex, check out the [playground](https://automorphic.ai/playground).

To install the Python client:

```bash
pip install git+https://github.com/automorphic-ai/trex.git
```

If you'd like to self-host this in your own cloud / with your own model, [email us](mailto:founders@automorphic.ai).

## Usage

To use Trex, you'll need an API key, which you can get by signing up for a free account at [automorphic.ai](https://automorphic.ai).

```python
import trex

tx = trex.Trex('<YOUR_AUTOMORPHIC_API_KEY>')
prompt = '''generate a valid json object of the following format:

{
    "name": "string",
    "age": "number",
    "height": "number",
    "pets": pet[]
}

in the above object, name is a string corresponding to the name of the person, age is a number corresponding to the age of the person in inches as an integer, height is a number corresponding to the height of the person, and pets is an array of pets.

where pet is defined as:
{
    "name": "string",
    "species": "string",
    "cost": "number",
    "dob": "string"
}

in the above object name is a string corresponding to the name of the pet, species is a string corresponding to the species of the pet, cost is a number corresponding to the cost of the pet, and dob is a string corresponding to the date of birth of the pet.

given the above, generate a valid json object containing the following data: one human named dave 30 years old 5 foot 8 with a single dog pet named 'trex'. the dog costed $100 and was born on 9/11/2001.
'''

json_schema = {
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
        },
        "pets": {
            "type": "array",
            "items": [{
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "species": {
                        "type": "string"
                    },
                    "cost": {
                        "type": "number"
                    },
                    "dob": {
                        "type": "string"
                    }
                }
            }]
        }
    }
}

print(tx.generate_json(prompt, json_schema=json_schema).response)
# the above produces:
# {
#     "name": "dave",
#     "age": 30,
#     "height": 58,
#     "pets": [
#         {
#             "name": "trex",
#             "species": "dog",
#             "cost": 100,
#             "dob": "2008-10-27"
#         }
#     ]
# }
```

## Roadmap

- [x] Structured JSON generation
- [x] Structured custom CFG generation
- [x] Structured custom regex generation
- [x] SIGNIFICANT speed improvements
- [x] Generation from JSON schema
- [ ] Auto-prompt generation for unstructured ETL
- [ ] More intelligent models

Join our [Discord](https://discord.gg/E8y4NcNeBe) or [email us](mailto:founders@automorphic.ai), if you're interested in or need help using Trex, have ideas, or want to contribute.

Follow us on [Twitter](https://twitter.com/AutomorphicAI) for updates.
