import sqlite3


class Amorces():
    def __init__(self):
        self.id_amorce = None
        self.nom_amorce = None
        self.orientation = None
        self.sequence = None
        self.taille_sequence = None
        self.pourcentage_gc = None
        self.temperature_hybridation = None

    def __repr__(self):
        return "<Amorce %s>" % self.nom_amorce

    def __str__(self):
        return self.nom_amorce

    def __eq__(self, other):
        return self.id_amorce == other.id_amorce

    # Constructeur

    def setId_amorce(self, id_amorce):
        self.id_amorce = id_amorce

    def setNom_amorce(self, nom_amorce):
        self.nom_amorce = nom_amorce

    def setOrientation(self, orientation):
        self.orientation = orientation

    def setSequence(self, sequence):
        self.sequence = sequence

    def setTaille_sequence(self, taille_sequence):
        self.taille_sequence = taille_sequence

    def setPourcentage_gc(self, pourcentage_gc):
        self.pourcentage_gc = pourcentage_gc

    def setTemperature_hybridation(self, temperature_hybridation):
        self.temperature_hybridation = temperature_hybridation

    # Getters

    def getId_amorce(self):
        return self.id_amorce

    def getNom_amorce(self):
        return self.nom_amorce

    def getOrientation(self):
        return self.orientation

    def getSequence(self):
        return self.sequence

    def getTaille_sequence(self):
        return self.taille_sequence

    def getPourcentage_gc(self):
        return self.pourcentage_gc

    def getTemperature_hybridation(self):
        return self.temperature_hybridation

    def create_amorce(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = "INSERT INTO amorces (nom_amorce, orientation, sequence, taille_sequence, pourcentage_gc, temperature_hybridation) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(request, (
            self.nom_amorce, self.orientation, self.sequence, self.taille_sequence, self.pourcentage_gc,
            self.temperature_hybridation))
        conn.commit()
        conn.close()

    def update_amorce(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = "UPDATE amorces SET nom_amorce = ?, orientation = ?, sequence = ?, taille_sequence = ?, pourcentage_gc = ?, temperature_hybridation = ? WHERE id_amorce = ?"
        cursor.execute(request, (
            self.nom_amorce, self.orientation, self.sequence, self.taille_sequence, self.pourcentage_gc,
            self.temperature_hybridation, self.id_amorce))
        conn.commit()
        conn.close()

    def delete_amorce(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = "DELETE FROM amorces WHERE id_amorce = ?"
        cursor.execute(request, (self.id_amorce,))
        conn.commit()
        conn.close()

    def get_amorce(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = "SELECT * FROM amorces WHERE id_amorce = ?"
        cursor.execute(request, (self.id_amorce,))
        result = cursor.fetchone()
        conn.close()
        return result

    def get_all_amorces(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = "SELECT * FROM amorces"
        cursor.execute(request)
        result = cursor.fetchall()
        conn.close()
        liste_amorces = []
        for row in result:
            primer = Amorces()
            primer.setId_amorce(row[0])
            primer.setNom_amorce(row[1])
            primer.setOrientation(row[2])
            primer.setSequence(row[3])
            primer.setTaille_sequence(row[4])
            primer.setPourcentage_gc(row[5])
            primer.setTemperature_hybridation(row[6])
            liste_amorces.append(primer)
        return liste_amorces


class Couple():
    def __init__(self):
        self.id_couple = None
        self.nom_couple =  None
        self.id_amorce_1 = None
        self.id_amorce_2 = None
        self.taille_amplicon = None
        self.programme_pcr = None
        self.regions = None
        self.nameTableCouple = "couple"

    def __repr__(self):
        return "<Couple %s>" % self.id_couple

    def __str__(self):
        return self.id_couple

    def __eq__(self, other):
        return self.id_couple == other.id_couple

    # Constructeur

    def setId_couple(self, id_couple):
        self.id_couple = id_couple

    def setNom_couple(self, nom_couple):
        self.nom_couple = nom_couple

    def setId_amorce_1(self, id_amorce_1):
        self.id_amorce_1 = id_amorce_1

    def setId_amorce_2(self, id_amorce_2):
        self.id_amorce_2 = id_amorce_2

    def setTaille_amplicon(self, taille_amplicon):
        self.taille_amplicon = taille_amplicon

    def setProgramme_pcr(self, programme_pcr):
        self.programme_pcr = programme_pcr

    def setRegions(self, regions):
        self.regions = regions

    # Getters

    def getId_couple(self):
        return self.id_couple

    def getNom_couple(self):
        return self.nom_couple

    def getId_amorce_1(self):
        return self.id_amorce_1

    def getId_amorce_2(self):
        return self.id_amorce_2

    def getTaille_amplicon(self):
        return self.taille_amplicon

    def getProgramme_pcr(self):
        return self.programme_pcr

    def getRegions(self):
        return self.regions

    def create_couple(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = f"INSERT INTO {self.nameTableCouple} (nom_couple, amorce_couple_1, amorce_couple_2, Taille_fragment, programme_pcr, region) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(request, (
            self.nom_couple, self.id_amorce_1, self.id_amorce_2, self.taille_amplicon, self.programme_pcr,self.regions))
        conn.commit()
        conn.close()

    def update_couple(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = f"UPDATE {self.nameTableCouple} SET nom_couple = ?, amorce_couple_1 = ?, amorce_couple_2 = ?, Taille_fragment = ?, programme_pcr = ?, region = ? WHERE id_couple = ?"
        cursor.execute(request, (
            self.nom_couple, self.id_amorce_1, self.id_amorce_2, self.taille_amplicon, self.programme_pcr,
            self.regions, self.id_couple))
        conn.commit()
        conn.close()

    def delete_couple(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = f"DELETE FROM {self.nameTableCouple} WHERE id_couple = ?"
        cursor.execute(request, (self.id_couple,))
        conn.commit()
        conn.close()

    def get_couple(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = f"SELECT * FROM {self.nameTableCouple} WHERE id_couple = ?"
        cursor.execute(request, (self.id_couple,))
        result = cursor.fetchone()
        conn.close()
        return result

    def get_all_couples(self):
        conn = sqlite3.connect('amorces_ngs.db')
        cursor = conn.cursor()
        request = f"SELECT * FROM {self.nameTableCouple}"
        cursor.execute(request)
        result = cursor.fetchall()
        conn.close()
        liste_couples = []
        for row in result:
            couple = Couple()
            couple.setId_couple(row[0])
            couple.setNom_couple(row[1])
            couple.setId_amorce_1(row[2])
            couple.setId_amorce_2(row[3])
            couple.setTaille_amplicon(row[4])
            couple.setProgramme_pcr(row[5])
            couple.setRegions(row[6])
            liste_couples.append(couple)
        return liste_couples
