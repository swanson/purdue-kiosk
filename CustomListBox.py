from PyQt4.QtCore import *
from PyQt4.QtGui import *
from random import randint
from flickcharm import *


class CustomListBox(QListView):
    def __init__(self, parent=None):
        QListView.__init__(self, parent)
        self.buildModel()
        self.setModel(self.model)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        #bind event for clicking a row (FML)
        #self.connect(self, SIGNAL("clicked(QModelIndex)"), \
        #    self.clickHandler)
        self.flick = FlickCharm()
        self.flick.activateOn(self)

    def buildModel(self):
        self.model = QStandardItemModel()
        
        #generate background gradient
        grad = QLinearGradient(0,0,0,75)
        grad.setColorAt(0, QColor('gray'))
        grad.setColorAt(1, QColor('black'))

        for n in range(100):                   
            item = QStandardItem("")
            item.setForeground(QColor('gold'))
            item.setBackground(grad)
            item.setSizeHint(QSize(200,50))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont(QString('helvetica'), 20, 75, False))
            item.setEditable(False)
            self.model.appendRow(item)

    def clickHandler(self, event):
        print "You clicked item %i" % event.row()

    def updateModel(self, newModel):
        self.model = newModel
        self.setModel(newModel)
        self.update()

if __name__ == "__main__":
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    widget = CustomListBox()
    widget.show()
    sys.exit(app.exec_())
