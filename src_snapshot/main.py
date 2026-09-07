import sys

from PySide6.QtWidgets import (
    QApplication,
)

from canvas_bridge import CanvasBridge
from element_bridge import ElementBridge
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    canvas_bridge = CanvasBridge(
        atoms=["O", "H", "H"],
        edges=[
            {"a1": 0, "a2": 1, "kind": "polar"},
            {"a1": 0, "a2": 2, "kind": "polar"},
        ],
    )
    element_bridge = ElementBridge()

    window = MainWindow(canvas_bridge, element_bridge)
    window.show()

    sys.exit(app.exec())
    