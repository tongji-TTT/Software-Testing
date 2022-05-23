
def get_str(total):
    return '{:g}' . format(total)

def get_total(minutes,times):
    if minutes in range(0,44640+1) and times in range(0,11+1):
        if minutes <= 60:
            if times <=1:
                return get_str(25+minutes*0.15*(1-0.01))
            else: return get_str(25+minutes*0.15)
        elif minutes <=120:
            if times <=2:
                return get_str(25+minutes*0.15*(1-0.015))
            else: return get_str(25+minutes*0.15)
        elif minutes <=180:
            if times <=3:
                return get_str(25+minutes*0.15*(1-0.02))
            else: return get_str(25+minutes*0.15)
        elif minutes <=300:
            if times <=3:
                return  get_str(25+minutes*0.15*(1-0.025))
            else: return get_str(25+minutes*0.15)
        else:
            if times <=6:
                return get_str(25+minutes*0.15*(1-0.03))
            else: return get_str(25+minutes*0.15)
    else:
        return 'Out of range'



