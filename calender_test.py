#判断两个单独函数 判断年是否为润，判断月是大月，还是小月，还是二月
import datetime
def year_dec(input):
    if (input % 4 == 0 and input % 100 != 0) or input % 400 == 0:
        return 1 #闰年
    else:
        return 0 #平年

def month_dec(input):
    if input == 2: #2月
        return 0
    elif input in [4,6,9,11]:#小月
        return 1
    else:
        return 2 #大月

def year_month_day_dec(year,month,day):
    if month_dec(month)==0 and year_dec(year) ==1:
        if day == 29:
            return 2
        elif day < 29:
            return 1
        else:
            return 0
    elif month_dec(month)==0 and year_dec(year) ==0:
        if day == 28:
            return 2
        elif day < 28:
            return 1
        else:
            return 0
    elif month_dec(month)==1:
        if day == 30:
            return 2
        elif day < 30:
            return 1
        else:
            return 0
    else:
        if day == 31:
            return 2
        elif day < 31:
            return 1
        else:
            return 0

def get_calender(year,month,day):
    if year in range(1100,4000+1) and month in range(1,12+1) and day in range(1,31+1):
        if month == 12 and day ==31:
            if year == 4000:
                return 'Out of year'
            else:
                detester = str(year+1)+'-1-1'
                date = datetime.datetime.strptime(detester, '%Y-%m-%d')
                return date.strftime('%Y-%m-%d')
        else:
            if year_month_day_dec(year, month, day) == 2:
                detester = str(year)+'-'+str(month+1)+'-'+str(1)
                date = datetime.datetime.strptime(detester, '%Y-%m-%d')
                return date.strftime('%Y-%m-%d')

            elif year_month_day_dec(year, month, day) == 1:
                detester =  str(year)+'-'+str(month)+'-'+str(day+1)
                date = datetime.datetime.strptime(detester, '%Y-%m-%d')
                return date.strftime('%Y-%m-%d')
            else:
                return 'Day out of month'
    else:
        return 'Out of range'


