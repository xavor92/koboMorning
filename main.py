import sys
from PySide import QtCore
from PySide import QtGui
from PySide.QtDeclarative import QDeclarativeView

app = QtGui.QApplication(sys.argv)

view = QDeclarativeView()

url = QtCore.QUrl('view.qml')

view.setSource(url)
view.show()

app.exec_()
sys.exit()
