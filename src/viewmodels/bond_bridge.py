from PySide6.QtCore import QObject, Property, Signal

from bond_logic import classify_bond, electronegativity_diff, percent_ionic_character
from graph import Graph


class BondBridge(QObject):
    rowsChanged = Signal()

    def __init__(self, graph: Graph) -> None:
        super().__init__()
        self.graph: Graph = graph

    def get_rows(self) -> list[dict[str, str]]:
        rows: list[dict[str, str]] = []
        for edge in self.graph.edges:
            atom_a: str = self.graph.atoms[edge["a1"]]
            atom_b: str = self.graph.atoms[edge["a2"]]
            delta_en: float | None = electronegativity_diff(atom_a, atom_b)
            ionic_pct: float | None = percent_ionic_character(delta_en)
            rows.append({
                "atomA": atom_a,
                "atomB": atom_b,
                "deltaEn": f"{delta_en:.2f}" if delta_en is not None else "N/A",
                "classification": classify_bond(delta_en),
                "ionicPct": f"{ionic_pct:.1f}%" if ionic_pct is not None else "N/A",
            })
        return rows

    rows = Property(list, get_rows, notify=rowsChanged)

    def notify_changed(self) -> None:
        """Call this after any mutation to graph.edges/atoms."""
        self.rowsChanged.emit()