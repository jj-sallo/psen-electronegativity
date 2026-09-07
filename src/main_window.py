from PySide6.QtWidgets import QMainWindow, QDockWidget
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtCore import QUrl, Qt
from canvas_container import CanvasContainer
from canvas_bridge import CanvasBridge
from element_bridge import ElementBridge
from bond_bridge import BondBridge
from atom_picker_window import AtomPickerWindow

class MainWindow(QMainWindow):
    def __init__(self, canvas_bridge: CanvasBridge, element_bridge: ElementBridge) -> None:
        super().__init__()
        self.setWindowTitle("Molecule Bond Polarity Classifier")
        self.resize(1000, 700)

        self.canvas_bridge: CanvasBridge = canvas_bridge
        self.element_bridge: ElementBridge = element_bridge
        self.bond_bridge: BondBridge = BondBridge(canvas_bridge.graph)

        self.canvas_container = CanvasContainer(canvas_bridge)
        self.setCentralWidget(self.canvas_container)
        self.canvas_container.fab.clicked.connect(self.show_atom_picker)

        self.picker_window: AtomPickerWindow | None = None
        element_bridge.atomAdded.connect(self.add_atom_from_picker)

        self.bond_table_widget = QQuickWidget()
        self.bond_table_widget.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        self.bond_table_widget.rootContext().setContextProperty("bondBridge", self.bond_bridge)
        self.bond_table_widget.setSource(QUrl.fromLocalFile("src/bond_info.qml"))

        dock = QDockWidget("Bonds", self)
        dock.setWidget(self.bond_table_widget)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

    def show_atom_picker(self) -> None:
        if self.picker_window is None:
            self.picker_window = AtomPickerWindow(self.element_bridge, self)
        fab_global_pos = self.canvas_container.fab.mapToGlobal(
            self.canvas_container.fab.rect().topRight()
        )
        self.picker_window.move(fab_global_pos.x() + 10, fab_global_pos.y() - self.picker_window.height())
        self.picker_window.show()
        self.picker_window.raise_()

    def add_atom_from_picker(self, symbol: str) -> None:
        self.canvas_bridge.graph.add_atom(symbol)
        self.bond_bridge.notify_changed()