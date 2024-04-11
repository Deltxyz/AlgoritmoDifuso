error_humedad={
    'B': 'H',
    'Min': 'OFF',
    'A': 'DH'
}

error_temperatura_ventilacion={
    'DH':{
        'B':'MB',
        'Min':'B',
        'A':'M',
        'MA':'A'},
    'OFF':{
        'B':'B',
        'Min':'M',
        'A':'A',
        'MA':'MA'},
    'H':{
        'B':'MB',
        'Min':'B',
        'A':'M',
        'MA':'A'}
}

error_temperatura_sombra={
    'DH':{
        'B':'C',
        'Min':'C',
        'A':'Q',
        'MA':'Q'},
    'OFF':{
        'B':'C',
        'Min':'Q',
        'A':'C',
        'MA':'Q'},
    'H':{
        'B':'Q',
        'Min':'Q',
        'A':'Q',
        'MA':'Q'}
}



error_humedad1 = {
    'MB' : 'HG',
    'B' : 'HP',
    'Min' : 'M',
    'A': 'HP',
    'MA' : 'HG',
}

error_temperatura1 = {
    'HG':{
        'MA' : 'BP',
        'A' : 'M',
        'Min' : 'SP',
        'B' : 'SG',
        'MB' : 'SG'},
    'HP':{
        'MA' :'BG',
        'A' : 'BP',
        'Min' : 'M',
        'B' : 'SP',
        'MB' : 'SG'},
    'M':{
        'MA' : 'BG',
        'A' : 'BP',
        'Min' : 'M',
        'B' : 'SP',
        'MB' : 'SG'},
    'DHP':{
        'MA' :'BG',
        'A' : 'BP',
        'Min' : 'M',
        'B' : 'SP',
        'MB' : 'SG'},
    'DHG':{
        'MA' : 'BP',
        'A' : 'M',
        'Min' : 'SP',
        'B' : 'SG',
        'MB' : 'SG'},
}



error_ph = {
    'M-Ac' : 'Bas-A',
    'Mod-Ac' : 'Bas-Mod',
    'L-Ac' : 'Bas-L',
    'Min': 'M',
    'L-Al' : 'Ac-L',
    'Mod-Al' : 'Ac-Mod',
    'M-Al' : 'Ac-A',
}

error_ce = {
    'MB' : 'SG',
    'B' : 'SP',
    'Min' : 'M',
    'A': 'BP',
    'MA' : 'BG',
    'EA' : 'BC',
}