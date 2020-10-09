import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
import tkcalendar
from datetime import datetime
#from varname import Wrapper
import database
import word
from entry import Entry

class Main():
    office_dict = {1: 'Πρεσβεία', 2: 'Γενικό Προξενείο', 3: 'Επίτιμο Γενικό Προξενείο', 4:'Άμισθο Γενικό Προξενείο', 5:'Κεντρικό Λιμεναρχείο'}

    @staticmethod
    def time_data_to_app(timestring):
        try:
            protocol_date_obj = datetime.strptime(timestring, '%Y-%m-%d %H:%M:%S')
            return protocol_date_obj.strftime("%d/%m/%Y")
        except:
            protocol_date_obj = datetime.strptime(timestring, '%Y-%m-%d')
            return protocol_date_obj.strftime("%d/%m/%Y")

    @staticmethod
    def time_app_to_data(timestring):
        protocol_date_obj = datetime.strptime(timestring, '%d/%m/%Y')
        return protocol_date_obj.strftime("%Y-%m-%d")

    @staticmethod
    def entry_formatter(name):
        eng = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ'
        el = 'αβψδεφγηιξκλμνοπρστθωςχυζΑΒΨΔΕΦΓΗΙΞΚΛΜΝΟΠΡΣΤΘΩςΧΥΖ'
        new_name = ''
        for i in name:
            if i in eng:
                new_name += el[eng.index(i)]
            else:
                new_name += i
        return new_name

    def __init__(self, root):
        self.root = root
        self.root.title("Απώλειες/Κλοπές Δελτίων Αστυνομικής Ταυτότητας Development")
        #self.root.geometry('550x410')
        self.root.resizable(width='false', height='false')

    def create_widgets(self):
        '''Tabs'''
        self.tab_parent = ttk.Notebook(self.root)
        self.main_tab = ttk.Frame(self.tab_parent)
        self.search_tab = ttk.Frame(self.tab_parent)
        #self.statistics_tab = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.main_tab, text='Νέο Έγγραφο')
        self.tab_parent.add(self.search_tab, text='Αναζήτηση')
        #self.tab_parent.add(self.statistics_tab, text='Στατιστικά')
        self.tab_parent.pack(expand=True, fill='both')

        '''Main Tab'''
        self.f1_1 = tk.LabelFrame(self.main_tab, text='Αιτία Ακύρωσης', bg="lightyellow", padx=5, pady=5) #font='"Segoe UI" 12 bold', fg="red")
        self.f1_1.pack(expand=True, fill='both')

        self.reason_variable = tk.StringVar(value='Απώλεια')
        self.loss = tk.Radiobutton(self.f1_1, text='Απώλεια', variable=self.reason_variable, value='Απώλεια', bg='lightyellow', activebackground='lightyellow')
        self.loss.pack(side='left', expand=True)
        self.theft = tk.Radiobutton(self.f1_1, text='Κλοπή', variable=self.reason_variable, value='Κλοπή', bg='lightyellow', activebackground='lightyellow')
        self.theft.pack(side='left', expand=True)
        self.confiscated = tk.Radiobutton(self.f1_1, text='Κατάσχεση', variable=self.reason_variable, value='Κατάσχεση', bg='lightyellow', activebackground='lightyellow') #font='TkDefaultFont 11')
        self.confiscated.pack(side='left', expand=True)

        self.f1_2 = tk.LabelFrame(self.main_tab, text='Στοιχεία Δελτίου', bg="lightyellow", padx=5, pady=5)
        self.f1_2.pack(expand=True, fill='both')
        tk.Label(self.f1_2, text='Αριθμός Δελτίου:', bg="lightyellow").grid(row=0, column=0)
        self.id_number_entry = tk.Entry(self.f1_2)
        self.id_number_entry.grid(row=0, column=1, sticky='we')

        tk.Label(self.f1_2, text='Επώνυμο:', bg="lightyellow").grid(row=2, column=0)
        self.surname_entry = tk.Entry(self.f1_2)
        self.surname_entry.grid(row=2, column=1, sticky='we')

        tk.Label(self.f1_2, text='Όνομα:', bg="lightyellow").grid(row=3, column=0)
        self.name_entry = tk.Entry(self.f1_2)
        self.name_entry.grid(row=3, column=1, sticky='we')
        for col in range(3):
            self.f1_2.grid_columnconfigure(col, weight=1, minsize=183)

        self.f1_3 = tk.LabelFrame(self.main_tab, text='Στοιχεία Εγγράφου', bg="lightyellow", padx=5, pady=5)
        self.f1_3.pack(expand=True, fill='both')
        self.f1_3_1 = tk.Frame(self.f1_3, bg="lightyellow", padx=5, pady=5)
        self.f1_3_1.pack(expand=True, fill='both')
        self.office_variable = tk.IntVar()
        self.embassy = tk.Radiobutton(self.f1_3_1,text=self.office_dict[1], variable=self.office_variable, value=1, bg='lightyellow', activebackground='lightyellow')
        self.embassy.bind('<ButtonRelease-1>', lambda event, office_type=1: data.create_office_tup(office_type))
        self.embassy.pack(side='left', fill='both', expand=True)
        self.gen_con = tk.Radiobutton(self.f1_3_1,text=self.office_dict[2], variable=self.office_variable, value=2, bg='lightyellow', activebackground='lightyellow')
        self.gen_con.pack(side='left', fill='both', expand=True)
        self.gen_con.bind('<ButtonRelease-1>', lambda event, office_type=2: data.create_office_tup(office_type))
        self.hon_gen_con = tk.Radiobutton(self.f1_3_1,text=self.office_dict[3], variable=self.office_variable, value=3, bg='lightyellow', activebackground='lightyellow')
        self.hon_gen_con.pack(side='left', fill='both', expand=True)
        self.hon_gen_con.bind('<ButtonRelease-1>', lambda event, office_type=3: data.create_office_tup(office_type))
        self.np_gen_con = tk.Radiobutton(self.f1_3_1,text=self.office_dict[4], variable=self.office_variable, value=4, bg='lightyellow', activebackground='lightyellow')
        self.np_gen_con.pack(side='left', fill='both', expand=True)
        self.np_gen_con.bind('<ButtonRelease-1>', lambda event, office_type=4: data.create_office_tup(office_type))
        self.np_gen_con = tk.Radiobutton(self.f1_3_1,text=self.office_dict[5], variable=self.office_variable, value=5, bg='lightyellow', activebackground='lightyellow')
        self.np_gen_con.pack(side='left', fill='both', expand=True)
        self.np_gen_con.bind('<ButtonRelease-1>', lambda event, office_type=5: data.create_office_tup(office_type))

        self.f1_3_2 = tk.Frame(self.f1_3, bg="lightyellow", padx=5, pady=5)
        self.f1_3_2.pack(expand=True, fill='both')
        tk.Label(self.f1_3_2, text='Προξενική/Λιμενική Αρχή:', bg="lightyellow").grid(row=0, column=0)
        self.office_name_variable = tk.StringVar()
        self.office_name = ttk.Combobox(self.f1_3_2, textvariable=self.office_name_variable, values=(), state='readonly')
        self.office_name.bind('<<ComboboxSelected>>', self.combobox_selection)
        self.office_name.grid(row=0, column=1, sticky='we')
        tk.Button(self.f1_3_2, text='Νέα Προξενική Αρχή', command=self.new_office).grid(row=0, column=2)

        tk.Label(self.f1_3_2, text='Αριθμός Πρωτοκόλλου:', bg="lightyellow").grid(row=1, column=0)
        self.protocol_num_entry = tk.Entry(self.f1_3_2)
        self.protocol_num_entry.grid(row=1, column=1, sticky='we')

        tk.Label(self.f1_3_2, text='Ημερομηνία Πρωτοκόλλου:', bg="lightyellow").grid(row=2, column=0)
        self.protocol_date_entry = tkcalendar.DateEntry(self.f1_3_2, date_pattern='dd/mm/y', locale='el_GR') #width=12, background='darkblue', foreground='white', borderwidth=2
        self.protocol_date_entry.grid(row=2, column=1, sticky='we')
        self.protocol_date_entry.delete(0, 'end')

        for col in range(3):
            self.f1_3_2.grid_columnconfigure(col, weight=1, minsize=183)

        self.f1_4 = tk.LabelFrame(self.main_tab, text='Άλλα Έγγραφα', bg="lightyellow", padx=5, pady=5)
        self.f1_4.pack(expand=True, fill='both')
        self.other_doc_passport_var = tk.IntVar()
        tk.Checkbutton(self.f1_4, text='Διαβατήριο', bg="lightyellow", activebackground='lightyellow', variable=self.other_doc_passport_var, onvalue=1, offvalue=0).pack(side='left', expand=True, fill='both')
        self.other_doc_driver_var = tk.IntVar()
        tk.Checkbutton(self.f1_4, text='Άδεια Ικανότητας Οδήγησης', bg="lightyellow", activebackground='lightyellow', variable=self.other_doc_driver_var, onvalue=1, offvalue=0).pack(side='left', expand=True, fill='both')

        self.f1_5 = tk.Frame(self.main_tab, bg="lightyellow", padx=5, pady=5)
        self.f1_5.pack(expand=True, fill='both')
        self.new_button = tk.Button(self.f1_5, text='Νέο Έγγραφο', command=self.reset)
        self.create_button = tk.Button(self.f1_5, text='Δημιουργία Εγγράφου', command=self.get_values)
        self.create_button.grid(row=0, column=1, sticky='ns')
        tk.Button(self.f1_5, text='Έξοδος', command=self.root.quit).grid(row=0, column=2, sticky='ns')
        for col in range(3):
            self.f1_5.grid_columnconfigure(col, weight=1, minsize=183)

        '''Search Tab'''
        self.f2 = tk.LabelFrame(self.search_tab, text="Κριτήρια Αναζήτησης", bg="lightyellow", padx=5, pady=5)
        self.f2.pack(expand=True, fill='both')

        tk.Label(self.f2, text='Αριθμός Δελτίου:', bg="lightyellow").grid(row=0, column=0)
        self.id_number_search_entry = tk.Entry(self.f2)
        self.id_number_search_entry.grid(row=0, column=1, sticky='we')

        tk.Label(self.f2, text='Επώνυμο:', bg="lightyellow").grid(row=1, column=0)
        self.surname_search_entry = tk.Entry(self.f2)
        self.surname_search_entry.grid(row=1, column=1, sticky='we')

        tk.Label(self.f2, text='Προξενική/Λιμενική Αρχή:', bg="lightyellow").grid(row=2, column=0)
        self.office_search_tup = data.create_office_search_tup('search')
        self.office_name_search_variable = tk.StringVar()
        self.office_name_search = ttk.Combobox(self.f2, textvariable=self.office_name_search_variable, values=self.office_search_tup, state='readonly')
        self.office_name_search.current(0)
        self.office_name_search.grid(row=2, column=1, sticky='we')
        tk.Button(self.f2, text='Επεξεργασία Αρχών', command=self.edit_office).grid(row=2, column=2)

        for col in range(3):
            self.f2.grid_columnconfigure(col, weight=1, minsize=183)

        self.f3 = tk.LabelFrame(self.search_tab, text="Ταξινόμηση Κατά", bg="lightyellow", padx=5, pady=5)
        self.f3.pack(expand=True, fill='both')

        self.sort_by_variable = tk.StringVar(value='surname')
        self.sort_by_name = tk.Radiobutton(self.f3,text='Επώνυμο', variable=self.sort_by_variable, value='surname', bg='lightyellow', activebackground='lightyellow')
        self.sort_by_name.pack(fill='both', expand=True, side='left')
        self.sort_by_prot_date = tk.Radiobutton(self.f3,text='Ημερομηνία Πρωτοκόλλου', variable=self.sort_by_variable, value='protocol_date', bg='lightyellow', activebackground='lightyellow')
        self.sort_by_prot_date.pack(fill='both', expand=True, side='left')
        self.sort_by_creation_date = tk.Radiobutton(self.f3,text='Ημερομηνία Δημιουργίας', variable=self.sort_by_variable, value='timestamp', bg='lightyellow', activebackground='lightyellow')
        self.sort_by_creation_date.pack(fill='both', expand=True, side='left')

        tk.Button(self.f3, text='Αναζήτηση', command=self.get_search_pars).pack(fill='both', expand=True, side='left')

        self.f4 = tk.LabelFrame(self.search_tab, text="Αποτελέσματα", bg="lightyellow", padx=5, pady=5)
        self.f4.pack(expand=True, fill='both')
        self.tree = ttk.Treeview(self.f4, style='Treeview')
        self.tree["columns"] = tuple(f'#{_i}' for _i in range(1, 8))
        self.column_tup = ('Αρ. Δελτίου', 'Επώνυμο', 'Όνομα', 'Αιτιολογία', 'Προξενική Αρχή', 'Αρ. Πρωτοκόλλου', 'Ημ. Πρωτοκόλλου', 'Ημ. Δημιουργίας')
        self.column_widths = [80, 150, 100, 70, 100, 110, 110, 100]
        for _i in range(len(self.column_tup)):
            self.tree.heading(f"#{_i}", text=self.column_tup[_i], anchor="w")
            self.tree.column(f"#{_i}", width=self.column_widths[_i])
        
        self.sbar = ttk.Scrollbar(self.f4, orient="vertical", command=self.tree.yview)
        self.sbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.sbar.set)
        self.sbar_1 = ttk.Scrollbar(self.f4, orient="horizontal", command=self.tree.xview)
        self.sbar_1.pack(side='bottom', fill='x')
        self.tree.configure(xscrollcommand=self.sbar_1.set)
        self.tree.pack(side='top', fill='both', expand=True)
        self.tree.bind('<<TreeviewSelect>>', self.tree_on_select)
        
        self.f5 = tk.Frame(self.search_tab, bg="lightyellow", padx=5, pady=5)
        self.f5.pack(expand=True, fill='both')
        self.delete_button = ttk.Button(self.f5, text='Διαγραφή', command=data.delete_from_database, state='disabled')
        self.delete_button.pack(side='right', fill='both')
        self.edit_button = ttk.Button(self.f5, text='Επεξεργασία', command=data.update_entry_retrieve, state='disabled')
        self.edit_button.pack(side='right', fill='both')

    def get_values(self):
        self.reason = self.reason_variable.get()
        self.id_number = self.id_number_entry.get().upper().strip()
        self.surname = self.surname_entry.get().upper().strip()
        self.name = self.name_entry.get().strip()
        self.office_type = self.office_variable.get()
        self.office_name = self.office_name_variable.get().strip()
        self.protocol_num = self.protocol_num_entry.get().strip()

        try:
            self.protocol_date_string = self.protocol_date_entry.get()
            self.protocol_date = Main.time_app_to_data(self.protocol_date_string)
        except:
            self.protocol_date = self.protocol_date_entry.get()

        self.other_doc_passport = self.other_doc_passport_var.get()
        self.other_doc_driver = self.other_doc_driver_var.get()
        self.now = datetime.now()
        self.timestamp = self.now.strftime("%Y-%m-%d %H:%M:%S")

        self.field_check('new')

    def get_search_pars(self):
        self.id_number_search = Main.entry_formatter(self.id_number_search_entry.get().upper().strip())
        self.surname_search = Main.entry_formatter(self.surname_search_entry.get().upper().strip())
        self.office_name_search = self.office_name_search_variable.get()
        self.sort_by = self.sort_by_variable.get()
        data.create_search_results()

    def tree_on_select(self, event):
        self.tree_selected = event.widget.selection()
        self.id_selection = self.tree.item(self.tree_selected[0])['text']
        self.enable_widgets([self.delete_button, self.edit_button])

    def field_check(self, reason):
        self.error = False
        self.error_message = ''
        if self.id_number == '':
            self.error = True
            self.error_message += '\n- Δώστε αριθμό δελτίου!'
        elif not ((self.id_number[0].isalpha() and self.id_number[1:].isdecimal() and len(self.id_number)==7)\
            or (self.id_number[0:2].isalpha() and self.id_number[2:].isdecimal() and len(self.id_number) == 8)):
            self.error = True
            self.error_message += '\n- Δώστε σωστό αριθμό δελτίου!'
        if self.surname == '':
            self.error = True
            self.error_message += '\n- Δώστε επώνυμο!'
        if self.name == '':
            self.error = True
            self.error_message += '\n- Δώστε όνομα!'
        if reason == 'new':
            if self.office_type == 0:
                self.error = True
                self.error_message += '\n- Δώστε είδος Αρχής του εγγράφου!'
        if self.office_name == '':
                self.error = True
                self.error_message += '\n- Δώστε όνομα Προξενικής/Λιμενικής Αρχής!'
        try:
            self.time_data_to_app(self.protocol_date)
        except:
            if not self.protocol_date == '':
                self.error = True
                self.error_message += '\n- Δώστε σωστή μορφή ημερομηνίας πρωτοκόλλου!'
        self.error_message.strip('\n')
        if not self.error:
            self.id_number = Main.entry_formatter(self.id_number)
            self.surname = Main.entry_formatter(self.surname)
            self.name = Main.entry_formatter(self.name)
            if reason == 'new':
                self.office_name = Main.entry_formatter(self.office_name)
                self.office_article = Main.entry_formatter(self.office_article)
                self.save_to_db = data.save_to_database()
                if self.save_to_db:
                    self.create_button.grid_forget()
                    self.new_button.grid(row=0, column=0, sticky='ns')
                    self.disable_widgets([self.f1_1, self.f1_2, self.f1_3_1, self.f1_3_2, self.f1_4])
                    word.create_text_variables()
                else:
                    messagebox.showerror('Σφάλμα!', f'Υπάρχει ήδη δελτίο ταυτότητας με αριθμό {self.id_number} καταχωριμένο στη βάση!')
                    self.office_name = ttk.Combobox(self.f1_3_2, textvariable=self.office_name_variable, values=(), state='readonly')
            elif reason == 'edit':
                return True
        else:
            messagebox.showerror('Σφάλμα!', self.error_message.strip('\n'))
            if reason == 'new':
                self.office_name = ttk.Combobox(self.f1_3_2, textvariable=self.office_name_variable, values=(), state='readonly')

    def new_office(self):
        self.new_office_window = tk.Toplevel(self.root)
        self.new_office_window.title("Καταχώρηση Νέας Αρχής")
        self.new_office_window.resizable(width='false', height='false')
        #self.root.wait_window(self.new_office_window)
        #self.new_office_window.geometry('1000x400')
        self.f_new_office = tk.Frame(self.new_office_window, bg="lightyellow", padx=5, pady=5)
        self.f_new_office.pack(expand=True, fill='both')
        tk.Label(self.f_new_office, text='Προξενική/Λιμενική Αρχη ', bg="lightyellow").pack(side='left')
        self.new_office_name = tk.Entry(self.f_new_office)
        self.new_office_name.pack(side='left')
        self.new_office_name.insert(0, 'στ')
        self.f1_new_office = tk.Frame(self.new_office_window, bg="lightyellow", padx=5, pady=5)
        self.f1_new_office.pack(expand=True, fill='both')
        tk.Button(self.f1_new_office, text='Καταχώρηση Αρχής', command=self.new_office_entry).pack()

    def edit_entry(self):
        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("Επεξεργασία Εγγραφής")
        self.edit_window.resizable(width='false', height='false')
        #self.root.wait_window(self.new_office_window)
        #self.new_office_window.geometry('1000x400')
        self.f_edit_entry = tk.Frame(self.edit_window, bg="lightyellow", padx=5, pady=5)
        self.f_edit_entry.pack(expand=True, fill='both')
        edit_labels = ['Αριθμός Δελτίου', 'Επώνυμο', 'Όνομα', 'Αιτία Ακύρωσης', 'Προξενική/Λιμενική Αρχή', 'Αριθμός Πρωτοκόλλου', 'Ημερομηνία Πρωτοκόλλου']
        for count, label in enumerate(edit_labels):
            tk.Label(self.f_edit_entry, text=f'{label}:', bg="lightyellow").grid(row=count, column=0)
        self.edit_id_number = tk.Entry(self.f_edit_entry)
        self.edit_id_number.grid(row=0, column=1)
        self.edit_id_number.insert(0, data.edit_id_number)
        self.edit_surname = tk.Entry(self.f_edit_entry)
        self.edit_surname.grid(row=1, column=1)
        self.edit_surname.insert(0, data.edit_surname)
        self.edit_name = tk.Entry(self.f_edit_entry)
        self.edit_name.grid(row=2, column=1)
        self.edit_name.insert(0, data.edit_name)
        self.edit_reason = tk.Entry(self.f_edit_entry)
        self.edit_reason_variable = tk.StringVar()
        self.reason_tup = ('Απώλεια', 'Κλοπή', 'Κατάσχεση')
        self.edit_reason = ttk.Combobox(self.f_edit_entry, textvariable=(self.edit_reason_variable), values=self.reason_tup, state='readonly')
        self.edit_reason.grid(row=3, column=1)
        self.edit_reason.current(self.reason_tup.index(data.edit_reason))

        self.edit_office_tup = data.create_office_search_tup()
        self.edit_office_name_variable = tk.StringVar()
        self.edit_office_name = ttk.Combobox(self.f_edit_entry, textvariable=self.edit_office_name_variable, values=self.edit_office_tup, state='readonly')
        self.edit_office_name.current(self.edit_office_tup.index(data.edit_office_name))
        self.edit_office_name.grid(row=4, column=1)

        self.edit_protocol_num = tk.Entry(self.f_edit_entry)
        self.edit_protocol_num.grid(row=5, column=1)
        self.edit_protocol_num.insert(0, data.edit_protocol_num)
        self.edit_protocol_date = tkcalendar.DateEntry(self.f_edit_entry, date_pattern='dd/mm/y', locale='el_GR')
        self.edit_protocol_date.grid(row=6, column=1)
        self.edit_protocol_date.delete(0, 'end')
        self.edit_protocol_date.insert(0, data.edit_protocol_date)
        self.f1_edit_entry = tk.Frame(self.edit_window, bg="lightyellow", padx=5, pady=5)
        self.f1_edit_entry.pack(expand=True, fill='both')

        tk.Button(self.f1_edit_entry, text='Ενημέρωση Εγγραφής', command=data.insert_update_entry).pack()

    def new_office_entry(self):
        self.user_office_entry = self.new_office_name.get().split(' ')
        self.office_article = self.user_office_entry[0]
        self.office_tup = (' '.join(self.user_office_entry[1:]),)
        self.new_office_window.destroy()
        self.office_name.config(values=self.office_tup)
        self.office_name.current(0)
        self.protocol_num_entry.delete(0, 'end')
        self.protocol_date_entry.delete(0, 'end')

    def edit_office(self):
        self.edit_office_window = tk.Toplevel(self.root)
        self.edit_office_window.title("Επεξεργασία Προξενικής/Λιμενικής Αρχής")
        self.edit_office_window.resizable(width='false', height='false')
        #self.root.wait_window(self.new_office_window)
        #self.new_office_window.geometry('1000x400')
        self.f_edit_office = tk.Frame(self.edit_office_window, bg="lightyellow", padx=5, pady=5)
        self.f_edit_office.pack(expand=True, fill='both')
        edit_labels = ['Προς Επεξεργασία Άρχη:', 'Είδος Αρχής:', 'Νέα Ονομασία: Προξενική/Λιμενική Αρχή ']
        for count, label in enumerate(edit_labels):
            tk.Label(self.f_edit_office, text=f'{label}', bg="lightyellow").grid(row=count, column=0)

        self.old_office_tup = data.create_office_search_tup()
        self.old_office_name_variable = tk.StringVar()
        self.old_office_name = ttk.Combobox(self.f_edit_office, textvariable=self.old_office_name_variable, values=self.old_office_tup, state='readonly')
        self.old_office_name.current(0)
        self.old_office_name.grid(row=0, column=1)

        self.type_list = []
        for value in main.office_dict.values():
            self.type_list.append(value)
        self.edit_office_type_variable = tk.StringVar()
        self.edit_office_type = ttk.Combobox(self.f_edit_office, textvariable=self.edit_office_type_variable, values=tuple(self.type_list), state='readonly')
        self.edit_office_type.current(0)
        self.edit_office_type.grid(row=1, column=1)

        self.editted_office_name = tk.Entry(self.f_edit_office)
        self.editted_office_name.grid(row=2, column=1)
        self.editted_office_name.insert(0, 'στ')

        self.f1_edit_office = tk.Frame(self.edit_office_window, bg="lightyellow", padx=5, pady=5)
        self.f1_edit_office.pack(expand=True, fill='both')

        tk.Button(self.f1_edit_office, text='Ενημέρωση Αρχής', command=data.update_office).pack()

    def combobox_selection(self, event):
        self.combo_selection = self.office_name.get()
        data.retrieve_num_date()

    def clear_tree(self):
        x = self.tree.get_children()
        if x != '()':
            for child in x:
                self.tree.delete(child)

    def tree_insert(self):
        for s in Entry.search_results:
            self.tree.insert('', 'end', text=s.id_number, values=(s.surname, s.name, s.reason, s.office_name, s.protocol_num, s.protocol_date, s.timestamp))

    def disable_widgets(self, widgets):
        for widget in widgets:
            if widget.winfo_class() in ('Frame','Labelframe'):
                for child in widget.winfo_children():
                    wtype = child.winfo_class()
                    if wtype not in ('Frame','Labelframe'):
                        child.configure(state='disable')
                    else:
                        self.disable_widgets(child)
            else:
                widget.configure(state='disable')

    def enable_widgets(self, widgets):
        for widget in widgets:
            if widget.winfo_class() in ('Frame','Labelframe'):
                for child in widget.winfo_children():
                    wtype = child.winfo_class()
                    if wtype not in ('Frame','Labelframe'):
                        child.configure(state='normal')
                    else:
                        self.disable_widgets(child)
            else:
                widget.configure(state='normal')

    def reset(self):
        self.tab_parent.pack_forget()
        self.create_widgets()
        '''self.enable_widgets([self.f1_1, self.f1_2, self.f1_3_1, self.f1_3_2, self.f1_4])
        to_delete = [self.id_number_entry, self.surname_entry, self.name_entry, self.protocol_num_entry, self.protocol_date_entry]
        for item in to_delete:
            item.delete(0, 'end')
        self.reason_variable = tk.StringVar(value='Απώλεια')
        #self.office_variable = tk.IntVar()
        self.office_name = ttk.Combobox(self.f1_3_2, textvariable=self.office_name_variable, values=('',), state='readonly')
        self.other_doc_passport_var = tk.IntVar()
        self.other_doc_driver_var = tk.IntVar()'''
            

root = tk.Tk()
main = Main(root)
data = database.Database(main)
word = word.WordCreator(main)
main.create_widgets()
root.mainloop()