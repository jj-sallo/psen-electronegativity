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

# Single source of truth for bond classification strings — must match
# bond_logic.classify_bond()'s return values exactly, since Graph derives
# an edge's "kind" from that function rather than accepting it as input.
BondType = Literal["Covalent", "Polar covalent", "Ionic", "N/A"]

class Bond(TypedDict):
    kind: BondType
    a1: int
    a2: int

Atom = str
