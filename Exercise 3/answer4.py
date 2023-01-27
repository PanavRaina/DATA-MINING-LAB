month_dict = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12"
}
def split_date(date):
    day, month, year = date.split("-")
    month = month_dict[month]
    return (year, month, day)

print(split_date("8-MAR-22"))
