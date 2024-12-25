from datetime import datetime, timedelta

def check_input(subarray):
    if len(subarray) != 2:
        return False
    time, number = subarray
    if not isinstance(time, str) or not isinstance(number, int) or number <= 0:
        return False
    try:
        datetime.strptime(time, '%H.%M')
        return True
    except ValueError:
        return False

def calculate_time(subarray):
    time_str, n = subarray
    time = datetime.strptime(time_str, '%H.%M')
    delta = timedelta(hours=n, minutes=n)
    new_time = time + delta
    return new_time.strftime('%H.%M')

def main(lst):
    for subarray in lst:
        if check_input(subarray):
            result = calculate_time(subarray)
            print(result)
            return