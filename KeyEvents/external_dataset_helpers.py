import calendar

# Used to convert sport key events date format to [month, day, month, day]
def convert_date_to_ints(date):
    abbr_to_num = list(calendar.month_abbr)
    date = date.replace('–', '-')
    # check if event occurs over multiple days
    if '-' in date:
        start_end = date.split('-', maxsplit=2)
        start = start_end[0]
        end = start_end[1]
        start_month_day = start.split(' ', maxsplit=2)
   #     print(start_month_day)
        start_month = int(abbr_to_num.index(start_month_day[0][0:3]))
        start_day = int(start_month_day[1])

        end_month_day = end.split(' ', maxsplit=2)
        if len(end_month_day) < 2:
            end_month = start_month
            end_day = int(end_month_day[0])
        else:    
            end_month = int(abbr_to_num.index(end_month_day[0][0:3]))
            end_day = int(end_month_day[1])
    else:
        start_month_day = date.split(' ', maxsplit=2)
        start_month = int(abbr_to_num.index(start_month_day[0][0:3]))
    #    print(start_month_day)
        start_day = int(start_month_day[1])
        end_month = start_month
        end_day = start_day
    
    # sanity checks
    assert start_month <= end_month
    if start_month == end_month:
        assert start_day <= end_day
        
    return start_month, start_day, end_month, end_day