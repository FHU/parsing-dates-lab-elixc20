#parse month should take in the text of the month and return the number as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
    #Use Dictionary
#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_month(month):
    month_dict = {"January": "01", "February": "02", 'March' : "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", 'November': "11", "December": "12"}
    return months[month]

def parse_date(orig_date):
        
    next_date = orig_date.split(',')
    next_date = next_date.split('')
    
    new_month = parse_month(next_date[0])
    new_day = next_date[1]
    new_year = next_date[2]

    def parse_new_date(new_month, new_day, new_year):
        final_date = f'{new_month:02d}/{new_day:02d}/{new_year}'

if __name__ == '__main__':
    final_date = input()
    parse_date(final_date)
    print(parse_date(final_date))
    
