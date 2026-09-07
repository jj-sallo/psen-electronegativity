import sys

from PySide6.QtWidgets import QApplication

from canvas_bridge import CanvasBridge
from element_bridge import ElementBridge
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    canvas_bridge = CanvasBridge(
        atoms=["O", "H", "H"],
        bonds=[(0, 1), (0, 2)],  # kind is derived from Pauling EN, not hand-specified
    )
    element_bridge = ElementBridge()

    window = MainWindow(canvas_bridge, element_bridge)
    window.show()

    sys.exit(app.exec())
