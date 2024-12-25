from datetime import datetime, timedelta


def check_input(element):
    if not isinstance(element, str):
        return False
    try:
        datetime.strptime(element, '%Y.%m.%d')
        return True
    except ValueError:
        return False


def count_mondays(valid_date):
    start_date = datetime.strptime(valid_date, '%Y.%m.%d').date()
    end_date = datetime.now().date()
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    count = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 0:  # Понедельник
            count += 1
        current_date += timedelta(days=1)
    return count


def main(lst):
    for element in lst:
        if check_input(element):
            result = count_mondays(element)
            print(result)
            return