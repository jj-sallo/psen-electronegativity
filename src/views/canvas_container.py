from PySide6.QtCore import QUrl
from PySide6.QtGui import QResizeEvent
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import  QPushButton, QVBoxLayout, QWidget
from viewmodels.canvas_bridge import CanvasBridge
from pathlib import Path

QML_DIR = Path(__file__).resolve().parent / "qml"


class CanvasContainer(QWidget):
    def __init__(self, canvas_bridge: "CanvasBridge", parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.quick_widget = QQuickWidget(self)
        self.quick_widget.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        self.quick_widget.rootContext().setContextProperty("graphBridge", canvas_bridge)
        self.quick_widget.setSource(QUrl.fromLocalFile(str(QML_DIR / "canvas.qml")))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.quick_widget)

        self.fab = QPushButton("+", self)
        self.fab.setFixedSize(56, 56)
        self.fab.setStyleSheet("""
            QPushButton {
                border-radius: 28px;
                background-color: #3498db;
                color: white;
                font-size: 24px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #2980b9; }
        """)
        self.fab.raise_()

        self._reposition_fab()

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self._reposition_fab()

    def _reposition_fab(self) -> None:
        margin: int = 20
        x: int = self.width() - self.fab.width() - margin
        y: int = self.height() - self.fab.height() - margin
        self.fab.move(x, y)
        self.fab.raise_()