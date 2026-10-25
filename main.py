# Import sadaļa
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
# Galvenā loga klase
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Loga nosaukums un izmērs
        self.setWindowTitle("MiniTask")
        self.resize(500, 400)

        # Galvenā datu struktūra
        self.tasks = []          # <- sākotnējā vērtība
        self.load_tasks()
        self.visible_task_indices = []

        
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

        # Meklēšana
        self.search_input = QLineEdit()
        
        self.search_input.setPlaceholderText(
            "Meklēt uzdevumu..."
        )
        
        # Prioritātes filtrs        
        self.priority_filter = QComboBox()

        self.priority_filter.addItems([
            "Visas",
            "Zema",
            "Normāla",
            "Augsta"
        ])
        
        # Poga
        self.add_button = QPushButton("Pievienot")

        # Izkārtojumi
        search_layout = QHBoxLayout()
        
        # Meklēšanas lauks
        search_layout.addWidget(self.search_input)
        # Prioritātes filtrs
        search_layout.addWidget(self.priority_filter)
        # Uzdevumu saraksts
        self.task_list = QListWidget()

        # Ievades lauka izkārtojums
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.priority_combo)
        input_layout.addWidget(self.add_button)

        # Galvenais izkārtojums
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.task_list)
        
        # Apstiprināšanas poga
        self.complete_button = QPushButton("Pabeigt uzdevumu")
        main_layout.addWidget(self.complete_button)
        
        # Rediģēšanas un dzēšanas pogas
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
        self.search_input.textChanged.connect(self.refresh_task_list)
        self.priority_filter.currentTextChanged.connect(self.refresh_task_list)

        # Atjauno uzdevumu sarakstu
        self.refresh_task_list()

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
        
        # Pievieno datiem
        self.tasks.append(task)
        # Atjauno UI
        self.refresh_task_list()
        # Saglabā JSON
        self.save_tasks()
        # Attīra ievades lauku
        self.task_input.clear()
        # Atjauno prioritātes izvēlni uz noklusējuma vērtību
        self.priority_combo.setCurrentText(
            "Normāla"
        )

    # Pabeidz uzdevumu
    def complete_task(self):
        source_index = self.get_selected_source_index()

        if source_index is None:
            return

        self.tasks[source_index]["done"] = True
        self.save_tasks()
        self.refresh_task_list()

    # Rediģē uzdevumu
    def edit_task(self):
        source_index = self.get_selected_source_index()

        if source_index is None:
            return

        current_text = self.tasks[source_index]["text"]

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
            self.tasks[source_index]["text"] = new_text.strip()
            self.tasks[source_index]["priority"] = priority
            self.save_tasks()
            self.refresh_task_list()

    # Dzēš uzdevumu
    def delete_task(self):
        source_index = self.get_selected_source_index()

        if source_index is None:
            return

        self.tasks.pop(source_index)
        self.save_tasks()
        self.refresh_task_list()
    
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
    
    # Meklēšanas funkcija
    def refresh_task_list(self):
        search_text = self.search_input.text().strip().lower()
        
        selected_priority = (
            self.priority_filter.currentText()
        )

        visible_tasks = []
        self.task_list.clear()
        self.visible_task_indices = []

        for index, task in enumerate(self.tasks):

            matches_search = (
                search_text in task["text"].lower()
            )

            matches_priority = (
                selected_priority == "Visas"
                or task["priority"] == selected_priority
            )

            if matches_search and matches_priority:
                visible_tasks.append(
                    (index, task)
                )

        # KĀRTOŠANA PĒC CIKLA

        visible_tasks = sorted(
            visible_tasks,
            key=lambda item:
            item[1]["text"].lower()
        )

        self.visible_task_indices = [
            index
            for index, task
            in visible_tasks
        ]

        self.task_list.clear()

        for index, task in visible_tasks:

            if task["done"]:
                prefix = "[x] "
            else:
                prefix = "[ ] "

            display_text = (
                prefix +
                "[" + task["priority"] + "] " +
                task["text"]
            )

            self.task_list.addItem(display_text)
    
    def get_selected_source_index(self):
        row = self.task_list.currentRow()

        if row < 0:
            return None

        if row >= len(self.visible_task_indices):
            return None

        return self.visible_task_indices[row]
    
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
