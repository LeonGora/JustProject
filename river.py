

a = {'S': 1,
     't': 3*60*60,
     't_bk': None,
     'V': None,
     'V_bk': None}
b = {'S': 1,
     't': 12*60*60,
     'V': None}
V_river = None

b['V'] = b['s'] / b['t']

V_river = b['V']

a['V'] = b['s'] / b['t']

a['V_bk'] = a['V'] - 2*V_river

a['t_bk'] = a['S']/a['V_bk']




