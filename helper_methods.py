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
    puncts = {'ά': 'α', 'έ': 'ε', 'ή': 'η', 'ί': 'ι', 'ΐ': 'ϊ', 'ό': 'ο', 'ύ': 'υ', 'ώ': 'ω',
                'Ά': 'Α', 'Έ': 'Ε', 'Ή': 'Η', 'Ί': 'Ι', 'Ό': 'Ο', 'Ύ': 'Υ', 'Ώ': 'Ω'}
    dieresis = {'ι': 'ϊ', 'υ': 'ϋ'}
    name_no = ''
    prev_char = 0
    for c in filename:
        char = c
        if c in puncts.keys():
            char = puncts[c]
        if char in dieresis.keys() and prev_char in ('ά', 'ό', 'έ'):
            char = dieresis[char]
        prev_char = c
        name_no += char
    return name_no