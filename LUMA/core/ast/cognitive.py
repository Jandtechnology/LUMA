from ast import Expression
from dataclasses import dataclass
from typing import List, Dict, Union

@dataclass
class CognitiveNode:
    name: str
    properties: List['Property']
    methods: List['Method']

@dataclass
class Property:
    name: str
    type: str
    constraints: List[str]

@dataclass
class Method:
    name: str
    return_type: str
    body: List['Expression']

@dataclass
class EmotionExpression:
    emotion_type: str
    parameters: Dict[str, Union[float, str]]
    target: str