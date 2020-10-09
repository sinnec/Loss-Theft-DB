import os
import os.path
import docx
import shutil

class WordCreator():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    @staticmethod
    def filename_formatter(filename):
        puncts = {'ά': 'α', 'έ': 'ε', 'ή': 'η', 'ί': 'ι', 'ό': 'ο', 'ύ': 'υ', 'ώ': 'ω'}
        name_cap = ''
        for c in filename.lower():
            char = c
            for t in puncts.keys():
                if c in t:
                    char = puncts[c]
            name_cap += char
        return name_cap.upper()

    def __init__(self, main):
        self.main = main

    def create_doc(self):
        self.name_cap = WordCreator.filename_formatter(self.main.name)
        self.filename = self.main.surname + ' ' + self.name_cap + '.doc'
        self.doc = docx.Document()
        self.title = f'{self.main.reason} του {self.main.id_number} δελτίου ταυτότητας{self.other_docs_title} με στοιχεία: {self.main.surname} {self.main.name}.'

        self.doc.add_paragraph(self.title)
        self.doc.add_paragraph('')
        self.doc.add_paragraph('ΣΧΕΤ.: α)  Η 8200/0 – 469448 από 5-10-2014 εγκύκλιος διαταγή.')
        self.doc.add_paragraph(f'            β) Το {self.main.protocol_num}{self.from_prot_date}{self.main.protocol_date_string} έγγραφο του {self.office_type_text} {self.main.office_article} {self.main.office_name}.')
        self.doc.add_paragraph('')
        self.doc.add_paragraph(f'  Σας διαβιβάζουμε το ανωτέρω (β) σχετικό και παρακαλούμε όπως προβείτε στην άμεση ακύρωση του εν θέματι δελτίου ταυτότητας, λόγω {self.reason_text} του, καταχωρώντας τις προβλεπόμενες μεταβολές στην κεντρική εφαρμογή ταυτοτήτων σύμφωνα με την ανωτέρω (α) εγκύκλιο.')
        self.doc.add_paragraph(self.other_docs_par)
        self.doc.save(self.filename)
        shutil.move(self.filename, self.desktop)

    def create_text_variables(self):
        if self.main.reason == 'Απώλεια':
            self.reason_text = 'απώλειάς'
        elif self.main.reason == 'Κλοπή':
            self.reason_text = 'κλοπής'
        else:
            self.reason_text = 'κατάσχεσής'

        if self.main.office_type == 1:
            self.office_type_text = 'Προξενικού Γραφείου της Πρεσβείας της Ελλάδος'
        elif self.main.office_type == 2:
            self.office_type_text = 'Γενικού Προξενείου της Ελλάδος'
        elif self.main.office_type == 3:
            self.office_type_text = 'Επιτίμου Γενικού Προξενείου της Ελλάδος'
        elif self.main.office_type == 4:
            self.office_type_text = 'Άμισθου Γενικού Προξενείου της Ελλάδος'
        else:
            self.office_type_text = 'Κεντρικού Λιμεναρχείου'

        if self.main.other_doc_passport == 0 and self.main.other_doc_driver == 0:
            self.other_docs_title = ''
            self.other_docs_par =''
        elif self.main.other_doc_passport == 1 and self.main.other_doc_driver == 0:
            self.other_docs_title = ' και διαβατηρίου'
            self.other_docs_par = '  Στη Διεύθυνση Διαβατηρίων και Εγγράφων Ασφαλείας/Α.Ε.Α., το παρόν κοινοποιείται για ενημέρωση και τις δικές της περαιτέρω ενέργειες, ως προς την ακύρωση του διαβατηρίου.'
        elif self.main.other_doc_passport == 0 and self.main.other_doc_driver == 1:
            self.other_docs_title = ' και αδείας ικανότητας οδήγησης'
            self.other_docs_par = '  Στη Διεύθυνση Διαβατηρίων και Εγγράφων Ασφαλείας/Α.Ε.Α., το παρόν κοινοποιείται για ενημέρωση και τις τυχόν δικές της ενέργειες.'
        else:
            self.other_docs_title = ', διαβατηρίου και αδείας ικανότητας οδήγησης'
            self.other_docs_par = '  Στη Διεύθυνση Διαβατηρίων και Εγγράφων Ασφαλείας/Α.Ε.Α., το παρόν κοινοποιείται για ενημέρωση και τις τυχόν δικές της ενέργειες.'
        
        if self.main.protocol_date:
            self.from_prot_date = ' από '
        else:
            self.from_prot_date = ''

        self.create_doc()