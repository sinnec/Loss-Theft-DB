import os
import os.path
import sqlite3 as lite
from tkinter import messagebox
from entry import Entry
from helper_methods import latin_to_greek, datetime_formatter

class Database():
    app_date_str = "%d/%m/%Y"
    data_date_str = "%Y-%m-%d"
    data_full_str = "%Y-%m-%d %H:%M:%S"

    def __init__(self, main):
        self.main = main
        self.db_file = 'database'
        self.db = self.db_file + '.sqlite'
        if not os.path.isfile(self.db):
            self.create_database()

    def create_database(self):
        if os.path.isfile('Create table commands.sql'):
            with open('Create table commands.sql') as f:
                sql = f.read()
                sql_commands = sql.split(';')
                conn = lite.connect(self.db)
                with conn:
                    curs = conn.cursor()
                    for command in sql_commands:
                        curs.execute(command+';')
        return False

    def save_to_database(self):
        sql = f'INSERT INTO entries VALUES (?,?,?,?,?,?,?,?,?,?,?,?);'
        try:
            con = lite.connect(self.db)
            with con:
                cur = con.cursor()
                cur.execute(sql, (self.main.id_number, self.main.surname, self.main.name, self.main.reason, self.main.office_article, self.main.office_type, self.main.office_name, self.main.protocol_num,\
                     self.main.protocol_date, self.main.other_doc_passport, self.main.other_doc_driver, self.main.timestamp))
                cur.execute('COMMIT;')
            return True
        except Exception as e:
            print(e)
            return False

    def create_office_tup(self, office_type):
        self.office_type = office_type
        if os.path.isfile(self.db):
            try:
                con = lite.connect(self.db)
                with con:
                    cur = con.cursor()
                    sql = f'SELECT DISTINCT office_name FROM entries WHERE office_type="{self.office_type}" ORDER BY office_name ASC;'
                    cur.execute(sql)
                    self.office_list = []
                    for result in cur.fetchall():
                        self.office_list.append(result[0])
                    self.main.office_name.config(values=tuple(self.office_list))
                    self.main.office_name.current(0)
            except Exception as e:
                self.office_list = ['']
                print(e)
        self.retrieve_num_date()

    def create_office_search_tup(self, reason=0):
        self.office_list = []
        if os.path.isfile(self.db):
            try:
                con = lite.connect(self.db)
                with con:
                    cur = con.cursor()
                    sql = f'SELECT DISTINCT office_name FROM entries ORDER BY office_name ASC;'
                    cur.execute(sql)
                    if reason == 'search':
                        self.office_list = ['']
                    for result in cur.fetchall():
                        self.office_list.append(result[0])
                    return tuple(self.office_list)
            except Exception as e:
                print(e)

    def create_search_results(self):
        Entry.search_results = []
        self.main.clear_tree()
        self.filled_search_fields = []
        for field in [['id_number', self.main.id_number_search], ['surname' ,self.main.surname_search], ['office_name', self.main.office_name_search]]:
            if field[1]:
                self.filled_search_fields.append(field)
        if len(self.filled_search_fields) == 0:
            self.search_criteria = ''
        elif len(self.filled_search_fields) == 1:
            self.search_criteria = f'WHERE {self.filled_search_fields[0][0]} LIKE "%{self.filled_search_fields[0][1]}%" '
        elif len(self.filled_search_fields) == 2:
            self.search_criteria = f'WHERE {self.filled_search_fields[0][0]} LIKE "%{self.filled_search_fields[0][1]}%" AND\
                 {self.filled_search_fields[1][0]} LIKE "%{self.filled_search_fields[1][1]}%" '
        else:
            self.search_criteria = f'WHERE {self.filled_search_fields[0][0]} LIKE "%{self.filled_search_fields[0][1]}%" AND\
             {self.filled_search_fields[1][0]} LIKE "%{self.filled_search_fields[1][1]}%" AND {self.filled_search_fields[2][0]} LIKE "%{self.filled_search_fields[2][1]}%" '
        if self.main.sort_by == 'surname':
            self.des_asc = 'ASC'
        else:
            self.des_asc = 'DESC'
            
        if os.path.isfile(self.db):
            try:
                con = lite.connect(self.db)
                with con:
                    cur = con.cursor()
                    sql = f'SELECT id_number, surname, name, reason, office_name, protocol_num, protocol_date, timestamp FROM entries {self.search_criteria}ORDER BY {self.main.sort_by} {self.des_asc};'
                    cur.execute(sql)
                    results = cur.fetchall()
                    for result in results:
                        try:
                            prot_date = datetime_formatter(result[6], self.data_date_str, self.app_date_str)
                        except:
                            prot_date = ''
                            time_date = ''
                        time_date = datetime_formatter(result[7], self.data_full_str, self.app_date_str)
                        Entry(result[0], result[1], result[2], result[3], result[4], result[5], prot_date, time_date)
                    self.main.tree_insert()
            except Exception as e:
                print(e)

    def retrieve_num_date(self):
        try:
            self.office = self.main.combo_selection
        except:
            self.office = self.office_list[0]
        if os.path.isfile(self.db):
            try:
                con = lite.connect(self.db)
                with con:
                    cur = con.cursor()
                    sql = f'SELECT office_article, protocol_num, protocol_date FROM entries WHERE office_name="{self.office}" ORDER BY timestamp DESC LIMIT 1;'
                    cur.execute(sql)
                    results = cur.fetchall()
                    self.main.office_article = results[0][0]
                    self.protocol_num = results[0][1]
                    self.protocol_date_string = results[0][2]
                    self.protocol_date = datetime_formatter(self.protocol_date_string, self.data_date_str, self.app_date_str)
                    self.main.protocol_num_entry.delete(0, 'end')
                    self.main.protocol_date_entry.delete(0, 'end')
                    self.main.protocol_num_entry.insert(0, self.protocol_num)
                    self.main.protocol_date_entry.insert(0, self.protocol_date)
            except Exception as e:
                print(e)

    def delete_from_database(self):
        result = messagebox.askyesno('Διαγραφή Εγγραφής', f'Έίστε βέβαιοι ότι θέλετε να διαγράψετε την εγγραφή με αριθμό δελτίου {self.main.id_selection};')
        if result == True:
            if os.path.isfile(self.db):
                try:
                    con = lite.connect(self.db)
                    with con:
                        cur = con.cursor()
                        sql = f'DELETE FROM entries WHERE id_number = "{self.main.id_selection}";'
                        cur.execute(sql)
                        cur.execute('COMMIT;')
                        self.create_search_results()
                        self.main.disable_widgets([self.main.delete_button, self.main.edit_button])
                        messagebox.showinfo('Διαγραφή Εγγραφής', f'Επιτυχής διαγραφή εγγραφής!')
                except Exception as e:
                    print(e)

    def update_entry_retrieve(self):
        if os.path.isfile(self.db):
            try:
                con = lite.connect(self.db)
                with con:
                    cur = con.cursor()
                    sql = f'SELECT * FROM entries WHERE id_number = "{self.main.id_selection}";'
                    cur.execute(sql)
                    edit_results = cur.fetchall()
                    self.edit_id_number = edit_results[0][0]
                    self.edit_surname = edit_results[0][1]
                    self.edit_name = edit_results[0][2]
                    self.edit_reason = edit_results[0][3]
                    self.edit_office_name = edit_results[0][6]
                    self.edit_protocol_num = edit_results[0][7]
                    self.edit_protocol_date_string = edit_results[0][8]
                    self.edit_protocol_date = datetime_formatter(self.edit_protocol_date_string, self.data_date_str, self.app_date_str)
                    self.main.edit_entry()
            except Exception as e:
                print(e)

    def insert_update_entry(self):
        self.main.id_number = latin_to_greek(self.main.edit_id_number.get().upper().strip())
        self.main.surname = latin_to_greek(self.main.edit_surname.get().upper().strip())
        self.main.name = latin_to_greek(self.main.edit_name.get().strip())
        self.main.reason = self.main.edit_reason_variable.get()
        self.main.office_name = self.main.edit_office_name_variable.get()
        self.main.protocol_num = self.main.edit_protocol_num.get()
        try:
            self.protocol_date_string = self.main.edit_protocol_date.get()
            self.main.protocol_date = datetime_formatter(self.protocol_date_string, self.app_date_str, self.data_date_str)
        except:
            self.main.protocol_date = self.main.edit_protocol_date.get()
        proceed = self.main.field_check('edit')
        if proceed:
            self.main.edit_window.destroy()
            if os.path.isfile(self.db):
                try:
                    con = lite.connect(self.db)
                    with con:
                        cur = con.cursor()
                        sql = f'SELECT office_type, office_article FROM entries WHERE office_name = "{self.main.office_name}" LIMIT 1'
                        cur.execute(sql)
                        results = cur.fetchall()
                        self.edit_office_type = results[0][0]
                        self.edit_office_article = results[0][1]
                        sql = 'UPDATE entries SET id_number=?, surname=?, name=?, reason=?, office_type =?, office_article =?, office_name=?, protocol_num=?, protocol_date=? WHERE id_number = ?;'
                        cur.execute(sql, (self.main.id_number, self.main.surname, self.main.name, self.main.reason, self.edit_office_type, self.edit_office_article, self.main.office_name, self.main.protocol_num, self.main.protocol_date, self.main.id_selection))
                        cur.execute('COMMIT;')
                        self.create_search_results()
                        self.main.disable_widgets([self.main.delete_button, self.main.edit_button])
                        messagebox.showinfo('Επεξεργασία Εγγραφής', f'Επιτυχής επεξεργασία εγγραφής!')
                except Exception as e:
                    print(e)

    def update_office(self):
        self.old_office_name = self.main.old_office_name_variable.get()
        self.editted_office_entry = self.main.editted_office_name.get().split(' ')
        self.editted_office_article = latin_to_greek(self.editted_office_entry[0])
        self.editted_office_name = latin_to_greek(' '.join(self.editted_office_entry[1:]))
        self.editted_office_type_string = self.main.edit_office_type_variable.get()
        self.editted_office_type = self.main.type_list.index(self.editted_office_type_string)+1
        if os.path.isfile(self.db):
            try:
                con = lite.connect(self.db)
                with con:
                    cur = con.cursor()
                    sql = 'UPDATE entries SET office_name=?, office_type=?, office_article=? WHERE office_name =?;'
                    cur.execute(sql, (self.editted_office_name, self.editted_office_type, self.editted_office_article, self.old_office_name))
                    cur.execute('COMMIT;')
                    self.main.edit_office_window.destroy()
                    messagebox.showinfo('Επεξεργασία Αρχής', f'Επιτυχής επεξεργασία Αρχής!')
            except Exception as e:
                print(e)