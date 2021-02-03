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

def greek_accent_remover(string_name):
    puncts = {'ά': 'α', 'έ': 'ε', 'ή': 'η', 'ί': 'ι', 'ΐ': 'ϊ', 'ό': 'ο', 'ύ': 'υ', 'ώ': 'ω',
                'Ά': 'Α', 'Έ': 'Ε', 'Ή': 'Η', 'Ί': 'Ι', 'Ό': 'Ο', 'Ύ': 'Υ', 'Ώ': 'Ω'}
    dieresis = {'ι': 'ϊ', 'υ': 'ϋ'}
    new_name = ''
    prev_char = 0
    for c in string_name:
        char = c
        if c in puncts.keys():
            char = puncts[c]
        if c in dieresis.keys() and prev_char in ('ά', 'ό', 'έ'):
            char = dieresis[c]
        prev_char = c
        new_name += char
    return new_name

def window_centre_position(window):
        window_width = window.winfo_reqwidth()
        window_height = window.winfo_reqheight()
        # Gets both half the screen width/height and window width/height
        position_right = int(window.winfo_screenwidth()/2 - window_width/2)
        position_down = int(window.winfo_screenheight()/2 - window_height/2)   
        # Positions the window in the center of the page.
        return window.geometry(f"+{position_right}+{position_down}")