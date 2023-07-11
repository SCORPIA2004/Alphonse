import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
from ui_TodoList import Ui_MainWindow
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        todos = ["Finish writing the report", "Buy groceries", "Schedule a dentist appointment", "Pay bills", "Call John regarding the project", "Clean the garage", "Research vacation destinations", "Attend the team meeting at 2 PM", "Read the new book", "Start a workout routine"]

        for todo in todos:
            # self.ui.listWidget.addItem(todo)
            item = QListWidgetItem(todo)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.ui.todoList.addItem(item)
        self.ui.pushButton.clicked.connect(self.toggleAll)

    def toggleAll(self):
        for todo in self.ui.todoList.findItems("", Qt.MatchContains):
            if todo.checkState() == Qt.Checked:
                todo.setCheckState(Qt.Unchecked)
            else:
                todo.setCheckState(Qt.Checked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())