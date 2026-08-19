import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

# ==============================================================================
# GALVENĀ LOGA KLASE (MAIN WINDOW CLASS)
# ==============================================================================
class MainWindow(QMainWindow):
    """
    Galvenā lietotnes grafiskās saskarnes klase.
    Manto no PySide6.QtWidgets.QMainWindow.
    """
    def __init__(self):
        super().__init__()

        # Loga virsraksta un izmēru konfigurācija
        self.setWindowTitle("MiniTask")
        self.resize(500, 300)

        # Centrālais logrīks - Pagaidu marķieris pirmajam prototipam
        label = QLabel("Tas tika izdarīts")
        
        # Pievieno marķieri kā galveno loga satura elementu
        self.setCentralWidget(label)


# ==============================================================================
# PROGRAMMAS GALVENĀ PALAIŠANAS SADAĻA (ENTRY POINT)
# ==============================================================================
if __name__ == "__main__":
    # Izveido aplikācijas objektu un nodod sistēmas argumentus
    app = QApplication(sys.argv)

    # Inicializē un parāda galveno logu
    window = MainWindow()
    window.show()

    # Palaiž Qt notikumu ciklu (event loop) un nodrošina korektu iziešanu
    sys.exit(app.exec())