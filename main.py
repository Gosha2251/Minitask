import json
import sys
from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QMessageBox,
    QWidget,
    QLineEdit,
    QPushButton,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
    QComboBox
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("MiniTask")
        self.resize(500, 400)

        # Galvenā datu struktūra
        self.tasks = []          # <- sākotnējā vērtība
        self.load_tasks()

        
        # Ievades lauks
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Ievadi jaunu uzdevumu...")
        
        # Prioritātes izvēlne
        self.priority_combo = QComboBox()

        self.priority_combo.addItems([
            "Zema",
            "Normāla",
            "Augsta"
        ])

        self.priority_combo.setCurrentText(
            "Normāla"
        )

        # Poga
        self.add_button = QPushButton("Pievienot")

        # Uzdevumu saraksts
        self.task_list = QListWidget()

        # Izkārtojums: ievades lauks + poga
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.priority_combo)
        input_layout.addWidget(self.add_button)

        # Galvenais izkārtojums
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        
        self.complete_button = QPushButton("Pabeigt uzdevumu")
        main_layout.addWidget(self.complete_button)
        
        self.edit_button = QPushButton("Rediģēt uzdevumu")
        self.delete_button = QPushButton("Dzēst uzdevumu")
        main_layout.addWidget(self.edit_button)
        main_layout.addWidget(self.delete_button)

        self.setLayout(main_layout)

        # Savieno pogu ar metodi
        self.add_button.clicked.connect(self.add_task)
        self.complete_button.clicked.connect(self.complete_task)
        self.edit_button.clicked.connect(self.edit_task)
        self.delete_button.clicked.connect(self.delete_task)

        # Atjauno UI no datiem
        self.update_ui()

    def add_task(self):
        task_text = self.task_input.text().strip()

        # Tukšas ievades pārbaude
        if not task_text:
            return

        task = {
        "text": task_text,
        "done": False,
        "priority": self.priority_combo.currentText()
        }
        
        # 1. Pievieno datiem
        self.tasks.append(task)

        # 2. Atjauno UI
        self.update_ui()

        # 3. Saglabā JSON
        self.save_tasks()

        # 4. Attīra ievades lauku
        self.task_input.clear()
        
        # 5. Atjauno prioritātes izvēlni uz noklusējuma vērtību
        self.priority_combo.setCurrentText(
            "Normāla"
        )
    
    # Pabeidz uzdevumu
    def complete_task(self):
        row = self.task_list.currentRow()

        if row < 0:
            return

        self.tasks[row]["done"] = True
        self.save_tasks()
        self.update_ui()

    # Rediģē uzdevumu
    def edit_task(self):
        row = self.task_list.currentRow()
        if row == -1:
            return

        current_text = self.tasks[row]["text"]

        new_text, ok = QInputDialog.getText(
            self,
            "Rediģēt uzdevumu",
            "Uzdevuma teksts:",
            text=current_text
        )
        
        priority, ok_priority = QInputDialog.getItem(
            self,
            "Prioritāte",
            "Izvēlies prioritāti:",
            ["Zema", "Normāla", "Augsta"],
            1,
            False
        )   

        if ok and ok_priority and new_text.strip():
            self.tasks[row]["text"] = new_text.strip()
            self.tasks[row]["priority"] = priority
            self.save_tasks()
            self.update_ui()

    # Dzēš uzdevumu
    def delete_task(self):
        row = self.task_list.currentRow()
        if row == -1:
            return

        self.tasks.pop(row)
        self.save_tasks()
        self.update_ui()
    
    # Atjaunojam UI no datiem
    def update_ui(self):
        self.task_list.clear()

        for task in self.tasks:
            if task["done"]:
                prefix = "[x] "
            else:
                prefix = "[ ] "

            # Sagatavo tekstu, ko parādīt sarakstā
            display_text = (
                prefix +
                "[" + task["priority"] + "] " +
                task["text"]
            )

            # Pievieno uzdevumu sarakstam
            self.task_list.addItem(display_text)
    
    # Saglabā uzdevumus JSON failā
    def save_tasks(self):
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    # Ielādē uzdevumus no JSON faila
    def load_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                self.tasks = json.load(file)

            for task in self.tasks:
                task.setdefault(
                    "priority",
                    "Normāla"
                )

        except FileNotFoundError:
            self.tasks = []

        except json.JSONDecodeError:
            self.tasks = []
            self.show_corrupted_data_warning()

    # Rāda brīdinājuma logu, ja datu fails ir bojāts
    def show_corrupted_data_warning(self):
        QMessageBox.warning(
            self,
        "Datu ielādes kļūda",
        "Neizdevās nolasīt saglabātos uzdevumus, jo datu fails ir bojāts.\n"
        "Lietotne turpinās darbu ar tukšu uzdevumu sarakstu."
        )



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
