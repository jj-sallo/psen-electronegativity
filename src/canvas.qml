import QtQuick 2.15
import QtQuick.Window 2.15


Canvas {
    id: canvas
    anchors.fill: parent

    Connections {
        target: graphBridge
        function onPositionsChanged() { canvas.requestPaint() }
    }

    onWidthChanged: graphBridge.setCanvasSize(width, height)
    onHeightChanged: graphBridge.setCanvasSize(width, height)

    onPaint: {
        var ctx = getContext("2d")
        ctx.reset(width, height)

        var edges = graphBridge.edges
        for (var e = 0; e < edges.length; e++) {
            var edge = edges[e]
            ctx.strokeStyle = edge.color
            ctx.lineWidth = 3
            ctx.beginPath()
            ctx.moveTo(edge.x1, edge.y1)
            ctx.lineTo(edge.x2, edge.y2)
            ctx.stroke()
        }

        var nodes = graphBridge.nodes
        for (var n = 0; n < nodes.length; n++) {
            var node = nodes[n]
            ctx.fillStyle = "#3498db"
            ctx.beginPath()
            ctx.arc(node.x, node.y, 18, 0, 2 * Math.PI)
            ctx.fill()

            ctx.fillStyle = "white"
            ctx.font = "14px sans-serif"
            ctx.textAlign = "center"
            ctx.textBaseline = "middle"
            ctx.fillText(node.label, node.x, node.y)
        }
    }
}