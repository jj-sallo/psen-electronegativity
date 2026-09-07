import QtQuick 2.15

Item {
    id: root
    width: 400
    height: header.height + rowsColumn.height

    readonly property real colWidth: width / 5

    Row {
        id: header
        width: parent.width
        height: 28

        Repeater {
            model: ["Atom A", "Atom B", "ΔEN", "Type", "% Ionic"]
            delegate: Text {
                width: root.colWidth
                text: modelData
                font.bold: true
                horizontalAlignment: Text.AlignHCenter
            }
        }
    }

    Column {
        id: rowsColumn
        anchors.top: header.bottom
        width: parent.width

        Repeater {
            model: bondBridge.rows

            delegate: Row {
                width: root.colWidth * 5
                height: 26

                Text { width: root.colWidth; text: modelData.atomA; horizontalAlignment: Text.AlignHCenter }
                Text { width: root.colWidth; text: modelData.atomB; horizontalAlignment: Text.AlignHCenter }
                Text { width: root.colWidth; text: modelData.deltaEn; horizontalAlignment: Text.AlignHCenter }
                Text { width: root.colWidth; text: modelData.classification; horizontalAlignment: Text.AlignHCenter }
                Text { width: root.colWidth; text: modelData.ionicPct; horizontalAlignment: Text.AlignHCenter }
            }
        }
    }
}