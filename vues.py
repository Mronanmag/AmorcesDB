from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow, QFormLayout, QLineEdit, QPushButton, QWidget, \
    QListWidget, QGridLayout, QComboBox
from models import Amorces, Couple

NAME_TABLE_AMORCES = "amorces"
NAME_TABLE_COUPLE = "couple"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PrimerDB")
        self.resize(800, 600)
        self.setCentralWidget(FormChoiceTable())


class FormChoiceTable(QWidget):
    def __init__(self):
        super().__init__()
        self.layout()
        self.connect()

    def widgets(self):
        # Widget avec un champs pour sélectionner la table
        self.table_choice = QComboBox()
        self.table_choice.addItem(NAME_TABLE_AMORCES)
        self.table_choice.addItem(NAME_TABLE_COUPLE)
        self.button_choice = QPushButton("Choisir")

    def layout(self):
        self.widgets()
        self.layout = QFormLayout()
        self.layout.addRow("Choix de la table", self.table_choice)
        self.layout.addRow("", self.button_choice)
        self.setLayout(self.layout)

    def connect(self):
        self.button_choice.clicked.connect(self.choice_table)

    def choice_table(self):
        if self.table_choice.currentText() == NAME_TABLE_AMORCES:
            self.amorce_widget = AmorceWidget()
            self.amorce_widget.show()
        elif self.table_choice.currentText() == NAME_TABLE_COUPLE:
            self.couple_widget = CoupleWidget()
            self.couple_widget.show()


class TableAmorces(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(7)
        self.setHorizontalHeaderLabels(
            ["Id amorce", "Nom amorce", "Orientation", "Sequence", "Taille sequence", "Pourcentage GC",
             "Temperature hybridation"])
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 100)
        self.setColumnWidth(3, 100)
        self.setColumnWidth(4, 100)
        self.setColumnWidth(5, 100)
        self.setColumnWidth(6, 100)
        self.setRowCount(0)
        self.setAlternatingRowColors(True)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)

    def load_amorces(self):
        amorces_list = Amorces()
        amorces_list = amorces_list.get_all_amorces()
        self.setRowCount(len(amorces_list))
        for i, amorce in enumerate(amorces_list):
            self.setItem(i, 0, QTableWidgetItem(str(amorce.getId_amorce())))
            self.setItem(i, 1, QTableWidgetItem(amorce.getNom_amorce()))
            self.setItem(i, 2, QTableWidgetItem(amorce.getOrientation()))
            self.setItem(i, 3, QTableWidgetItem(amorce.getSequence()))
            self.setItem(i, 4, QTableWidgetItem(str(amorce.getTaille_sequence())))
            self.setItem(i, 5, QTableWidgetItem(str(amorce.getPourcentage_gc())))
            self.setItem(i, 6, QTableWidgetItem(str(amorce.getTemperature_hybridation())))
        self.resizeColumnsToContents()
        self.resizeRowsToContents()


class TableCouple(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(7)
        self.setHorizontalHeaderLabels(
            ["Id couple", "Nom amorce", "Id amorce 1", "Id amorce 2", "Taille amplicon", "Programme PCR", "Regions"])
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 100)
        self.setColumnWidth(3, 100)
        self.setColumnWidth(4, 100)
        self.setColumnWidth(5, 100)
        self.setColumnWidth(6, 100)
        self.setRowCount(0)
        self.setAlternatingRowColors(True)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)

    def load_couple(self):
        couple_list = Couple()
        couple_list = couple_list.get_all_couples()
        self.setRowCount(len(couple_list))
        for i, couple in enumerate(couple_list):
            self.setItem(i, 0, QTableWidgetItem(str(couple.getId_couple())))
            self.setItem(i, 1, QTableWidgetItem(couple.getNom_couple()))
            self.setItem(i, 2, QTableWidgetItem(str(couple.getId_amorce_1())))
            self.setItem(i, 3, QTableWidgetItem(str(couple.getId_amorce_2())))
            self.setItem(i, 4, QTableWidgetItem(str(couple.getTaille_amplicon())))
            self.setItem(i, 5, QTableWidgetItem(str(couple.getProgramme_pcr())))
            print(couple.getRegions())
            self.setItem(i, 6, QTableWidgetItem(str(couple.getRegions())))
        self.resizeColumnsToContents()
        self.resizeRowsToContents()


class FormAddWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.widgets()
        self.connect()

    def widgets(self):
        self.button_add_amorce = QPushButton("Ajouter")
        self.button_add_couple = QPushButton("Ajouter")
        self.button_cancel = QPushButton("Annuler")
        self.lb_nom = QLineEdit()
        self.l_orientation = QComboBox()
        self.l_orientation.addItem("forward")
        self.l_orientation.addItem("reverse")
        self.lb_sequence = QLineEdit()
        self.lb_temperature_hybridation = QLineEdit()
        self.lb_id_couple = QLineEdit()
        self.lb_nom_couple = QLineEdit()
        self.lb_id_amorce_1 = QLineEdit()
        self.lb_id_amorce_2 = QLineEdit()
        self.lb_taille_amplicon = QLineEdit()
        self.lb_programme_pcr = QLineEdit()
        self.lb_regions = QLineEdit()

    def layout_amorce(self):
        self.layout = QFormLayout()
        self.layout.addRow("Nom amorce", self.lb_nom)
        self.layout.addRow("Orientation", self.l_orientation)
        self.layout.addRow("Sequence", self.lb_sequence)
        self.layout.addRow("Temperature hybridation", self.lb_temperature_hybridation)
        self.layout.addRow("", self.button_add_amorce)
        self.layout.addRow("", self.button_cancel)
        self.setLayout(self.layout)

    def layout_couple(self):
        self.layout = QFormLayout()
        self.layout.addRow("Id couple", self.lb_id_couple)
        self.layout.addRow("Nom couple", self.lb_nom_couple)
        self.layout.addRow("Id amorce 1", self.lb_id_amorce_1)
        self.layout.addRow("Id amorce 2", self.lb_id_amorce_2)
        self.layout.addRow("Taille amplicon", self.lb_taille_amplicon)
        self.layout.addRow("Programme PCR", self.lb_programme_pcr)
        self.layout.addRow("Regions", self.lb_regions)
        self.layout.addRow("", self.button_add_couple)
        self.layout.addRow("", self.button_cancel)
        self.setLayout(self.layout)

    def get_amorce(self):
        return None, self.lb_nom.text(), self.l_orientation.currentText(), self.lb_sequence.text(), str(len(self.lb_sequence.text())), self.calculate_gc(self.lb_sequence.text()), self.lb_temperature_hybridation.text()
    def get_couple(self):
        return self.lb_id_couple.text(), self.lb_nom_couple.text(), self.lb_id_amorce_1.text(), self.lb_id_amorce_2.text(), self.lb_taille_amplicon.text(), self.lb_programme_pcr.text(), self.lb_regions.text()

    def calculate_gc(self,sequence):
        count_gc = 0
        for nucleotide in sequence:
            if nucleotide == "G" or nucleotide == "C":
                count_gc += 1
        return count_gc/len(sequence)*100
    def connect(self):
        self.button_add_amorce.clicked.connect(self.addAmorce)
        self.button_add_couple.clicked.connect(self.addCouple)
        self.button_cancel.clicked.connect(self.cancel)

    def addAmorce(self):
        amorce_info = self.get_amorce()
        primer = Amorces()
        primer.setId_amorce(amorce_info[0])
        primer.setNom_amorce(amorce_info[1])
        primer.setOrientation(amorce_info[2])
        primer.setSequence(amorce_info[3])
        primer.setTaille_sequence(amorce_info[4])
        primer.setPourcentage_gc(amorce_info[5])
        primer.setTemperature_hybridation(amorce_info[6])
        primer.create_amorce()
        self.close()

    def addCouple(self):
        couple_info = self.get_couple()
        primers_couple = Couple()
        primers_couple.setId_couple(couple_info[0])
        primers_couple.setNom_couple(couple_info[1])
        primers_couple.setId_amorce_1(couple_info[2])
        primers_couple.setId_amorce_2(couple_info[3])
        primers_couple.setTaille_amplicon(couple_info[4])
        primers_couple.setProgramme_pcr(couple_info[5])
        primers_couple.setRegions(couple_info[6])
        primers_couple.create_couple()
        self.close()

    def cancel(self):
        self.close()


class FormUpdateWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.widgets()
        self.connect()

    def widgets(self):
        self.button_update_amorces = QPushButton("Modifier")
        self.button_update_couple = QPushButton("Modifier")
        self.button_cancel = QPushButton("Annuler")
        self.lb_id = QLineEdit()
        self.lb_id.setReadOnly(True)
        self.lb_nom = QLineEdit()
        self.lb_orientation = QLineEdit()
        self.lb_sequence = QLineEdit()
        self.lb_taille_sequence = QLineEdit()
        self.lb_pourcentage_gc = QLineEdit()
        self.lb_temperature_hybridation = QLineEdit()
        self.lb_id_couple = QLineEdit()
        self.lb_nom_couple = QLineEdit()
        self.lb_id_amorce_1 = QLineEdit()
        self.lb_id_amorce_2 = QLineEdit()
        self.lb_taille_amplicon = QLineEdit()
        self.lb_programme_pcr = QLineEdit()
        self.lb_regions = QLineEdit()
        self.lb_id_couple.setReadOnly(True)
        self.btn_id_amorce_1 = QPushButton("Forward")
        self.btn_id_amorce_2 = QPushButton("Reverse")

    def layout_amorce(self):
        self.layout = QFormLayout()
        self.layout.addRow("Id amorce", self.lb_id)
        self.layout.addRow("Nom amorce", self.lb_nom)
        self.layout.addRow("Orientation", self.lb_orientation)
        self.layout.addRow("Sequence", self.lb_sequence)
        self.layout.addRow("Taille sequence", self.lb_taille_sequence)
        self.layout.addRow("Pourcentage GC", self.lb_pourcentage_gc)
        self.layout.addRow("Temperature hybridation", self.lb_temperature_hybridation)
        self.layout.addRow("", self.button_update_amorces)
        self.layout.addRow("", self.button_cancel)
        self.setLayout(self.layout)

    def layout_couple(self):
        self.layout = QFormLayout()
        self.layout.addRow("Id couple", self.lb_id_couple)
        self.layout.addRow("Nom couple", self.lb_nom_couple)
        self.layout.addRow("Id amorce 1", self.lb_id_amorce_1)
        self.layout.addRow("Id amorce 2", self.lb_id_amorce_2)
        self.layout.addRow("Taille amplicon", self.lb_taille_amplicon)
        self.layout.addRow("Programme PCR", self.lb_programme_pcr)
        self.layout.addRow("Regions", self.lb_regions)
        self.layout.addRow("", self.button_update_couple)
        self.layout.addRow("", self.button_cancel)
        self.layout.addRow("", self.btn_id_amorce_1)
        self.layout.addRow("", self.btn_id_amorce_2)
        self.setLayout(self.layout)

    def setFormAmorces(self, amorce):
        self.lb_id.setText(str(amorce.getId_amorce()))
        self.lb_nom.setText(amorce.getNom_amorce())
        self.lb_orientation.setText(amorce.getOrientation())
        self.lb_sequence.setText(amorce.getSequence())
        self.lb_taille_sequence.setText(str(amorce.getTaille_sequence()))
        self.lb_pourcentage_gc.setText(str(amorce.getPourcentage_gc()))
        self.lb_temperature_hybridation.setText(str(amorce.getTemperature_hybridation()))

    def setFormCouple(self, couple):
        self.lb_id_couple.setText(str(couple.getId_couple()))
        self.lb_nom_couple.setText(couple.getNom_couple())
        self.lb_id_amorce_1.setText(str(couple.getId_amorce_1()))
        self.lb_id_amorce_2.setText(str(couple.getId_amorce_2()))
        self.lb_taille_amplicon.setText(str(couple.getTaille_amplicon()))
        self.lb_programme_pcr.setText(str(couple.getProgramme_pcr()))
        self.lb_regions.setText(str(couple.getRegions()))

    def get_amorce(self):
        return self.lb_id.text(), self.lb_nom.text(), self.lb_orientation.text(), self.lb_sequence.text(), self.lb_taille_sequence.text(), self.lb_pourcentage_gc.text(), self.lb_temperature_hybridation.text()

    def get_couple(self):
        return self.lb_id_couple.text(), self.lb_nom_couple.text(), self.lb_id_amorce_1.text(), self.lb_id_amorce_2.text(), self.lb_taille_amplicon.text(), self.lb_programme_pcr.text(), self.lb_regions.text()

    def calculate_gc(self,sequence):
        count_gc = 0
        for nucleotide in sequence:
            if nucleotide == "G" or nucleotide == "C":
                count_gc += 1
        return count_gc/len(sequence)*100
    
    def updateAmorce(self):
        amorce_info = self.get_amorce()
        primer = Amorces()
        primer.setId_amorce(amorce_info[0])
        primer.setNom_amorce(amorce_info[1])
        primer.setOrientation(amorce_info[2])
        primer.setSequence(amorce_info[3])
        primer.setTaille_sequence(len(amorce_info[3]))
        primer.setPourcentage_gc(self.calculate_gc(amorce_info[3]))
        primer.setTemperature_hybridation(amorce_info[6])
        primer.update_amorce()
        self.close()

    def updateCouple(self):
        couple_info = self.get_couple()
        primers_couple = Couple()
        primers_couple.setId_couple(couple_info[0])
        primers_couple.setNom_couple(couple_info[1])
        primers_couple.setId_amorce_1(couple_info[2])
        primers_couple.setId_amorce_2(couple_info[3])
        primers_couple.setTaille_amplicon(couple_info[4])
        primers_couple.setProgramme_pcr(couple_info[5])
        primers_couple.setRegions(couple_info[6])
        primers_couple.update_couple()
        self.close()

    def cancel(self):
        self.close()

    def connect(self):
        self.button_update_amorces.clicked.connect(self.updateAmorce)
        self.button_update_couple.clicked.connect(self.updateCouple)
        self.button_cancel.clicked.connect(self.cancel)
        self.btn_id_amorce_1.clicked.connect(self.choose_primer_forward)
        self.btn_id_amorce_2.clicked.connect(self.choose_primer_reverse)

    def choose_primer_forward(self):
        self.primer_found = PrimerFound("forward")
        self.primer_found.load_primer_found()
        self.primer_found.show()

    def choose_primer_reverse(self):
        self.primer_found = PrimerFound("reverse")
        self.primer_found.load_primer_found()

        self.primer_found.show()



class AmorceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout()
        self.connect()

    def widgets(self):
        self.tableAmorce = TableAmorces()
        self.tableAmorce.load_amorces()
        self.buttonAdd = QPushButton("Ajouter")
        self.buttonUpdate = QPushButton("Modifier")
        self.buttonDelete = QPushButton("Supprimer")
        self.buttonCancel = QPushButton("Annuler")
        self.buttonActualiser = QPushButton("Actualiser")

    def layout(self):
        self.widgets()
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.tableAmorce, 0, 0, 1, 5)
        self.main_layout.addWidget(self.buttonAdd, 1, 0)
        self.main_layout.addWidget(self.buttonUpdate, 1, 1)
        self.main_layout.addWidget(self.buttonDelete, 1, 2)
        self.main_layout.addWidget(self.buttonCancel, 1, 3)
        self.main_layout.addWidget(self.buttonActualiser, 1, 4)
        self.setLayout(self.main_layout)

    def connect(self):
        self.buttonAdd.clicked.connect(self.addAmorce)
        self.buttonUpdate.clicked.connect(self.updateAmorce)
        self.buttonDelete.clicked.connect(self.deleteAmorce)
        self.buttonCancel.clicked.connect(self.cancel)
        self.buttonActualiser.clicked.connect(self.tableAmorce.load_amorces)

    def addAmorce(self):
        self.formAdd = FormAddWidget()
        self.formAdd.layout_amorce()
        self.formAdd.show()

    def updateAmorce(self):
        self.formUpdate = FormUpdateWidget()
        self.formUpdate.layout_amorce()
        amorces_modif = Amorces()
        amorces_modif.setId_amorce(self.tableAmorce.item(self.tableAmorce.currentRow(), 0).text())
        amorces_modif.setNom_amorce(self.tableAmorce.item(self.tableAmorce.currentRow(), 1).text())
        amorces_modif.setOrientation(self.tableAmorce.item(self.tableAmorce.currentRow(), 2).text())
        amorces_modif.setSequence(self.tableAmorce.item(self.tableAmorce.currentRow(), 3).text())
        amorces_modif.setTaille_sequence(self.tableAmorce.item(self.tableAmorce.currentRow(), 4).text())
        amorces_modif.setPourcentage_gc(self.tableAmorce.item(self.tableAmorce.currentRow(), 5).text())
        amorces_modif.setTemperature_hybridation(self.tableAmorce.item(self.tableAmorce.currentRow(), 6).text())
        self.formUpdate.setFormAmorces(amorces_modif)
        self.formUpdate.show()

    def deleteAmorce(self):
        amorce_delete = Amorces()
        amorce_delete.setId_amorce(self.tableAmorce.item(self.tableAmorce.currentRow(), 0).text())
        amorce_delete.delete_amorce()
        self.tableAmorce.load_amorces()

    def cancel(self):
        self.close()


class CoupleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout()
        self.connect()

    def widgets(self):
        self.tableCouple = TableCouple()
        self.tableCouple.load_couple()
        self.buttonAdd = QPushButton("Ajouter")
        self.buttonUpdate = QPushButton("Modifier")
        self.buttonDelete = QPushButton("Supprimer")
        self.buttonCancel = QPushButton("Annuler")
        self.buttonActualiser = QPushButton("Actualiser")

    def layout(self):
        self.widgets()
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.tableCouple, 0, 0, 1, 5)
        self.main_layout.addWidget(self.buttonAdd, 1, 0)
        self.main_layout.addWidget(self.buttonUpdate, 1, 1)
        self.main_layout.addWidget(self.buttonDelete, 1, 2)
        self.main_layout.addWidget(self.buttonCancel, 1, 3)
        self.main_layout.addWidget(self.buttonActualiser, 1, 4)
        self.setLayout(self.main_layout)

    def connect(self):
        self.buttonAdd.clicked.connect(self.addCouple)
        self.buttonUpdate.clicked.connect(self.updateCouple)
        self.buttonDelete.clicked.connect(self.deleteCouple)
        self.buttonCancel.clicked.connect(self.cancel)
        self.buttonActualiser.clicked.connect(self.tableCouple.load_couple)


    def addCouple(self):
        self.formAdd = FormAddWidget()
        self.formAdd.layout_couple()
        self.formAdd.show()

    def updateCouple(self):
        self.formUpdate = FormUpdateWidget()
        self.formUpdate.layout_couple()
        self.formUpdate.btn_id_amorce_1.clicked.connect(self.formUpdate.choose_primer_forward)
        self.formUpdate.btn_id_amorce_2.clicked.connect(self.formUpdate.choose_primer_reverse)
        couple_modif = Couple()
        couple_modif.setId_couple(self.tableCouple.item(self.tableCouple.currentRow(), 0).text())
        couple_modif.setNom_couple(self.tableCouple.item(self.tableCouple.currentRow(), 1).text())
        couple_modif.setId_amorce_1(int(self.tableCouple.item(self.tableCouple.currentRow(), 2).text()))
        couple_modif.setId_amorce_2(int(self.tableCouple.item(self.tableCouple.currentRow(), 3).text()))
        couple_modif.setTaille_amplicon(self.tableCouple.item(self.tableCouple.currentRow(), 4).text())
        couple_modif.setProgramme_pcr(self.tableCouple.item(self.tableCouple.currentRow(), 5).text())
        couple_modif.setRegions(self.tableCouple.item(self.tableCouple.currentRow(), 6).text())
        self.formUpdate.setFormCouple(couple_modif)
        self.formUpdate.show()

    def deleteCouple(self):
        couple_delete = Couple()
        couple_delete.setId_couple(self.tableCouple.item(self.tableCouple.currentRow(), 0).text())
        couple_delete.delete_couple()
        self.tableCouple.load_couple()

    def cancel(self):
        self.close()

    def choose_primer_forward(self):
        self.formUpdate.lb_id_amorce_1.setText(self.formUpdate.primer_found.primer)

    def choose_primer_reverse(self):
        self.formUpdate.lb_id_amorce_2.setText(self.formUpdate.primer_found.primer)

