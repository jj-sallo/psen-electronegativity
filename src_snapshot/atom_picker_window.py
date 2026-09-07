from PySide6.QtCore import QUrl, Qt
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout
from element_bridge import ElementBridge

class AtomPickerWindow(QWidget):
    def __init__(self, element_bridge: "ElementBridge", parent: QWidget | None = None) -> None:
        super().__init__(parent, Qt.WindowType.Window)
        self.setWindowTitle("Add Atom")
    
        picker_widget = QQuickWidget(self)
        picker_widget.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        picker_widget.rootContext().setContextProperty("elementBridge", element_bridge)
        picker_widget.setSource(QUrl.fromLocalFile("src/atom_picker.qml"))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(picker_widget)
        self.resize(760, 340)
