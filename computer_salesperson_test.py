def get_basic(host,screen,equipment):
    return host*25+screen*30+equipment*45

def get_range(host,screen,equipment):
    if host == -1 and screen in range(1,80+1) and equipment in range(1,90+1):
        return 'Calculate total'
    elif host in range(1,70+1) and screen in range(1,80+1) and equipment in range(1,90+1):
        return 'In range'
    else:
        return 'Out of range'

def get_total(host,screen,equipment):
    if get_range(host, screen, equipment) == 'Calculate total':
        return 'Calculate total'
    elif get_range(host, screen, equipment) == 'Out of range':
        return 'Out of range'
    else:
        basic = get_basic(host, screen, equipment)
        if basic <= 1000:
            return '{:g}' . format (basic*0.1 + basic)
        elif basic <= 1800:
            return '{:g}' . format(basic*0.15+basic)
        else:
            return '{:g}' . format(basic*0.2+basic)
