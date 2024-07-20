"""For generating synthetic data from an LLM adhering to a particular schema, in this case generic JSON."""

import json

import trex

tx = trex.Trex('<YOUR AUTOMORHPIC API KEY HERE>')
prompt = '''generate a valid json object containing a single key "humans" with an array with two objects each representing humans. generate 5 different properties each human could have, including strings and numbers.'''
print(json.dumps(tx.generate_json(prompt).response, indent=2))