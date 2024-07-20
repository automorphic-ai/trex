# -*- coding: utf-8 -*-
import json
import os
from dataclasses import dataclass

import requests

from trex.exceptions import InvalidAPIKey, InvalidConfigError, InvalidJSONError


@dataclass
class TrexResponse:
    response: str | dict
    tokens: int

class Trex:
    """Trex API client."""

    BASE_URL = "https://api.automorphic.ai/trex"
    JSON_GRAMMAR = r"""
                    ?start: object

                    ?value: object
                        | array
                        | string
                        | SIGNED_NUMBER      -> number
                        | "true"             -> true
                        | "false"            -> false
                        | "null"             -> null

                    array  : "[" [value ("," value)*] "]"
                    object : "{" [pair ("," pair)*] "}"
                    pair   : string ":" value

                    string : ESCAPED_STRING

                    %import common.ESCAPED_STRING
                    %import common.SIGNED_NUMBER
                    %import common.WS

                    %ignore WS
                """

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("AUTOMORPHIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "AUTOMORPHIC_API_KEY must be set in the environment or passed into the client."
            )
        
    def generate(self, prompt: str, max_tokens: int = 512) -> TrexResponse:
        """
        Generate a completion without any restrictions.

        :param prompt: The prompt given to the model to generate the completion.
        :param max_tokens: The maximum number of tokens to generate. Defaults to 512.
        """
        response = requests.post(
            f"{Trex.BASE_URL}/generate",
            headers={"X-API-Key": self.api_key},
            json={"prompt": prompt, "max_tokens": max_tokens},
        )
        response_json = response.json()
        if response.status_code != 201:
            if response.status_code == 401:
                raise InvalidAPIKey(f'Invalid API Key: {self.api_key}')
            else:
                response.raise_for_status()
        return TrexResponse(response=response_json['response'], tokens=response_json['tokens'])
        
    def generate_cfg(self, prompt: str, cfg: str, language: str = None, max_tokens: int = 512) -> TrexResponse:
        """
        Generate data to conform to a [lark](https://github.com/lark-parser/lark) context free grammar.

        :param prompt: The prompt / instructions / guidelines to follow when generating the data.
        :param cfg: The context free grammar to generate data from (specified as a lark DSL).
        :param max_tokens: The maximum number of tokens to generate. Defaults to 512.
        """
        response = requests.post(
            f"{Trex.BASE_URL}/generate",
            headers={"X-API-Key": self.api_key},
            json={"prompt": prompt, "structured_method": "CFG", "structured_config": cfg, "language": language, "max_tokens": max_tokens},
        )
        response_json = response.json()
        if response.status_code != 201:
            message = response_json['detail']
            if 'Invalid' in message:
                raise InvalidConfigError(message)
            elif response.status_code == 401:
                raise InvalidAPIKey(f'Invalid API Key: {self.api_key}')
            else:
                response.raise_for_status()
        return TrexResponse(response=response_json['response'], tokens=response_json['tokens'])


    def generate_json(self, prompt: str, json_schema: dict = None, max_tokens: int = 512) -> TrexResponse:
        """
        Generate data in valid JSON.

        :param json_schema: The JSON schema to generate data from. If not specified, the data will be in JSON format but not conform to any particular schema.
        :param prompt: The prompt / instructions / guidelines to follow when generating the data.
        :param max_tokens: The maximum number of tokens to generate. Defaults to 512.
        """
        if json_schema is None:
            response = requests.post(
                f"{Trex.BASE_URL}/generate",
                headers={"X-API-Key": self.api_key},
                json={"prompt": prompt, "structured_method": "CFG", "structured_config": Trex.JSON_GRAMMAR, "language": 'json', "max_tokens": max_tokens},
            )
        else:
            response = requests.post(
                f"{Trex.BASE_URL}/generate",
                headers={"X-API-Key": self.api_key},
                json={"prompt": prompt, "structured_method": "JSON", "structured_config": json_schema, "language": 'json', "max_tokens": max_tokens},
            )
        response_json = response.json()
        if response.status_code != 201:
            message = response_json['detail']
            if 'Invalid' in message:
                raise InvalidConfigError(message)
            elif response.status_code == 401:
                raise InvalidAPIKey(f'Invalid API Key: {self.api_key}')
            elif response.status_code == 400:
                raise 
            else:
                response.raise_for_status()
        try:
            response_json['response'] = json.loads(response_json['response'])
        except:
            raise InvalidJSONError(response_json['response'])
        return TrexResponse(response=response_json['response'], tokens=response_json['tokens'])
    
    def generate_regex(self, prompt: str, regex: str, max_tokens: int = 512) -> TrexResponse:
        """
        Generate data to conform to a particular regex.

        :param prompt: The prompt / instructions / guidelines to follow when generating the data.
        :param max_tokens: The maximum number of tokens to generate. Defaults to 512.
        """
        response = requests.post(
            f"{Trex.BASE_URL}/generate",
            headers={"X-API-Key": self.api_key},
            json={"prompt": prompt, "structured_method": "REGEX", "structured_config": regex, "max_tokens": max_tokens},
        )
        response_json = response.json()
        if response.status_code != 201:
            message = response_json['detail']
            if 'Invalid' in message:
                raise InvalidConfigError(message)
            elif response.status_code == 401:
                raise InvalidAPIKey(f'Invalid API Key: {self.api_key}')
            else:
                response.raise_for_status()
        return TrexResponse(response=response_json['response'], tokens=response_json['tokens'])