class PrimerFound(QWidget) :
    primer = ""
    def __init__(self,sens):
        super().__init__()
        self.sens = sens
        self.layout()
        self.connect()

    def widgets(self):
        self.tablePrimerFound = QTableWidget()
        self.tablePrimerFound.setColumnCount(3)
        self.tablePrimerFound.setHorizontalHeaderLabels(["Id primer", "Primer_name", "Sequence"])
        self.tablePrimerFound.setColumnWidth(0, 100)
        self.tablePrimerFound.setColumnWidth(1, 100)
        self.tablePrimerFound.setColumnWidth(2, 100)
        self.tablePrimerFound.setRowCount(0)
        self.tablePrimerFound.setAlternatingRowColors(True)
        self.tablePrimerFound.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tablePrimerFound.setSelectionBehavior(QTableWidget.SelectRows)
        self.buttonCancel = QPushButton("Quitter")
        self.buttonActualiser = QPushButton("Actualiser")
        self.buttonValider = QPushButton("Choisir")

    def load_primer_found(self):
        all_primers = Amorces()
        liste_primers = all_primers.get_all_amorces()
        if self.sens == "forward" :
            for i, primer in enumerate(liste_primers):
                if primer.getOrientation() == "forward" :
                    self.tablePrimerFound.setItem(i, 0, QTableWidgetItem(str(primer.getId_amorce())))
                    self.tablePrimerFound.setItem(i, 1, QTableWidgetItem(str(primer.getNom_amorce())))
                    self.tablePrimerFound.setItem(i, 2, QTableWidgetItem(str(primer.getSequence())))
        elif self.sens == "reverse" :
            for i, primer in enumerate(liste_primers):
                if primer.getOrientation() == "reverse" :
                    self.tablePrimerFound.setItem(i, 0, QTableWidgetItem(str(primer.getId_amorce())))
                    self.tablePrimerFound.setItem(i, 1, QTableWidgetItem(str(primer.getNom_amorce())))
                    self.tablePrimerFound.setItem(i, 2, QTableWidgetItem(str(primer.getSequence())))
        self.tablePrimerFound.resizeColumnsToContents()
        self.tablePrimerFound.resizeRowsToContents()



    def return_primer_found(self):
        #Emettre un signal avec le primer choisi
        self.primer = self.tablePrimerFound.item(self.tablePrimerFound.currentRow(), 1).text()
        self.close()

    def layout(self):
        self.widgets()
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.tablePrimerFound, 0, 0, 1, 5)
        self.main_layout.addWidget(self.buttonCancel, 1, 0)
        self.main_layout.addWidget(self.buttonActualiser, 1, 1)
        self.main_layout.addWidget(self.buttonValider, 1, 2)
        self.setLayout(self.main_layout)
    def connect(self):
        self.buttonCancel.clicked.connect(self.cancel)
        self.buttonActualiser.clicked.connect(self.load_primer_found)
        self.buttonValider.clicked.connect(self.return_primer_found)

    def cancel(self):
        self.close()
