from PyQt4 import QtGui, QtCore

class Scoreboard(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.awayLabel = QtGui.QLabel(self.tr("Away team"))
        self.awayLabel.setObjectName("awayLabel")

        self.awayScoreLabel = QtGui.QLabel(self.tr("0"))
        self.awayScoreLabel.setObjectName("awayScoreLabel")

        self.homeLabel = QtGui.QLabel(self.tr("Home team"))
        self.homeLabel.setObjectName("homeLabel")

        self.homeScoreLabel = QtGui.QLabel(self.tr("10"))
        self.homeScoreLabel.setObjectName("homeScoreLabel")

        self.dateLabel = QtGui.QLabel(self.tr("Jan 1, 1900"))
        self.dateLabel.setObjectName("dateLabel")

        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.homeScoreLabel, 0, 0)
        layout.addWidget(self.homeLabel, 1, 0)
        layout.addWidget(self.awayScoreLabel, 0, 1)
        layout.addWidget(self.awayLabel, 1, 1)
        layout.addWidget(self.dateLabel, 2, 0)

    def homeScore(self):
        return self.homeScoreLabel.text()

    def setHomeScore(self, score):
        self.homeScoreLabel.setText(score)

if __name__ == "__main__":

    import sys
    from PyQt4.QtGui import QApplication

    app = QApplication(sys.argv)
    widget = Scoreboard()
    widget.show()
    sys.exit(app.exec_())


