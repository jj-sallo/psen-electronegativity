from models.elements import ELEMENTS
from models.datatypes import BondType
import math

PAULING_EN: dict[str, float | None] = {symbol: en for symbol, _, _, _, en in ELEMENTS}

def electronegativity_diff(atom_a: str, atom_b: str) -> float | None:
    en_a: float | None = PAULING_EN.get(atom_a)
    en_b: float | None = PAULING_EN.get(atom_b)
    if en_a is None or en_b is None:
        return None
    return abs(en_a - en_b)


def classify_bond(delta_en: float | None) -> BondType:
    if delta_en is None:
        return "N/A"
    if delta_en < 0.5:
        return "Covalent"
    if delta_en <= 1.7:
        return "Polar covalent"
    return "Ionic"

def percent_ionic_character(delta_en: float | None) -> float | None:
    """Pauling's empirical approximation: %ionic ≈ (1 - e^(-0.25·ΔEN²)) × 100"""
    if delta_en is None:
        return None
    return (1 - math.exp(-0.25 * delta_en**2)) * 100
