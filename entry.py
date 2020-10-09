class Entry():
    search_results = []
    def __init__(self, id_number, surname, name, reason, office_name, protocol_num, protocol_date, timestamp):
        self.id_number = id_number
        self.surname = surname
        self.name = name
        self.reason = reason
        self.office_name = office_name
        self.protocol_num = protocol_num
        self.protocol_date = protocol_date
        self.timestamp = timestamp
        Entry.search_results.append(self)