"""For when you want to use an LLM as a classifier, in the case GPT produces a more verbose output than you want."""

import trex

tx = trex.Trex('<YOUR AUTOMORPHIC API KEY HERE>')

prompt = '''Classify the following branch of science as either under "physics", "chemistry", or "biology":
The study of the structure and function of the nervous system and the brain.'''
regex = '(biology|chemistry|physics)'

print(tx.generate_regex(prompt, regex).response) 
# the above results in "biology", though GPT 3.5 generates:
# The study of the structure and function of the nervous system and the brain is under the branch of science called "biology".