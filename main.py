#parse month should take in the text of the month and return the number as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
    #Use Dictionary
#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION

def parse_date(string_date):
    
    if string_date != "-1":
        month, day, year = string_date.split(' ')
        day = int(day.replace(",", ""))
        day = '{:02d}'.format(day)
        month_dictionary = {"January": "01", "February": "02", 'March' : "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", 'November': "11", "December": "12" }
        month = month_dictionary.get(month,"01")
        separator = '/'
        reg_date = separator.join((month, day, year))
        return reg_date
    
if __name__ == '__main__':
    string_date = input()
    print(reg_date)
    
