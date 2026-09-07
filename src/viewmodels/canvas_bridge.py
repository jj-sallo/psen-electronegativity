from PySide6.QtCore import QObject, Property, Signal, Slot, QTimer

import models.datatypes as dt
from models.graph import Graph


class CanvasBridge(QObject):
    positionsChanged = Signal()

    def __init__(self, atoms: list[dt.Atom], bonds: list[tuple[int, int]]) -> None:
        super().__init__()
        self.graph: Graph = Graph(atoms, bonds)
        self._width: float = 500   # sane defaults until QML reports real size
        self._height: float = 500

        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)
        self.timer.start(33)

    def _tick(self) -> None:
        self.graph.step(self._width, self._height)
        self.positionsChanged.emit()

    @Slot(float, float)
    def setCanvasSize(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    @Slot(float, float, result=int)
    def hitTest(self, x: float, y: float) -> int:
        node: int | None = self.graph.find_node_at(x, y)
        return node if node is not None else -1

    def get_nodes(self) -> list[dt.Node]:
        return self.graph.to_qml_nodes()

    def get_edges(self) -> list[dt.Edge]:
        return self.graph.to_qml_edges()

    nodes = Property(list, get_nodes, notify=positionsChanged)
    edges = Property(list, get_edges, notify=positionsChanged)
