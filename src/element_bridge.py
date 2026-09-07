from PySide6.QtCore import QObject, Property, Signal, Slot
from constants.ELEMENTS import ELEMENTS
from typing import TypedDict

class Element(TypedDict):
    symbol: str
    name: str
    row: int
    col: int
    en: float  # -1 if not available

class ElementBridge(QObject):
    atomAdded = Signal(str)  # emits the chosen symbol

    def get_elements(self) -> list[Element]:
        return [
            {"symbol": sym, "name": name, "row": row, "col": col,
             "en": en if en is not None else -1}
            for sym, name, row, col, en in ELEMENTS
        ]

    elements = Property(list, get_elements, constant=True)

    @Slot(str)
    def selectAtom(self, symbol: str):
        self.atomAdded.emit(symbol)
