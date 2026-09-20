import json
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

        # Galvenā datu struktūra
        self.tasks = self.load_tasks()
        
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
        self.complete_button = QPushButton("Pabeigt uzdevumu")
        main_layout.addWidget(self.complete_button)

        self.setLayout(main_layout)

        # Savienojam pogu ar metodi
        self.add_button.clicked.connect(self.add_task)
        self.complete_button.clicked.connect(self.complete_task)

        # Atjaunojam UI no datiem
        self.update_ui()

    def add_task(self):
        task_text = self.task_input.text().strip()

        # Tukšas ievades pārbaude
        if not task_text:
            return

        task = {
        "text": task_text,
        "done": False
        }
        
        # 1. Pievienojam datiem
        self.tasks.append(task)

        # 2. Atjaunojam UI
        self.update_ui()

        # 3. Saglabājam JSON
        self.save_tasks()

        # 4. Attīrām ievades lauku
        self.task_input.clear()
    
    def complete_task(self):
        row = self.task_list.currentRow()

        if row < 0:
            return

        self.tasks[row]["done"] = True
        self.save_tasks()
        self.update_ui()

    
    def update_ui(self):
        self.task_list.clear()

        for task in self.tasks:
            if task["done"]:
                prefix = "[x] "
            else:
                prefix = "[ ] "

            self.task_list.addItem(prefix + task["text"])

    def save_tasks(self):
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def load_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
