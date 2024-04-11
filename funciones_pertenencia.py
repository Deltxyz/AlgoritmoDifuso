macro_tuneles = {
    'func_membresia':{
        'Error de humedad': {
            'B':'Bajo',
            'Min':'Minimo',
            'A':'Alto'},
        'Error de temperatura':{
            'B':'Bajo',
            'Min':'Minimo',
            'A':'Alto',
            'MA':'Muy alto'},
        'Control de estado de humedad':{
            'DH':'Deshumidificación',
            'OFF':'OFF',
            'H':'Humidificación'},

        'Control de Humedad':{
            'DH':'Deshumidificación',
            'OFF':'OFF',
            'H':'Humidificación'},
        'Ventilacion':{
            'MB': 'Muy Baja',
            'B': 'Baja',
            'M': 'Media',
            'A': 'Alta',
            'MA': 'Muy Alta'},
        'Sombra':{
            'Q': 'Quitar',
            'C': 'Colocar'}
    },
    'parametros':{
        'Error de humedad': {
            'B':[-70, -70, -15, 0],
            'Min':[-15, 0, 15],
            'A':[0, 15, 30, 30]},
        'Error de temperatura':{
            'B':[-25,-25,-8,0],
            'Min':[-8, 0, 8],
            'A':[0, 8, 16],
            'MA':[8, 16, 25, 25]},
        'Control de estado de humedad':{
            'DH':[-1, -1, 0],
            'OFF':[-0.8, 0, 0.8],
            'H':[0, 1, 1]},

        'Control de Humedad':{
            'DH':[-1, -1, 0],
            'OFF':[-0.8, 0, 0.8],
            'H':[0, 1, 1]},
        'Ventilacion':{
            'MB': [-25, -16.7, -8.3],
            'B': [-16.7, -8.3, 0],
            'M': [-8.3, 0, 8.3],
            'A': [0, 8.3, 16.7],
            'MA': [8.3, 16.7, 25]},
        'Sombra':{
            'Q': [0, 0, 1],
            'C': [0, 1, 1]
        }
    }
}

invernadero = {
    'func_membresia':{
        'Error de humedad': {
            'MA':'Muy Alto',
            'A':'Alto',
            'Min':'Minimo',
            'B':'Bajo',
            'MB':'Muy Bajo'},
        'Error de temperatura':{
            'MA':'Muy Alto',
            'A':'Alto',
            'Min':'Minimo',
            'B':'Bajo',
            'MB':'Muy Bajo'},
        'Control de estado de humedad':{
            'HG':'Humidificación Grande',
            'HP':'Humidificación Pequeña',
            'M':'Mantener',
            'DHP':'Des-Humidificación Pequeña',
            'DHG':'Des-Humidificación Grande'},

        'Control de Humedad':{
            'HumG':'Humidificación Grande',
            'HumP':'Humidificación Pequeña',
            'M':'Mantener',
            'DHumP':'Des-Humidificación Pequeña',
            'DHumG':'Des-Humidificación Grande'},
        'Control de Temperatura':{
            'SG': 'Subida Grande',
            'SP': 'Subida Pequeña',
            'M': 'Media',
            'BP': 'Bajada Pequeña',
            'BG': 'Bajada Grande'},
    },
    'parametros':{
        'Error de humedad': {
            'MA':[10, 30, 30],
            'A':[0, 10, 30],
            'Min':[-10, 0, 10],
            'B':[-30, -10, 0],
            'MB':[-70, -30, -10]},
        'Error de temperatura':{
            'MA':[14, 25, 25],
            'A':[0, 7, 14],
            'Min':[-5, 0, 5],
            'B':[-14, -7, 0],
            'MB':[-30, -30, -14]},
        'Control de estado de humedad':{
            'HG':[50, 100, 100],
            'HP':[0, 50, 100],
            'M':[-50, 0, 50],
            'DHP':[-100, -50, 0],
            'DHG':[-100, -100, -50]},

        'Control de Humedad':{
            'HG':[50, 100, 100],
            'HP':[0, 50, 100],
            'M':[-50, 0, 50],
            'DHP':[-100, -50, 0],
            'DHG':[-100, -100, -50]},
        'Control de Temperatura':{
            'SG': [50, 100, 100],
            'SP': [0, 50, 100],
            'M': [-50, 0, 50],
            'BP': [-100, -50, 0],
            'BG': [-100, -100, -50]},
    }
}

agua_sustratos = {
    'func_membresia':{
        'Error de pH': {
            'M-Ac':'Muy Ácido',
            'Mod-Ac':'Moderadamente Ácido',
            'L-Ac':'Ligeramente Ácido',
            'Min':'Minimo',
            'L-Al':'Ligeramente Alcalino',
            'Mod-Al':'Moderadamente Alcalino',
            'M-Al':'Muy Alcalino'},
        'Error de Conductividad':{
            'MB':'Muy Baja',
            'B':'Baja',
            'Min':'Minima',
            'A':'Alta',
            'MA':'Muy Alta',
            'EA':'Extremadamente Alta'},

        'Control de pH':{
            'Bas-A':'Basificación Alta',
            'Bas-Mod':'Basificación Moderada',
            'Bas-L':'Basificación Ligera',
            'M':'Mantener',
            'Ac-L':'Acidificación Ligera',
            'Ac-Mod':'Acidificación Moderada',
            'Ac-A':'Acidificación Alta'},
        'Control de CE':{
            'BC': 'Bajada Crítica',
            'BG': 'Bajada Grande',
            'BP': 'Bajada Pequeña',
            'M': 'Mantener',
            'SP': 'Subida Pequeña',
            'SM': 'Subida Moderada'},
    },
    'parametros':{
        'Error de pH': {
            'M-Ac':[-7, -4, -2.5],
            'Mod-Ac':[-4, -2.5, -1],
            'L-Ac':[-2.5, -1, 0],
            'Min':[-0.5, 0, 0.5],
            'L-Al':[0, 1, 2.5],
            'Mod-Al':[1, 2.5, 4],
            'M-Al':[2.5, 4, 7]},
        'Error de Conductividad':{
            'MB':[-3, -3, -1.5],
            'B':[-3, -1.5, 0],
            'Min':[-0.75, 0, 0.75],
            'A':[0, 1.5, 3],
            'MA':[1.5, 3, 4.5],
            'EA':[3, 4.5, 4.5]},

        'Control de pH':{
            'Bas-A':[ 60, 100, 100],
            'Bas-Mod':[30, 60, 100],
            'Bas-L':[0, 30, 60],
            'M':[-30, 0, 30],
            'Ac-L':[-60, -30, 0],
            'Ac-Mod':[-100, -60, -30],
            'Ac-A':[-100, -100, -60]},
        'Control de CE':{
            'BC': [-100, -100, -60],
            'BG': [-100, -60, -30],
            'BP': [-60, -30, 0],
            'M': [-35, 0, 50],
            'SP': [0, 50, 100],
            'SG': [50, 100, 100]}
    }
}