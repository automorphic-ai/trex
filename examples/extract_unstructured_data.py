"""For when you want to extract structured data from an unstructured description."""

import json

import trex

tx = trex.Trex('<YOUR AUTOMORPHIC API KEY HERE>')
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
      
      given the above, generate a valid json object containing the following data: one human named dave 30 years old 58 inches with a single dog pet named 'trex'. the dog costed $100 and was born on 9/1/2003.'''
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

print(json.dumps(tx.generate_json(prompt, json_schema=json_schema).response, indent=2))