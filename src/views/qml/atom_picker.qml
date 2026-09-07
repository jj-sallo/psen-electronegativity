import QtQuick 2.15


Item {
    id: root
    anchors.fill: parent

    readonly property int columns: 18
    readonly property int totalRows: 9
    readonly property real gapHeight: 14

    // Cell size driven by available width first
    readonly property real cellSizeByWidth: width / columns
    readonly property real naturalGridHeight: totalRows * cellSizeByWidth + gapHeight

    // If the width-driven height doesn't fit, scale everything down to fit height instead
    readonly property real fitScale: naturalGridHeight > height
        ? height / naturalGridHeight
        : 1.0

    function rowY(row: int, cellSize: real): real {
        return row <= 7
            ? (row - 1) * cellSize
            : (row - 1) * cellSize + gapHeight
    }

    Item {
        id: grid
        width: root.columns * root.cellSizeByWidth
        height: root.naturalGridHeight
        anchors.centerIn: parent
        scale: root.fitScale

        Repeater {
            model: elementBridge.elements

            delegate: Rectangle {
                x: (modelData.col - 1) * root.cellSizeByWidth
                y: root.rowY(modelData.row, root.cellSizeByWidth)
                width: root.cellSizeByWidth - 2
                height: root.cellSizeByWidth - 2
                radius: 4
                color: "#3498db"

                Text {
                    anchors.centerIn: parent
                    text: modelData.symbol
                    color: "white"
                    font.pixelSize: Math.max(8, root.cellSizeByWidth * 0.35)
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: elementBridge.selectAtom(modelData.symbol)
                }
            }
        }
    }
}