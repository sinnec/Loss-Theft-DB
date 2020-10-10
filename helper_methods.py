from datetime import datetime

def datetime_formatter(timestring, from_time, to_time):
    protocol_date_obj = datetime.strptime(timestring, from_time)
    return protocol_date_obj.strftime(to_time)

def latin_to_greek(name):
    eng = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ'
    el = 'αβψδεφγηιξκλμνοπρστθωςχυζΑΒΨΔΕΦΓΗΙΞΚΛΜΝΟΠΡΣΤΘΩςΧΥΖ'
    new_name = ''
    for i in name:
        if i in eng:
            new_name += el[eng.index(i)]
        else:
            new_name += i
    return new_name

def greek_accent_remover(filename):
    puncts = {'ά': 'α', 'έ': 'ε', 'ή': 'η', 'ί': 'ι', 'ό': 'ο', 'ύ': 'υ', 'ώ': 'ω'}
    name_no = ''
    for c in filename.lower():
        char = c
        for t in puncts.keys():
            if c in t:
                char = puncts[c]
        name_no += char
    return name_no