from PySide import QtCore, QtGui
import os

class NukeHotKeys(QtGui.QWidget):
    def __init__(self):
        super(NukeHotKeys, self).__init__()
        self.initUI()
        
    def initUI(self): 

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(All_PanesTab(self), "All Panes")
        tabWidget.addTab(Properties_PanelsTab(self), "Properties Panels")
        tabWidget.addTab(Node_GraphTab(self), "Node Graph")
        tabWidget.addTab(ViewersTab(self), "Viewers")
        tabWidget.addTab(TriD_ViewersTab(self), "3D Viewers")
        tabWidget.addTab(Curve_EditorTab(self), "Curve Editor")
        tabWidget.addTab(RotoPaintTab(self), "RotoPaint")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 650, 500)
        self.setWindowTitle("NUKE hotkeys")
        self.show()


class All_PanesTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(All_PanesTab, self).__init__(parent)

        applicationsListBox = QtGui.QListWidget()
        Hotkeys_All = []
        
        fo = open(os.path.abspath('plugins/n_hotkeys/all_panels.txt'), "r")
        for line in fo.readlines():
            line = line.replace('\n','')
            Hotkeys_All.append(line)
        fo.close()

        applicationsListBox.insertItems(0, Hotkeys_All)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(applicationsListBox)
        self.setLayout(layout)

class Properties_PanelsTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(Properties_PanelsTab, self).__init__(parent)

        applicationsListBox = QtGui.QListWidget()
        Hotkeys_All = []
        
        fo = open(os.path.abspath('plugins/n_hotkeys/properties_panels.txt'), "r")
        for line in fo.readlines():
            line = line.replace('\n','')
            Hotkeys_All.append(line)
        fo.close()

        applicationsListBox.insertItems(0, Hotkeys_All)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(applicationsListBox)
        self.setLayout(layout)

class Node_GraphTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(Node_GraphTab, self).__init__(parent)

        applicationsListBox = QtGui.QListWidget()
        Hotkeys_All = []
        
        fo = open(os.path.abspath('plugins/n_hotkeys/node_graph.txt'), "r")
        for line in fo.readlines():
            line = line.replace('\n','')
            Hotkeys_All.append(line)
        fo.close()

        applicationsListBox.insertItems(0, Hotkeys_All)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(applicationsListBox)
        self.setLayout(layout)

class ViewersTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(ViewersTab, self).__init__(parent)

        applicationsListBox = QtGui.QListWidget()
        Hotkeys_All = []
        
        fo = open(os.path.abspath('plugins/n_hotkeys/viewers.txt'), "r")
        for line in fo.readlines():
            line = line.replace('\n','')
            Hotkeys_All.append(line)
        fo.close()

        applicationsListBox.insertItems(0, Hotkeys_All)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(applicationsListBox)
        self.setLayout(layout)

class TriD_ViewersTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(TriD_ViewersTab, self).__init__(parent)

        applicationsListBox = QtGui.QListWidget()
        Hotkeys_All = []
        
        fo = open(os.path.abspath('plugins/n_hotkeys/tridviewers.txt'), "r")
        for line in fo.readlines():
            line = line.replace('\n','')
            Hotkeys_All.append(line)
        fo.close()

        applicationsListBox.insertItems(0, Hotkeys_All)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(applicationsListBox)
        self.setLayout(layout)

class Curve_EditorTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(Curve_EditorTab, self).__init__(parent)

        applicationsListBox = QtGui.QListWidget()
        Hotkeys_All = []
        
        fo = open(os.path.abspath('plugins/n_hotkeys/curve_editor.txt'), "r")
        for line in fo.readlines():
            line = line.replace('\n','')
            Hotkeys_All.append(line)
        fo.close()

        applicationsListBox.insertItems(0, Hotkeys_All)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(applicationsListBox)
        self.setLayout(layout)

class RotoPaintTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(RotoPaintTab, self).__init__(parent)

        applicationsListBox = QtGui.QListWidget()
        Hotkeys_All = []
        
        fo = open(os.path.abspath('plugins/n_hotkeys/rotopaint.txt'), "r")
        for line in fo.readlines():
            line = line.replace('\n','')
            Hotkeys_All.append(line)
        fo.close()

        applicationsListBox.insertItems(0, Hotkeys_All)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(applicationsListBox)
        self.setLayout(layout)
