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