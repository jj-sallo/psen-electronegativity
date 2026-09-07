from typing import TypedDict, Literal

class Node(TypedDict):
    label: str
    x: float
    y: float

class Edge(TypedDict):
    color: str
    x1: float
    y1: float
    x2: float
    y2: float

BondType = Literal["covalent", "polar", "ionic"]

class Bond(TypedDict):
    kind: BondType
    a1: int
    a2: int

Atom = str