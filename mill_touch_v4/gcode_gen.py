# Smart G code thingy
import linuxcnc

def preambleAdd(parent):
    parent.gcodeListWidget.addItem("; G code generated by the JT's G code wizard")
    parent.gcodeListWidget.addItem(parent.gcodePreambleLine.text())

def gcodeAppend(parent):
    if parent.drillOpChkBox.isChecked():
        parent.gcodeListWidget.addItem('; Drill Op')
        if parent.drillRPMLbl.text():
            parent.gcodeListWidget.addItem('M3 S{}'.format(parent.drillRPMLbl.text()))
        if parent.drillFeedLbl.text():
            parent.gcodeListWidget.addItem('F{}'.format(parent.drillFeedLbl.text()))
        if parent.coordListWidget.count() > 0: # toss out an error if not
            for i in range(parent.coordListWidget.count()):
                coordinates = parent.coordListWidget.item(i).text()
                zDepth = parent.drillDepthLbl.text()
                zClear = parent.drillRetractLbl.text()
                if i == 0:
                    parent.gcodeListWidget.addItem('G81 {} Z{} R{}'.format(coordinates, zDepth, zClear))
                else:
                    parent.gcodeListWidget.addItem('{}'.format(coordinates))



def postambleAppend(parent):
    parent.gcodeListWidget.addItem('M2')

def gcodeLoad(parent):
    emcCommand = linuxcnc.command()
    print(parent.gcodeListWidget.item(0).text())
    gcode = []
    with open('/tmp/qtpyvcp.ngc','w') as f:
        for i in range(parent.gcodeListWidget.count()):
            gcode.append(parent.gcodeListWidget.item(i).text())
        f.write('\n'.join(gcode))
    emcCommand.program_open('/tmp/qtpyvcp.ngc')

def clearGcode(parent):
    parent.gcodeListWidget.clear()
