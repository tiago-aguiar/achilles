from datetime import datetime

def firebase_todate(string_date):
    return datetime.strptime(string_date, '%a, %d %b %Y %H:%M:%S GMT')
