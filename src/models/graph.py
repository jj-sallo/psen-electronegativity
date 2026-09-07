import numpy as np

import datatypes as dt
from bond_logic import classify_bond, electronegativity_diff

# Colors keyed on the exact strings classify_bond() returns — this is the
# only place bond color is decided, so canvas rendering and the bond table
# can never disagree about what a bond "is."
BOND_COLORS: dict[dt.BondType, str] = {
    "Covalent": "#2ecc71",
    "Polar covalent": "#f39c12",
    "Ionic": "#e74c3c",
    "N/A": "#999999",
}


class Graph:
    def __init__(self, atoms: list[dt.Atom], bonds: list[tuple[int, int]]) -> None:
        self.atoms: list[dt.Atom] = atoms
        n: int = len(atoms)
        self.pos: np.ndarray = np.random.uniform(-1, 1, size=(n, 2)) * 100 + np.array([200, 200])
        self.vel: np.ndarray = np.zeros((n, 2))
        self.pinned: set[int] = set()  # node indices currently being dragged
        self.edges: list[dt.Bond] = [self._make_edge(a1, a2) for a1, a2 in bonds]

    def _make_edge(self, a1: int, a2: int) -> dt.Bond:
        """Single place an edge's classification is computed, so 'kind' can
        never drift from what bond_logic would say given the same atoms."""
        atom_a: dt.Atom = self.atoms[a1]
        atom_b: dt.Atom = self.atoms[a2]
        delta_en: float | None = electronegativity_diff(atom_a, atom_b)
        kind: dt.BondType = classify_bond(delta_en)
        return {"a1": a1, "a2": a2, "kind": kind}

    def add_bond(self, a1: int, a2: int) -> None:
        self.edges.append(self._make_edge(a1, a2))

    def add_atom(self, symbol: dt.Atom, spawn_center: tuple[float, float] = (250.0, 250.0)) -> None:
        self.atoms.append(symbol)
        new_pos: np.ndarray = np.random.uniform(-1, 1, size=(1, 2)) * 50 + np.array(spawn_center)
        self.pos = np.vstack([self.pos, new_pos])
        self.vel = np.vstack([self.vel, np.zeros((1, 2))])

    def step(self, width: float, height: float, radius: float = 18) -> None:
        n = len(self.pos)
        forces = np.zeros((n, 2))

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                delta: np.ndarray = self.pos[i] - self.pos[j]
                dist = np.linalg.norm(delta) + 1e-3
                forces[i] += (delta / dist) * (2000 / dist**2)

        rest_length, stiffness = 120, 0.05
        for edge in self.edges:
            a1, a2 = edge["a1"], edge["a2"]
            delta = self.pos[a2] - self.pos[a1]
            dist = np.linalg.norm(delta) + 1e-3
            f = stiffness * (dist - rest_length) * (delta / dist)
            forces[a1] += f
            forces[a2] -= f

        damping = 0.85
        self.vel = (self.vel + forces * 0.02) * damping

        for i in range(n):
            if i in self.pinned:
                self.vel[i] = 0  # dragged nodes ignore physics, position set externally
                continue
            self.pos[i] += self.vel[i]

        self._clamp_bounds(width, height, radius)

    def _clamp_bounds(self, width: float, height: float, radius: float) -> None:
        for i in range(len(self.pos)):
            if self.pos[i][0] < radius:
                self.pos[i][0], self.vel[i][0] = radius, 0
            elif self.pos[i][0] > width - radius:
                self.pos[i][0], self.vel[i][0] = width - radius, 0
            if self.pos[i][1] < radius:
                self.pos[i][1], self.vel[i][1] = radius, 0
            elif self.pos[i][1] > height - radius:
                self.pos[i][1], self.vel[i][1] = height - radius, 0

    def find_node_at(self, x: float, y: float, radius: float = 18) -> int | None:
        """Hit-test — returns index of node under (x, y), or None."""
        for i, (nx, ny) in enumerate(self.pos):
            if np.hypot(nx - x, ny - y) <= radius:
                return i
        return None

    def set_pinned_position(self, i: int, x: float, y: float) -> None:
        self.pos[i] = [x, y]
        self.pinned.add(i)

    def release_pin(self, i: int) -> None:
        self.pinned.discard(i)

    def to_qml_nodes(self) -> list[dt.Node]:
        return [{"label": self.atoms[i], "x": float(x), "y": float(y)}
                for i, (x, y) in enumerate(self.pos)]

    def to_qml_edges(self) -> list[dt.Edge]:
        return [{"x1": float(self.pos[e["a1"]][0]), "y1": float(self.pos[e["a1"]][1]),
                 "x2": float(self.pos[e["a2"]][0]), "y2": float(self.pos[e["a2"]][1]),
                 "color": BOND_COLORS.get(e["kind"], "#999999")}
                for e in self.edges]
