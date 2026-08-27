import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MiniTask")
        self.resize(500, 400)

        # Ievades lauks
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Ievadi jaunu uzdevumu...")

        # Poga
        self.add_button = QPushButton("Pievienot")

        # Uzdevumu saraksts
        self.task_list = QListWidget()

        # Izkārtojums: ievades lauks + poga
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        # Galvenais izkārtojums
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)

        self.setLayout(main_layout)

        # Savienojam pogu ar metodi
        self.add_button.clicked.connect(self.add_task)

    def add_task(self):
        task_text = self.task_input.text().strip()

        # Tukšas ievades pārbaude
        if not task_text:
            return

        # Pievienojam sarakstam
        self.task_list.addItem(task_text)

        # Attīrām ievades lauku
        self.task_input.clear()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
