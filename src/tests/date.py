import datetime

def test_format_firebase_timestamp():
    string_time = 'Thu, 10 Oct 2019 03:00:00 GMT'
    date_time_obj = datetime.datetime.strptime(string_time, '%a, %d %b %Y %H:%M:%S GMT')
    assert datetime.datetime(2019, 10, 10, 3, 0, 0) == date_time_obj
